# fastapi-url-shortener
A high-performance URL shortening service built with Python (FastAPI) and MySQL. This application converts long URLs into manageable short codes, handles efficient HTTP redirects, and tracks detailed usage analytics.
# API Documentation
For a detailed look at request parameters, headers, and example responses, please visit our live Postman documentation:

https://documenter.getpostman.com/view/48093396/2sB3dVPTnf
# Technical Stack
Backend: Python 3.12+ (FastAPI)

Database: MySQL

ORM: SQLAlchemy

Testing/Docs: Postman & Swagger UI

# Project Structure
```bash
url_shortener/
├── main.py            # API Routes and core business logic
├── models.py          # SQLAlchemy database models
├── database.py        # MySQL connection configuration
├── requirements.txt   # Python dependencies
├── .gitignore         # Files to ignore in Git
└── url_shortener.postman_collection.json # Local Postman collection
```
# Setup & Installation
1. Database Initialization
Login to your MySQL CMD and run the following script:
```bash
CREATE DATABASE url_db;
USE url_db;

CREATE TABLE urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original_url TEXT NOT NULL,
    short_code VARCHAR(10) UNIQUE NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX (short_code)
);

CREATE TABLE clicks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url_id INT,
    click_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(45),
    user_agent TEXT,
    FOREIGN KEY (url_id) REFERENCES urls(id) ON DELETE CASCADE
);
```
2. Environment Setup
```bash
# Navigate to directory
cd D:\url_shortener

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```


