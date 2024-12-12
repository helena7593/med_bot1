import sqlite3

DB_NAME = "clinic.db"

def initialize_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_name TEXT NOT NULL,
            time TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_appointment(doctor_name, time, first_name, last_name, phone):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO appointments (doctor_name, time, first_name, last_name, phone)
        VALUES (:doctor_name, :time, :first_name, :last_name, :phone)
    ''', {
        'doctor_name': doctor_name,
        'time': time,
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone
    })
    conn.commit()
    conn.close()
