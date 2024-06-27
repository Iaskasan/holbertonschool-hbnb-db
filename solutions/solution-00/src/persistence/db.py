from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.base import Base
from src.persistence.repository import Repository
from src.config import SQLALCHEMY_DATABASE_URI
from src.models.user import User
from src.models.city import City
from src.models.country import Country
from src.models.review import Review
from src.models.amenity import Amenity
from src.models.place import Place

class DBRepository(Repository):
    def __init__(self) -> None:
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_all(self, model_name: str) -> list:
        model = self._get_model_class(model_name)
        if model:
            return self.session.query(model).all()
        return []

    def get(self, model_name: str, obj_id: str):
        model = self._get_model_class(model_name)
        if model:
            return self.session.query(model).filter_by(id=obj_id).first()
        return None

    def reload(self):
        self.session.rollback()

    def save(self, obj: Base):
        self.session.add(obj)
        self.session.commit()

    def update(self, obj: Base):
        self.session.commit()

    def delete(self, obj: Base) -> bool:
        self.session.delete(obj)
        self.session.commit()
        return True

    def _get_model_class(self, model_name: str):
        # Mapping of model name strings to actual model classes
        model_mapping = {
            'user': User,
            'city': City,
            'country': Country,
            'review': Review,
            'amenity': Amenity,
            'place': Place,
        }
        return model_mapping.get(model_name.lower())
