# Cloud-Native Portfolio Automation Engine
An automated financial backend system designed to track a diversified multi-asset portfolio (Equities and ETFs) in real-time. This project replaces manual market monitoring with a 24/7 autonomous ingestion pipeline, logging market "heartbeats" directly to a cloud-hosted NoSQL infrastructure.

## Key Features
- Automated Data Ingestion: Periodically fetches real-time market prices for assets like Vedanta (VEDL.NS) and Silver BeES (SILVERBEES.NS) using the yfinance API.
- Cloud Integration: Managed NoSQL data storage using MongoDB Atlas for persistent historical logging.
- Operational Reliability: Built-in logging and error-handling to ensure system stability and data integrity.
- Secure Credential Management: Uses environment variables (.env) to keep sensitive cloud connection strings secure.

## Tech Stack
-Language: Python 3.9+
-Database: MongoDB Atlas (Cloud NoSQL)
-Libraries: yfinance, pymongo, python-dotenv, pandas
-Tools: Git, VS Code, MongoDB Compass

## Repository Structure
portfolio-automation/
├── src/
│   ├── automation.py    # Main monitoring logic
│   └── database.py      # MongoDB connection and CRUD operations
├── .env                 # (Ignored) Sensitive credentials
├── .gitignore           # File/folder exclusion rules
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

##Setup & Installation
To run this project locally, follow these steps:
Clone the Repository

git clone https://github.com/Vedant804/portfolio-automation.git
cd portfolio-automation

Set up Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Configuration Create a .env file in the root directory and add your MongoDB URI:

MONGO_URI=mongodb+srv://your_username:your_password@cluster.mongodb.net/
DB_NAME=IWealthProject

Run the Script

python src/automation.py
