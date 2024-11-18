from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, User

app = Flask(__name__)
# applies CORS headers to all routes, enabling resources to be accessed
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

db = SQLAlchemy(app)
api = Api(app)


class PollutionHistory(Resource):
    def get(self):
        return {'pollution': 'No data available'}
    

api.add_resource(PollutionHistory, '/pollution-hisotry', '/pollution-history')


if __name__=='__main__':
    app.run(port=5555, debug=True)