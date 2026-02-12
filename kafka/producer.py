from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime, timedelta

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
)

topic_name = "price-data"
print("Kafka Producer started...")

while True:
    past_days = random.randint(1, 90)
    event_time = datetime.now() - timedelta(days=past_days)

    data = {
        "quantity": round(random.uniform(1, 10), 2),
        "customer_id":random.randint(1000, 1010),
        "predicted_at": event_time
    }

    producer.send(topic_name, value=data)
    print("Sent:", data)

    time.sleep(5)
