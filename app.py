from flask import render_template, redirect
import connexion
from models import Users
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#DB Connection
engine = create_engine("sqlite:///contacts.db")
DBSession = sessionmaker(bind=engine)
session = DBSession()

    	

# Create the application instance
app = connexion.App(__name__, specification_dir='./')


def basic_auth(username, password, required_scopes=None):
    user = session.query(Users).filter_by(name=username).one()
    print(user.name)
    if user and user.verify_password(password):
        info = {'sub': username, 'scope': ''}
    else:
        # optional: raise exception for custom error response
        return None
    return info

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return redirect("/v1/ui/")

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
