# Cloud-Native Portfolio Automation Engine

An automated financial backend system designed to track a diversified multi-asset portfolio (Equities and ETFs) in real-time. This project replaces manual market monitoring with a 24/7 autonomous ingestion pipeline, logging market "heartbeats" directly to a cloud-hosted NoSQL infrastructure.

---

## Execution

![Portfolio Automation Execution](./Output.png)

---

## Key Features
- Automated Data Ingestion: Periodically fetches real-time market prices for assets like Vedanta (VEDL.NS), Silver BeES (SILVERBEES.NS), etc using the yfinance API.
- Cloud Integration: Managed NoSQL data storage using MongoDB Atlas for persistent historical logging.
- Operational Reliability: Built-in logging and error-handling to ensure system stability and data integrity.
- Secure Credential Management: Uses environment variables (.env) to keep sensitive cloud connection strings secure.

---

## System Architecture
```bash
Data Flow: yfinance API (Market Data) → Python Engine (Processing & Logic) → MongoDB Atlas (Cloud Storage)
```

---

## Tech Stack
| Layer | Technology |
| :--- | :--- |
| **Language** | Python 3.9+ |
| **Data Ingestion** | yfinance API |
| **Database** | MongoDB Atlas (Cloud NoSQL) |
| **Security** | python-dotenv |
| **Infrastructure** | MongoDB Cloud & Git |

---

## Repository Structure

```
portfolio-automation/
├── src/
│   ├── automation.py    # Main monitoring logic
│   └── database.py      # MongoDB connection and CRUD operations
├── .env                 # (Ignored) Sensitive credentials
├── .gitignore           # File/folder exclusion rules
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## Setup & Installation

To run this project locally, follow these steps:
1. Clone the Repository
```bash
git clone https://github.com/Vedant804/portfolio-automation.git
cd portfolio-automation
```
2. Set up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Configuration Create a .env file in the root directory and add your MongoDB URI:
```bash
MONGO_URI=mongodb+srv://your_username:your_password@cluster.mongodb.net/
DB_NAME=IWealthProject
```
5. Run the Script
```bash
python src/automation.py
```
