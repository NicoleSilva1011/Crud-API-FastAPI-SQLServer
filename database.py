import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import urllib
import os
from dotenv import load_dotenv

load_dotenv(".env")

server_name = os.environ.get("SERVER_NAME")
database_name = os.environ.get("DATABASE_NAME")
user = os.environ.get("UID")
password = os.environ.get("PWD")

connection_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"UID={user};"
    f"PWD={password};"
)

params = urllib.parse.quote_plus(connection_str)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

