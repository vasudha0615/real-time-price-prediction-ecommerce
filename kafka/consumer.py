from kafka import KafkaConsumer
import json
import csv
import os

consumer = KafkaConsumer(
    'price-data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='price_consumer_v1',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

os.makedirs('../data', exist_ok=True)
filepath = '../data/streaming_data.csv'

file_exists = os.path.isfile(filepath)

print("Kafka Consumer started... Saving data to CSV")

file = open(filepath, mode='a', newline="")
writer = csv.writer(file)

if not file_exists:
    writer.writerow(['product_id', 'price', 'timestamp'])
    file.flush()

try:
    for message in consumer:
        data = message.value

        writer.writerow([
            data['product_id'],
            data['price'],
            data['timestamp']
        ])
        file.flush()

        print("Saved:", data)

except KeyboardInterrupt:
    print("Stopping consumer...")

finally:
    file.close()
