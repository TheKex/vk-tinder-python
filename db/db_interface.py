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
    existed_user = db_session.query(User).where(User.vk_user_id == vk_user_id).first()

    if existed_user is not None:
        user = existed_user
    else:
        user = User()

    user.vk_user_id = vk_user_id
    user.first_name = first_name
    user.last_name = last_name
    user.sex = sex
    user.age = datetime.today().year - datetime.strptime(birthdate, '%d.%m.%Y').date().year
    user.link = link

    if existed_user is None:
        db_session.add(user)

    if photos is not None:
        for photo_data in photos:
            photo = Phote()
            photo.user = user
            photo.photo_data = photo_data
            db_session.add(photo)

    db_session.commit()


def add_favorite(db_session: db.orm.Session, current_user_vk_id: int, favorite_user_vk_id: int):
    user = get_user_by_vk_id(db_session, current_user_vk_id)
    favorite = get_user_by_vk_id(db_session, favorite_user_vk_id)
    favor = Favorite()
    favor.user = user.id
    favor.favorite_user = favorite.id
    db_session.add(favor)
    db_session.commit()


def get_favorites(db_session: db.orm.Session, current_user_vk_id: int):
    user = get_user_by_vk_id(db_session, current_user_vk_id)
    users = db_session.query(Favorite).where(Favorite.user == user.id).all()
    if len(users) == 0:
        return []
    res_users = [db_session.query(User).where(User.id == user.favorite_user).first() for user in users]
    res_users = [f"{user.first_name} {user.last_name}\nПрофиль: {user.link}" for user in res_users]
    return res_users


def get_user_by_vk_id(db_session: db.orm.Session, user_vk_id: int):
    user = db_session.query(User).where(User.vk_user_id == user_vk_id).first()
    return user


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

