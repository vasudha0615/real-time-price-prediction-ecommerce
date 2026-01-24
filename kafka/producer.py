from kafka import KafkaProducer
import json
import time
import random

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = "price-data"

print("Kafka Producer started...")

while True:
    data = {
        "product_id": random.randint(1000, 1010),
        "price": round(random.uniform(200, 1500), 2),
        "timestamp": time.time()
    }

    producer.send(topic_name, value=data)
    print("Sent:", data)

    time.sleep(5)


