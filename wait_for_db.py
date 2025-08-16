import socket
import sys
import time
import os

DB_HOST = os.environ.get('DB_HOST', 'db')
DB_PORT = int(os.environ.get('DB_PORT', 3306))

print("Waiting for database connection...")
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((DB_HOST, DB_PORT))
        print("Database connection successful!")
        sock.close()
        break
    except socket.error:
        print("MySQL is unavailable - waiting")
        time.sleep(1)