from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class PollutionHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    air_quality_index = db.Column(db.Integer)
    water_quality_index = db.Column(db.Integer)
    ph_level = db.Column(db.Float)
    temperature = db.Column(db.Float)

    def __repr__(self):
        return f'<id {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'air_quality_index': self.air_quality_index,
            'water_quality_index': self.water_quality_index,
            'ph_level': self.ph_level,
            'temperature': self.temperature,
            
        }