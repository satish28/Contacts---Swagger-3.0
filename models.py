from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context


Base = declarative_base()

class Contacts(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact = Column(String)
    timestamp = Column(String)

    @property
    def serialize(self):
        return {
        'id' : self.id,
	    'name' : self.name,
	    'contact' : self.contact,
        'timestamp' : self.timestamp
	        }

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

engine = create_engine('sqlite:///contacts.db')
Base.metadata.create_all(engine)
