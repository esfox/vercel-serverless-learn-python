import os
from dotenv import load_dotenv
from estoult import *
# import psycopg2

load_dotenv()

connection = PostgreSQLDatabase(
    host=os.getenv('DB_HOST', ''),
    database=os.getenv('DB_NAME', ''),
    user=os.getenv('DB_USER', ''),
    password=os.getenv('DB_PASSWORD', '')
)

# def db_connect():
#     return psycopg2.connect(
#         host='host',
#         dbname='dbname',
#         user='user',
#         password='password'
#     )
