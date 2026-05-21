import mysql.connector
import streamlit as st

conn = mysql.connector.connect(
    host=st.secrets["Host_Name"],
    user=st.secrets["user"],
    password=st.secrets["password"],
    database=st.secrets["database"],
    port=st.secrets["port"]
)

cursor = conn.cursor()

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id int PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
)
""")

# FILES TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS files(
    id int PRIMARY KEY,
    user_id INT,
    file_name VARCHAR(255),
    file_type VARCHAR(100),
    file_url TEXT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
""")

conn.commit()

print("Tables Created Successfully")

#pip install streamlit mysql-connector-python

