from kafka import KafkaConsumer
import json
import csv
import os

consumer = KafkaConsumer(
    'price-data',
    bootstrap_servers = 'localhost:9092',
    auto_offset_reset = 'earliest',
    value_deserializer = lambda x:json.loads(x.decode('utf-8'))
)

os.makedirs('../data',exist_ok = True)
filepath = '../data/streaming_data.csv'

file_exists = os.path.isfile(filepath)

with open(filepath,mode = 'a',newline = "") as file:
    writer = csv.writer(file)

if not file_exists:
    writer.writerow(['product_id','price','demand','timestamp'])

print(" Saving Kafka data to CSV...")

for message in consumer:
    data = message.value

writer.writerow([
            data['product_id'],
            data['price'],
            data['demand'],
            data['timestamp']
        ])

        
print("Saved:", data)

