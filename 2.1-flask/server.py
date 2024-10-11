from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import datetime

# Инициализация приложения Flask
app = Flask(__name__)

# Конфигурация базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'

# Инициализация расширений
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


# Модель для пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


# Модель для объявления
class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# Схема для сериализации объявлений
class AdSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ad
        include_fk = True


ad_schema = AdSchema()
ads_schema = AdSchema(many=True)


# Создание пользователя (регистрация)
@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400

    user = User(email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


# Логин и получение JWT токена
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200


# Получение всех объявлений
@app.route('/ads', methods=['GET'])
def get_ads():
    ads = Ad.query.all()
    return ads_schema.jsonify(ads)


# Получение конкретного объявления
@app.route('/ads/<int:id>', methods=['GET'])
def get_ad(id):
    ad = Ad.query.get_or_404(id)
    return ad_schema.jsonify(ad)


# Создание нового объявления (только для авторизованных пользователей)
@app.route('/ads', methods=['POST'])
@jwt_required()
def create_ad():
    title = request.json.get('title')
    description = request.json.get('description')
    user_id = get_jwt_identity()

    if not title or not description:
        return jsonify({"error": "Title and description are required"}), 400

    new_ad = Ad(title=title, description=description, owner_id=user_id)
    db.session.add(new_ad)
    db.session.commit()

    return ad_schema.jsonify(new_ad), 201


# Редактирование объявления (только владелец)
@app.route('/ads/<int:id>', methods=['PUT'])
@jwt_required()
def update_ad(id):
    ad = Ad.query.get_or_404(id)
    user_id = get_jwt_identity()

    if ad.owner_id != user_id:
        return jsonify({"error": "You are not authorized to update this ad"}), 403

    ad.title = request.json.get('title', ad.title)
    ad.description = request.json.get('description', ad.description)
    db.session.commit()

    return ad_schema.jsonify(ad)


# Удаление объявления (только владелец)
@app.route('/ads/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_ad(id):
    ad = Ad.query.get_or_404(id)
    user_id = get_jwt_identity()

    if ad.owner_id != user_id:
        return jsonify({"error": "You are not authorized to delete this ad"}), 403

    db.session.delete(ad)
    db.session.commit()

    return jsonify({"message": "Ad deleted successfully"}), 200


# Инициализация базы данных
with app.app_context():
    db.create_all()


# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
