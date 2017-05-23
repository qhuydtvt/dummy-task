from flask import Flask
from mlab import connect
from flask_restful import Resource, Api, reqparse
from user import User

app = Flask(__name__)
api = Api(app)
connect()

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, help="Username")
parser.add_argument("password", type=str, help="Password")

class Register(Resource):
    def post(self):
        args = parser.parse_args()
        username = args["username"]
        password = args["password"]
        found_user = User.objects(username=username).first()
        if found_user is not None:
            return {
                "code": 0,
                "message": "User already exists"
            }
        else:
            user = User(username=username, password=password)
            user.save()
            return {
                "code": 1,
                "message": "Registered"
            }

class Login(Resource):
    def post(self):
        args = parser.parse_args()
        username = args["username"]
        password = args["password"]
        found_user = User.objects(username=username).first()
        if found_user is not None and found_user.password == password:
            return {
                "code": 1,
                "message": "Logged in"
            }
        else:
            return {
                "code": 0,
                "message": "Login failed"
            }

api.add_resource(Register, "/register")
api.add_resource(Login, "/login")

if __name__ == '__main__':
    app.run(port=9696)
