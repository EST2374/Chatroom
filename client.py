import socket
import threading
import os
import sys
import argparse

def parser():

    Default_port = 9001

    parser = argparse.ArgumentParser(
        description="Chat Client. Needs IP and Port"
    )

    parser.add_argument(
        '-i', '--ip',
        type=str,
        required=None,
        help="IP of the Server (127.0.0.1)" 
    )

    parser.add_argument(
        '-p', '--port',
        type=int,
        default=Default_port,
        help=f"Port of the Server. Defualt Port is {Default_port}"
    )

    parser.add_argument(
        '-u', '--user',
        type=str,
        default=None,
        help="Your Username/Nickname"
    )
    
    args = parser.parse_args()

    if args.ip is None:
        args.ip = input("Server IP: ")
    if args.port == Default_port and '-p' not in sys.argv and '--port' not in sys.argv:
        change_port = input(f"Use default Port {Default_port}? [Y/n]")
        if change_port.lower() == 'n':
          while True:
              try: 
                    new_port_str = input("Server Port: ")
                    args.port = int(new_port_str)
                    break
              except ValueError:
                    print("Invalid Port number. Please enter a number")
          
    if args.user is None:
        args.user = input("Choose a nickname: ")
    
    return args

if __name__ == "__main__":
    args = parser()

    IP = args.ip
    Port = args.port
    nickname = args.user

    if not IP:
        print("Error. Server IP cannot be empty. Exiting")
        sys.exit(1)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((IP, int(Port)))
    print(f"Connected to {IP}:{Port}...")
except ConnectionRefusedError:
    print("Couldn't connect to the Server")
    sys.exit(1)

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(msg)
        except:
            print("An error occured!")
            client.close()
            os._exit(0)
            break

def write():
    while True:
        user_input = input("")
        if user_input.lower() == '.exit':
            print("Disconneting...")
            client.close()
            os._exit(0)
            break

        msg = f'{nickname}: {user_input}'
        try:
            client.send(msg.encode('ascii'))
        except socket.error as e:
            print(f"Error sending message: {e}")
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()