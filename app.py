from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, fields, marshal_with
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
db.create_all()
db.session.commit()

api = Api(app)
import models

resource_fields = {
    'first_name':   fields.String,
    'last_name':   fields.String
}


class UserList(Resource):
    @marshal_with(resource_fields)
    def get(self):
        users = db.session.query(models.User).all()
        print(db.session.query(models.User).all())
        return users


class UserDetail(Resource):
    @marshal_with(resource_fields)
    def get(self, user_id):
        print('get')

    def post(self, user_id):
        print('post')

    def delete(self, user_id):
        print('delete')


api.add_resource(UserList, '/users')
api.add_resource(UserDetail, '/users/<user_id>')


if __name__ == '__main__':
    app.run()
