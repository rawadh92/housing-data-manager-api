from confluent_kafka import Consumer, KafkaException
import requests
import json
import os

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "broker:29092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "housing_topic")
API_ENDPOINT = os.getenv("API_ENDPOINT", "http://housing_api:8000/houses")

consumer_conf = {
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'housing_group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_conf)
consumer.subscribe([KAFKA_TOPIC])

print("[Consumer] En attente des messages sur le topic...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        
        data = json.loads(msg.value().decode('utf-8'))
        response = requests.post(API_ENDPOINT, json=data)
        print(f"[Consumer] Message consommé et envoyé, réponse: {response.status_code}, {response.json()}")

except KeyboardInterrupt:
    print("[Consumer] Arrêt du consumer...")
finally:
    consumer.close()