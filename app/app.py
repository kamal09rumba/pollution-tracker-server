import json
import os

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv

from models import db, PollutionHistory

load_dotenv()

app = Flask(__name__)
# applies CORS headers to all routes, enabling resources to be accessed
CORS(app)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

with open('app/fixtures/weather.json', encoding="utf-8") as json_file:
    weather_data = json.load(json_file)

class PollutionHistories(Resource):
    def get(self):
        latest_pollution = PollutionHistory.query.order_by().first()
        pollution_history = PollutionHistory.query.all()
        return {
            'sensor_data': latest_pollution.to_dict(),
            'pollution_history_data': [pollution.to_dict() for pollution in pollution_history],
            'weather_data': weather_data
        }, 200
    

api.add_resource(PollutionHistories, '/pollution-hisotry', '/pollution-history')


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)
