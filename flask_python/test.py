from flask import flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, name):
        return {'student': name}

api.add_resource(Student, '/student/<string:name>')
api.add_resource(Student, '/dob/<string:name>')
api.add_resource(Student, '/student/<string:name>/classes/<string:name>'')

app.run(port=50000)
