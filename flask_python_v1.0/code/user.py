import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod #making it a method of the class
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        #always have to be a tuple thats why (username,)
        result = cursor.execute(query, (username,))
        row = result.fetchone()  #gets the first row, unless no row then None
        if row:
            #cls is reference to the @classmethod
            user = cls(*row)  #args and kwargs
        else:
            user = None

        connection.close()
        return user

    @classmethod #making it a method of the class
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        #always have to be a tuple thats why (username,)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()  #gets the first row, unless no row then None
        if row:
            #cls is reference to the @classmethod
            user = cls(*row)  #args and kwargs
        else:
            user = None

        connection.close()
        return user

        #either returns a user object or None
class UserRegister(Resource):
    #parser for data
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    #POST request
    def post(self):
        #connect to db
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        #Defining data from parser
        data = UserRegister.parser.parse_args()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"

        #data is from parser
        cursor.execute(query, (data['username'], data['password'])) #must be a tuple

        connection.commit()

        connection.close()

        return {"message": "User has been created successfully."}
