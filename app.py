from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
import falcon
from middleware import SQLAlchemySessionManager
from api import ContactCRUD

engine = create_engine('sqlite:///database/database.db')
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

app = falcon.API(middleware=[
    SQLAlchemySessionManager(Session),
])