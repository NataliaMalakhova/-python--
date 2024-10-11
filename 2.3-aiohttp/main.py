from aiohttp import web
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import datetime
from passlib.hash import bcrypt
import jwt
from functools import wraps

# Конфигурация приложения
JWT_SECRET = 'your_jwt_secret'
app = web.Application()

# Настройка SQLAlchemy
Base = declarative_base()
engine = create_engine('sqlite:///ads.db')
Session = sessionmaker(bind=engine)
session = Session()


# Модель пользователя
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)

    def hash_password(self, password):
        self.password_hash = bcrypt.hash(password)


# Модель объявления
class Ad(Base):
    __tablename__ = 'ads'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    owner = relationship("User")


Base.metadata.create_all(engine)


# Утилита для создания JWT токенов
def create_jwt_token(user_id):
    payload = {'user_id': user_id}
    token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
    return token


# Декоратор для проверки авторизации
# async def auth_required(handler):
#     async def middleware(request):
#         token = request.headers.get('Authorization', None)
#         if not token:
#             return web.json_response({'error': 'Authorization token is missing'}, status=401)
#
#         try:
#             payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
#             user = session.query(User).get(payload['user_id'])
#             if not user:
#                 return web.json_response({'error': 'Invalid token'}, status=401)
#         except jwt.ExpiredSignatureError:
#             return web.json_response({'error': 'Token has expired'}, status=401)
#         except jwt.InvalidTokenError:
#             return web.json_response({'error': 'Invalid token'}, status=401)
#
#         request['user'] = user
#         return await handler(request)
#
#     return middleware


def auth_required(handler):
    @wraps(handler)
    async def middleware(request):
        token = request.headers.get('Authorization', None)
        if not token:
            return web.json_response({'error': 'Authorization token is missing'}, status=401)

        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            user = session.query(User).get(payload['user_id'])
            if not user:
                return web.json_response({'error': 'Invalid token'}, status=401)
        except jwt.ExpiredSignatureError:
            return web.json_response({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return web.json_response({'error': 'Invalid token'}, status=401)

        request['user'] = user
        return await handler(request)  # Обратите внимание, что здесь используется await

    return middleware


# Регистрация нового пользователя
async def register(request):
    data = await request.json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return web.json_response({'error': 'Email and password are required'}, status=400)

    if session.query(User).filter_by(email=email).first():
        return web.json_response({'error': 'User already exists'}, status=400)

    new_user = User(email=email)
    new_user.hash_password(password)
    session.add(new_user)
    session.commit()

    return web.json_response({'message': 'User registered successfully'}, status=201)


# Логин и получение JWT токена
async def login(request):
    data = await request.json()
    email = data.get('email')
    password = data.get('password')

    user = session.query(User).filter_by(email=email).first()
    if not user or not user.verify_password(password):
        return web.json_response({'error': 'Invalid credentials'}, status=401)

    token = create_jwt_token(user.id)
    return web.json_response({'token': token}, status=200)


# Получение всех объявлений
async def get_ads(request):
    ads = session.query(Ad).all()
    ads_list = [{'id': ad.id, 'title': ad.title, 'description': ad.description, 'owner_id': ad.owner_id} for ad in ads]
    return web.json_response(ads_list)


# Получение конкретного объявления
async def get_ad(request):
    ad_id = request.match_info['id']
    ad = session.query(Ad).get(ad_id)
    if not ad:
        return web.json_response({'error': 'Ad not found'}, status=404)

    return web.json_response({'id': ad.id, 'title': ad.title, 'description': ad.description, 'owner_id': ad.owner_id})


# Создание нового объявления (только для авторизованных пользователей)
@auth_required
async def create_ad(request):
    data = await request.json()
    title = data.get('title')
    description = data.get('description')
    user = request['user']

    if not title or not description:
        return web.json_response({'error': 'Title and description are required'}, status=400)

    new_ad = Ad(title=title, description=description, owner_id=user.id)
    session.add(new_ad)
    session.commit()

    return web.json_response(
        {'id': new_ad.id, 'title': new_ad.title, 'description': new_ad.description, 'owner_id': new_ad.owner_id},
        status=201)


# Редактирование объявления (только владелец)
@auth_required
async def update_ad(request):
    ad_id = request.match_info['id']
    ad = session.query(Ad).get(ad_id)
    user = request['user']

    if not ad or ad.owner_id != user.id:
        return web.json_response({'error': 'You are not authorized to edit this ad'}, status=403)

    data = await request.json()
    ad.title = data.get('title', ad.title)
    ad.description = data.get('description', ad.description)
    session.commit()

    return web.json_response({'id': ad.id, 'title': ad.title, 'description': ad.description, 'owner_id': ad.owner_id})


# Удаление объявления (только владелец)
@auth_required
async def delete_ad(request):
    ad_id = request.match_info['id']
    ad = session.query(Ad).get(ad_id)
    user = request['user']

    if not ad or ad.owner_id != user.id:
        return web.json_response({'error': 'You are not authorized to delete this ad'}, status=403)

    session.delete(ad)
    session.commit()

    return web.json_response({'message': 'Ad deleted successfully'}, status=200)


# Маршруты
app.router.add_post('/register', register)
app.router.add_post('/login', login)
app.router.add_get('/ads', get_ads)
app.router.add_get('/ads/{id}', get_ad)
app.router.add_post('/ads', create_ad)
app.router.add_put('/ads/{id}', update_ad)
app.router.add_delete('/ads/{id}', delete_ad)

# Запуск сервера
if __name__ == '__main__':
    web.run_app(app, port=8000)
