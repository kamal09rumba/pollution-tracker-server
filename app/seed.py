from faker import Faker
from app import app
from models import db, PollutionHistory

fake = Faker()
with app.app_context():
    print("Starting seed...")
    PollutionHistory.query.delete()
    new_pollution_datum = []
    for _ in range(20):
        date = fake.date_time()
        air_quality_index = fake.random_int(min=0, max=500)
        water_quality_index = fake.random_int(min=0, max=100)
        ph_level = fake.pyfloat(min_value=0, max_value=14)
        temperature = fake.pyfloat(min_value=-5, max_value=45)
        new_pollution_data = PollutionHistory(
            date=date,
            air_quality_index=air_quality_index,
            water_quality_index=water_quality_index,
            ph_level=ph_level,
            temperature=temperature
        )
        new_pollution_datum.append(new_pollution_data)
    db.session.add_all(new_pollution_datum)
    db.session.commit()
    print("Successfully seeded")