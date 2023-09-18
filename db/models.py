import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from os import getenv

from dotenv import load_dotenv

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = sq.Column(sq.Integer, primary_key=True)
    vk_user_id = sq.Column(sq.Integer, unique=True)
    first_name = sq.Column(sq.String(length=40))
    last_name = sq.Column(sq.String(length=40))
    sex = sq.Column(sq.Integer)
    age = sq.Column(sq.Integer)
    link = sq.Column(sq.String(length=400))

    def __str__(self):
        return f"User: {self.vk_user_id}: {self.first_name} {self.last_name}"


class Favorite(Base):
    __tablename__ = "favorite"

    id = sq.Column(sq.Integer, primary_key=True)
    user = sq.Column(sq.Integer, sq.ForeignKey("user.id"))
    favorite_user = sq.Column(sq.Integer, sq.ForeignKey("user.id"))

    def __str__(self):
        return (f"User: {self.user.first_name} {self.user.last_name}; "
                f"Favorite:{self.favorite_user.first_name} {self.favorite_user.last_name}")


class BlackList(Base):
    __tablename__ = "blacklist"

    id = sq.Column(sq.Integer, primary_key=True)
    user = sq.Column(sq.Integer, sq.ForeignKey("user.id"))
    black_listed_user = sq.Column(sq.Integer, sq.ForeignKey("user.id"))

    def __str__(self):
        return (f"User: {self.user.first_name} {self.user.last_name}; "
                f"Favorite:{self.black_listed_user.first_name} {self.black_listed_user.last_name}")


class Phote(Base):
    __tablename__ = "photo"

    id = sq.Column(sq.Integer, primary_key=True)
    user = sq.Column(sq.Integer, sq.ForeignKey("user.id"))
    photo_data = sq.Column(sq.LargeBinary)


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    load_dotenv()
    db_host = getenv('DB_HOST')
    db_port = getenv('DB_PORT')
    db_user = getenv('DB_USER')
    db_pass = getenv('DB_PASS')
    db_name = getenv('DB_NAME')


    engine = sq.create_engine(f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}/{db_name}",
                              echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    create_tables(engine)
