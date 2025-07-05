# relay_to_kafka.py

from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # tai sinun Kafka-serverisi
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_to_kafka(signal: dict, topic: str):
    producer.send(topic, value=signal)
    producer.flush()
    print(f"[INFO] Signal sent to Kafka topic '{topic}'")
