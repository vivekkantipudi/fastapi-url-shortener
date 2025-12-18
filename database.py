from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Change 'root' and 'password' to your MySQL credentials
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:ViveK%402005@localhost/url_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()