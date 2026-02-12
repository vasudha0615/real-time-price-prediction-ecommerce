from kafka import KafkaConsumer
import json
import pandas as pd
import joblib
import csv
import os

# Load trained model
model = joblib.load("../model/price_model.pkl")

# CSV output
OUTPUT_FILE = "../data/predictions.csv"
os.makedirs("../data", exist_ok=True)

file_exists = os.path.isfile(OUTPUT_FILE)

csv_file = open(OUTPUT_FILE, mode="a", newline="")
writer = csv.writer(csv_file)

if not file_exists:
    writer.writerow([
        "quantity",
        "customer_id",
        "predicted_price",
        "predicted_at"
    ])

# Kafka Consumer
consumer = KafkaConsumer(
    "price-data",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="latest",
    enable_auto_commit=True
)

print("Kafka Predictor started...")

for message in consumer:
    msg = message.value

    predicted_at = pd.to_datetime(msg["predicted_at"])

    # 🔑 FEATURES MUST MATCH MODEL TRAINING
    df = pd.DataFrame([{
        "Quantity": msg["quantity"],
        "CustomerID": msg["customer_id"],
        "year": predicted_at.year,
        "month": predicted_at.month
    }])

    predicted_price = round(model.predict(df)[0], 2)

    writer.writerow([
        msg["quantity"],
        msg["customer_id"],
        predicted_price,
        predicted_at
    ])

    csv_file.flush()
    print("Predicted & saved:", predicted_price)
