import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="Employee_Payroll"
)

cursor = con.cursor()