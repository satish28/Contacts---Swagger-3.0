from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Contacts, Users

### Intiating the DB Connection

engine = create_engine("sqlite:///contacts.db")
DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_contact():
    contacts = session.query(Contacts).all()
    contacts = [contact.serialize for contact in contacts]
    return contacts


def update(id, body):
    contact = session.query(Contacts).filter_by(id=id).one()
    contact.name = body['name']
    contact.contact = body['contact']
    contact.timestamp = get_timestamp()


def create(body):
    name = body['name']
    contact = body['contact']
    new_contact = Contacts(name=name, contact=contact, timestamp=get_timestamp())
    session.add(new_contact)
    session.commit()
    
def delete(id):
    contact = session.query(Contacts).filter_by(id=id).one()
    session.delete(contact)
    session.commit()

def create_testuser():
    name = "admin"
    password = "secret"
    new_user = Users(name=name)  
    new_user.hash_password(password)
    session.add(new_user)
    session.commit()
