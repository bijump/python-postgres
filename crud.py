from datetime import datetime

from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, User,Comment,Post
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from obj import admin_user,post_1,post_2

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    recreate_database()
    # add_data()
    with session_scope() as s:
        s.add(admin_user)
    with session_scope() as s:
        s.add(post_1)
    with session_scope() as s:
        s.add(post_2)
    with session_scope() as s:
        p=s.query(Post).filter_by(id=2).first()
        print(p.body)