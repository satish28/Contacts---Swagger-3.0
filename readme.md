## Contacts API.

A simple demo API built to learn how to build a an API with connexion and Swagger OAS 3.0

### Objectives

1. To understand the basic structure of OAS 3.0 specification. [Done]
2. To build a simple Contacts API which supports the following functionality. [Done]
    - GET /contact returns a list of existing contacts.
    - POST /contact create a new contact.
    - Delete /contact delete a contact given an id.
    - Put /contact update a contact given an id
3. Use Basic Authentication. POST, DELETE and PUT methods should be available only post authentication. [Done]
4. Write test cases to validate the API calls. (Test suite with pytest or unittest.) [Todo]

#### Requirements

1. Python3.7
2. SQLAlchemy==1.3.3
3. swagger-ui-bundle==0.0.3
4. connexion==2.2.0
5. Flask==1.0.3