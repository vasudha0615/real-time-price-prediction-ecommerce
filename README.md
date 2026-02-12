# Cloud-Based Real-Time Price Prediction for E-Commerce

## 📌 Project Overview
This project implements an end-to-end real-time price prediction pipeline for an e-commerce use case.  
It uses **Apache Kafka** for streaming data, **Machine Learning** for price prediction, **Snowflake** as a cloud data warehouse, and **Power BI** for visualization.

---

## 🏗️ System Architecture
Kafka Producer → ML Prediction Engine → Snowflake → Power BI

---

## 🧰 Tech Stack
- **Programming Language:** Python  
- **Streaming:** Apache Kafka  
- **Machine Learning:** Scikit-learn  
- **Cloud Data Warehouse:** Snowflake  
- **Visualization:** Power BI  

---

## 🔄 Project Workflow

### 1️⃣ Kafka Producer
- Simulates real-time order data
- Publishes quantity and customer information to Kafka topics

### 2️⃣ Machine Learning Prediction
- Consumes streaming data from Kafka
- Uses a trained ML model to predict product prices
- Prepares prediction results for storage

### 3️⃣ Snowflake Integration
- Prediction results are loaded into **Snowflake**
- SQL scripts create database, schema, tables, and stages
- Data is queried directly from Snowflake

### 4️⃣ Power BI Dashboard
- Power BI connects to Snowflake
- Visualizes predicted prices and trends over time

---

## 🗄️ Snowflake Usage
Snowflake is used as the cloud data warehouse for storing prediction results.

Key features used:
- Database and schema creation
- Staging files
- `COPY INTO` command for data loading

## ▶️ How to Run the Project

### Prerequisites
- Python 3.8+
- Apache Kafka running locally
- Snowflake account
- SnowSQL (optional)
- Power BI Desktop



