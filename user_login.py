from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine('mysql+pymysql://root:mysql123@localhost:3306/internassistantdb', echo=True)
Base = declarative_base()

# create a Session
Session = scoped_session(sessionmaker(bind=engine))
session = Session()


class login(Base):
    """"""
    __tablename__ = "login"

    id = Column(String(100), primary_key=True)
    user_name = Column(String(40), nullable=False)
    email_id = Column(String(100,), nullable=False, unique=True)

    def __init__(self, id, user_name, email_id):
        """"""
        self.id = id
        self.user_name = user_name
        self.email_id = email_id

    @staticmethod
    def get(user_id):
        user =  session.query(login).filter(login.id == user_id).with_entities(login.id, login.user_name,
                                                                              login.email_id).first()
        if not user:
            return None

        user = login(id_=user[0], name=user[1], email=user[2])
        return user

    @staticmethod
    def create(id_, name, email):
        u = users(user_name=user_name, email_id=user_email, password=user_password, phone=user_phone,
                  user_type=user_type)
        u = login(id=id_, user_name=name, email_id=email)
        session.add(u)
        session.commit()





