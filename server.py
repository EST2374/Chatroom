import socket
import threading
import sqlite3
import os
import hashlib

host = '127.0.0.1'
port = 9001

DB_Name = 'user_data.db'

def init_db():
    conn = sqlite3.connect(DB_Name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            key TEXT,
            level INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def auth_or_reg(username, key):
    hashed_key = hashlib.sha256(key.encode()).hexdigest()
    
    conn = sqlite3.connect(DB_Name)
    cursor = conn.cursor()

    cursor.execute('SELECT key FROM users WHERE username = ?',(username,))
    user_data = cursor.fetchone()

    if user_data:
        db_hashed_key = user_data[0]
        input_hashed_key = hashlib.sha256(key.encode()).hexdigest()
        if db_hashed_key == input_hashed_key:
            conn.close()
            return True
        else:
            conn.close()
            return False
    else:
        try:
            cursor.execute(
                'INSERT INTO users (username, key, level) VALUES (?, ?, ?)',
                (username, hashed_key, 0)
            )
            conn.commit()
            print(f"***New User registered: {username}***")
            conn.close()
            return True
        except sqlite3.IntegrityError:
            print(f"Error with registration from user: {username}")
            return False

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname =  nicknames[index]
            broadcast(f"{nickname} left the chat!".encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    init_db()

    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        try:
            client.send('USER'.encode('ascii'))
            username = client.recv(1024).decode('ascii')
        
            client.send('KEY'.encode('ascii'))
            key = client.recv(1024).decode('ascii')

            if auth_or_reg(username, key):
                nickname = username
                nicknames.append(nickname)
                clients.append(client)
                print(f"Authentication successful for {nickname}")

                client.send("SUCCESS".encode('ascii'))
                client.send(f"Connected to the Server as {nickname}".encode('ascii'))

                broadcast(f"\n{nickname} joined the chat".encode('ascii'))
                thread = threading.Thread(target=handle, args=(client,))
                thread.start()
            else:
                print(f"Authentication failed for {username}")
                client.send("FAIL".encode('ascii'))
                client.close()
        except Exception as e:
            print(f"Error during login process: {e}")
            client.close()
        
print("Server is listening...")
receive()