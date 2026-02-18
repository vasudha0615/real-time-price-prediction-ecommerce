# Real-Time Price Prediction for E-Commerce

## 📌 Overview
This project demonstrates an end-to-end real-time price prediction system for an e-commerce use case.  
It streams live order data using Apache Kafka, predicts prices using Machine Learning, stores results in Snowflake, and visualizes insights using Power BI.

---

## 🚀 Key Highlights
- Real-time data streaming with Apache Kafka  
- Machine Learning–based price prediction  
- Cloud data warehousing using Snowflake  
- Interactive dashboards using Power BI  
- Complete industry-style data pipeline  

---

## 🏗️ System Architecture
Kafka Producer → ML Prediction Engine → Snowflake → Power BI

---

## 🧰 Tech Stack
- Python  
- Apache Kafka  
- Scikit-learn  
- Snowflake  
- Power BI  

---

## 🔄 Project Workflow
1. Kafka Producer simulates live e-commerce order data  
2. ML Prediction Engine processes streaming data and predicts prices  
3. Prediction results are stored in Snowflake  
4. Power BI visualizes monthly and yearly price trends  

---

## ▶️ How to Run the Project

### Install Dependencies
pip install -r requirements.txt

### Start Kafka
zookeeper-server-start.bat config/zookeeper.properties  
kafka-server-start.bat config/server.properties  

### Run Kafka Producer
python producer.py

### Run ML Prediction Consumer
python predict.py

---

## 🗄️ Snowflake
Snowflake is used to store prediction results in a cloud data warehouse.  
SQL scripts are included to create databases, tables, and load data using COPY INTO.

---

## 🎯 Use Case
This project showcases real-time analytics, machine learning integration, and cloud data engineering skills relevant to Data Engineer and AI/ML Engineer roles.

---

## 👩‍💻 Author
Vasudha Tulla  
B.Tech CSE (AI & ML)
