import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from faker import Faker
from kafka import KafkaProducer

load_dotenv(dotenv_path=Path("/opt/app/.env"))

kafka_host = os.getenv("KAFKA_HOST")
kafka_topic = os.getenv("KAFKA_TOPIC_NAME")

fake = Faker()
EVENT_KEYS = ["click", "view", "add_to_cart", "purchase", "like"]

producer = KafkaProducer(
    bootstrap_servers=f"{kafka_host}:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

print(f"Producing fake events to topic '{kafka_topic}' on {kafka_host}:9092 ...")
try:
    while True:
        event = {
            "event": fake.random_element(EVENT_KEYS),
            "user_id": fake.random_int(min=1, max=1000),
            "value": fake.random_int(min=1, max=10),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        producer.send(kafka_topic, value=event)
        print(event)
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    producer.flush()
    producer.close()
