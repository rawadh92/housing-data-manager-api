from confluent_kafka import Producer
import json
import os

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "broker:29092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "housing_topic")

producer_conf = {'bootstrap.servers': KAFKA_BROKER}
producer = Producer(producer_conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"[Producer] Erreur lors de l'envoi: {err}")
    else:
        print(f"[Producer] Message envoyé sur {msg.topic()} [Partition {msg.partition()}]")

data = {
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41,
    "total_rooms": 880,
    "total_bedrooms": 129,
    "population": 322,
    "households": 126,
    "median_income": 8.3252,
    "median_house_value": 452600.0,
    "ocean_proximity": "NEAR BAY"
}

producer.produce(KAFKA_TOPIC, key="house", value=json.dumps(data), callback=delivery_report)
producer.flush()
print("[Producer] Message envoyé avec succès !")