import mysql.connector
from mysql.connector import Error
import streamlit as st
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def register_user(name, email, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                       (name, email, password))
        conn.commit()
        return True
    except mysql.connector.IntegrityError:
        st.error("Registration failed: User already exists.")
        return False
    except mysql.connector.Error as e:
        st.error(f"Registration failed: {e}")
        return False
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


def login_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def delete_user(email):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE email = %s", (email,))
        conn.commit()
        return True
    except mysql.connector.Error as e:
        st.error(f"Failed to delete user: {e}")
        return False
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


# def insert_meal(meal_type, name, calories, protein, carbs, fat, fiber):
#     conn = get_connection()
#     cursor = conn.cursor()
#     # Note: your columns must match your table exactly: carbohydrate, total_fat (not 'carbs', 'fat')
#     query = f"""
#         INSERT INTO {meal_type} (name, calories, protein, carbohydrate, total_fat, fiber)
#         VALUES (%s, %s, %s, %s, %s, %s)
#     """
#     cursor.execute(query, (name, calories, protein, carbs, fat, fiber))
#     conn.commit()
#     cursor.close()
#     conn.close()
