# fastapi-url-shortener
A high-performance URL shortening service built with Python (FastAPI) and MySQL. This application converts long URLs into manageable short codes, handles efficient HTTP redirects, and tracks detailed usage analytics.
# API Documentation
For a detailed look at request parameters, headers, and example responses, please visit our live Postman documentation:

https://documenter.getpostman.com/view/48093396/2sB3dVPTnf
#Technical Stack
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

