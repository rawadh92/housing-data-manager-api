from flask import Flask, request, jsonify
from database import db_session, init_db
from models import House

app = Flask(__name__)

@app.route('/houses', methods=['GET'])
def get_houses():
    houses = House.query.all()
    return jsonify([house.to_dict() for house in houses])

@app.route('/houses', methods=['POST'])
def add_house():
    data = request.get_json()
    new_house = House(
        longitude=data['longitude'],
        latitude=data['latitude'],
        housing_median_age=data['housing_median_age'],
        total_rooms=data['total_rooms'],
        total_bedrooms=data['total_bedrooms'],
        population=data['population'],
        households=data['households'],
        median_income=data['median_income'],
        median_house_value=data['median_house_value'],
        ocean_proximity=data['ocean_proximity']
    )
    db_session.add(new_house)
    db_session.commit()
    return jsonify(new_house.to_dict()), 201

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8000)