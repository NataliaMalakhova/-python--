from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Инициализация FastAPI
app = FastAPI()

# Конфигурация базы данных (SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./advertisements.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Конфигурация для работы с паролями и токенами
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "secret_key_for_jwt"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 48  # 48 часов

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Модели базы данных
# Модель пользователя в БД
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")
    is_active = Column(Boolean, default=True)


# Модель объявления в БД
class Advertisement(Base):
    __tablename__ = "advertisements"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    price = Column(Float)
    author_id = Column(Integer)  # ID автора объявления
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)


# Модель для создания пользователя
class UserCreate(BaseModel):
    username: str
    password: str
    role: Optional[str] = "user"


# Модель для обновления данных пользователя
class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None


class AdvertisementCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: float


class AdvertisementUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


# Модель для входа
class Token(BaseModel):
    access_token: str
    token_type: str


# Модель для данных токена
class TokenData(BaseModel):
    username: Optional[str] = None


# Вспомогательные функции для паролей и токенов
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Получение текущего пользователя по JWT токену
def get_current_user(token: str = Depends(oauth2_scheme), db: SessionLocal = Depends(SessionLocal)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=403, detail="Invalid token")
        token_data = TokenData(username=username)
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")

    user = db.query(User).filter(User.username == token_data.username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Ограничения для пользователей
def admin_required(user: User = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Insufficient permissions")


def user_required(user: User = Depends(get_current_user)):
    if user.role not in ["user", "admin"]:
        raise HTTPException(status_code=403, detail="Insufficient permissions")


# Роуты для аутентификации и создания токена
@app.post("/login", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Роуты для управления пользователями
@app.post("/user", response_model=dict)
def create_user(user: UserCreate, db: SessionLocal = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created", "id": db_user.id}


# Получение пользователя по id (GET /user/{user_id})
@app.get("/user/{user_id}", response_model=dict)
def get_user(user_id: int, db: SessionLocal = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": db_user.id,
        "username": db_user.username,
        "role": db_user.role,
        "is_active": db_user.is_active
    }


# Обновление данных пользователя (PATCH /user/{user_id})
@app.patch("/user/{user_id}", response_model=dict)
def update_user(user_id: int, user: UserUpdate, current_user: User = Depends(user_required),
                db: SessionLocal = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if db_user.id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="You don't have permission to update this user")

    if user.username:
        db_user.username = user.username
    if user.password:
        db_user.hashed_password = get_password_hash(user.password)
    if user.role and current_user.role == "admin":
        db_user.role = user.role

    db.commit()
    return {"message": "User updated successfully"}


# Удаление пользователя (DELETE /user/{user_id})
@app.delete("/user/{user_id}", response_model=dict)
def delete_user(user_id: int, current_user: User = Depends(user_required), db: SessionLocal = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if db_user.id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="You don't have permission to delete this user")

    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}


# Роуты для управления объявлениями
@app.post("/advertisement", response_model=dict)
def create_advertisement(advert: AdvertisementCreate, current_user: User = Depends(user_required),
                         db: SessionLocal = Depends(get_db)):
    new_advert = Advertisement(
        title=advert.title,
        description=advert.description,
        price=advert.price,
        author_id=current_user.id  # Автором является текущий пользователь
    )
    db.add(new_advert)
    db.commit()
    db.refresh(new_advert)
    return {"message": "Advertisement created", "id": new_advert.id}


@app.get("/advertisement/{advertisement_id}", response_model=dict)
def get_advertisement(advertisement_id: int, db: SessionLocal = Depends(get_db)):
    advert = db.query(Advertisement).filter(Advertisement.id == advertisement_id).first()

    if not advert:
        raise HTTPException(status_code=404, detail="Advertisement not found")

    return {
        "id": advert.id,
        "title": advert.title,
        "description": advert.description,
        "price": advert.price,
        "author_id": advert.author_id,
        "created_at": advert.created_at,
    }


@app.patch("/advertisement/{advertisement_id}", response_model=dict)
def update_advertisement(advertisement_id: int, advert: AdvertisementUpdate,
                         current_user: User = Depends(user_required), db: SessionLocal = Depends(get_db)):
    db_advert = db.query(Advertisement).filter(Advertisement.id == advertisement_id).first()

    if not db_advert:
        raise HTTPException(status_code=404, detail="Advertisement not found")

    if db_advert.author_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="You don't have permission to update this advertisement")

    if advert.title is not None:
        db_advert.title = advert.title
    if advert.description is not None:
        db_advert.description = advert.description
    if advert.price is not None:
        db_advert.price = advert.price

    db.commit()
    return {"message": "Advertisement updated successfully"}


@app.delete("/advertisement/{advertisement_id}", response_model=dict)
def delete_advertisement(advertisement_id: int, current_user: User = Depends(user_required),
                         db: SessionLocal = Depends(get_db)):
    db_advert = db.query(Advertisement).filter(Advertisement.id == advertisement_id).first()

    if not db_advert:
        raise HTTPException(status_code=404, detail="Advertisement not found")

    if db_advert.author_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="You don't have permission to delete this advertisement")

    db.delete(db_advert)
    db.commit()
    return {"message": "Advertisement deleted successfully"}


@app.get("/advertisement", response_model=List[dict])
def search_advertisements(title: Optional[str] = None, author_id: Optional[int] = None,
                          db: SessionLocal = Depends(get_db)):
    query = db.query(Advertisement)

    if title:
        query = query.filter(Advertisement.title.contains(title))
    if author_id:
        query = query.filter(Advertisement.author_id == author_id)

    adverts = query.all()

    return [
        {
            "id": advert.id,
            "title": advert.title,
            "description": advert.description,
            "price": advert.price,
            "author_id": advert.author_id,
            "created_at": advert.created_at,
        }
        for advert in adverts
    ]
