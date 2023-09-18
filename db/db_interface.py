from os import getenv
from enum import Enum
from datetime import datetime

from dotenv import load_dotenv
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from db.models import create_tables, User, Favorite, Phote, BlackList


def add_user(db_session: db.orm.Session,
             vk_user_id: int,
             first_name: str,
             last_name: str,
             sex: int,
             birthdate: str,
             link: str,
             photos: list = None):
    user = User()
    user.vk_user_id = vk_user_id
    user.first_name = first_name
    user.last_name = last_name
    user.sex = sex
    user.age = datetime.today().year - datetime.strptime(birthdate, '%d.%m.%Y').date().year
    user.link = link

    db_session.add(user)
    if photos is not None:
        for photo_data in photos:
            photo = Phote()
            photo.user = user
            photo.photo_data = photo_data
            db_session.add(photo)

    db_session.commit()


def get_user_by_vk_id(db_session: db.orm.Session, user_vk_id: int):
    user = db_session.query(User).where(User.vk_user_id == user_vk_id).first()
    return user


def add_to_favorite(db_session: db.orm.Session, user: User, favorite: User):
    favorite_user = Favorite()
    favorite_user.user = user
    favorite_user.favorite_user = favorite
    db_session.add(favorite_user)
    db_session.commit()



load_dotenv()
db_host = getenv('DB_HOST')
db_port = getenv('DB_PORT')
db_user = getenv('DB_USER')
db_pass = getenv('DB_PASS')
db_name = getenv('DB_NAME')

print(f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}")

engine = db.create_engine(f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}",
                          echo=True)

Session = sessionmaker(bind=engine)
session = Session()
