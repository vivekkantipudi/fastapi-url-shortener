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
venv\Scrpts\activate
```
3. Run the Application
```bash
uvicorn main:app --reload
```
The server will start at http://127.0.0.1:8000.
# Short Code Generation Strategy
This system uses Base62 Encoding based on the Database Auto-Increment ID
Unique Mapping: Each long URL is assigned a unique integer ID by MySQL.
Encoding: That ID is converted into a string using a character set of [0-9][a-z][A-Z].
Collision Handling: Because every database ID is unique, code collisions are mathematically impossible. No secondary "check-if-exists" loop is required.

# Testing Order
POST /api/shorten: Create a short code for a long URL.

GET /{short_code}: Visit the code in your browser to trigger a redirect.

GET /api/stats/{short_code}: Verify the click was recorded in the analytics.



