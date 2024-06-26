from src.models.base import Base
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime
from src import db 
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = 'users'  # Nom de la table dans la base de données

    id = db.Column(String(36), primary_key=True)
    email = db.Column(String(120), unique=True, nullable=False)
    password_hash = db.Column(String(128), nullable=False)
    is_admin = db.Column(Boolean, default=False)
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, onupdate=datetime.now)

    def __init__(self, email: str, password: str, is_admin: bool = False, **kwargs) -> None:
        super().__init__(**kwargs)
        self.email = email
        self.set_password(password)
        self.is_admin = is_admin

    def __repr__(self) -> str:
        return f"<User {self.id} ({self.email})>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
    
    def set_password(self, password: str) -> None:
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password_hash, password)
    

    @staticmethod
    def create(user_data: dict) -> "User":
        email = user_data.get("email")
        password = user_data.get("password")
        is_admin = user_data.get("is_admin", False)

        new_user = User(email=email, password=password, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()

        return new_user

    @staticmethod
    def update(user_id: str, data: dict) -> "User | None":
        user = User.query.get(user_id)

        if not user:
            return None

        if "email" in data:
            user.email = data["email"]
        if "password" in data:
            user.set_password(data["password"])
        if "is_admin" in data:
            user.is_admin = data["is_admin"]

        db.session.commit()

        return user
    
    @staticmethod
    def get_by_id(user_id: str) -> "User | None":
        return User.query.get(user_id)
    
    @staticmethod
    def get_all() -> list["User"]:
        return User.query.all()