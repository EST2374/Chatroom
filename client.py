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

    # TODO Password pflicht machen
    parser.add_argument(
        '-k', '--key',
        type=str,
        required=None,
        help="Your Password"
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
    
    if args.key is None:
        args.key = input("Password: ")

    return args

if __name__ == "__main__":
    args = parser()

    IP = args.ip
    Port = args.port
    nickname = args.user
    level = 0
    ranks = ["Noob", "King", "Chad"]
    rank=""
    msg_count = 0


    if not IP:
        print("Error. Server IP cannot be empty. Exiting")
        sys.exit(1)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((IP, int(Port)))
    print(f"Connected to {IP}:{Port}...")
except ConnectionRefusedError:
    print("Couldn't connect to the Server")
    os._exit(0)

while True:
    try: 
        msg = client.recv(1024).decode('ascii')

        if msg == 'USER':
            client.send(nickname.encode('ascii'))
        elif msg == 'KEY':
            client.send(args.key.encode('ascii'))
        elif msg == 'SUCCESS':
            welcome_msg = client.recv(1024).decode('ascii')
            print("Login successful")
            print(welcome_msg)
            break
        elif msg == 'FAIL':
            print("Login failed: Invalid Username or Key. Disconneting...")
            client.close()
            os._exit(0)
        else:
            print(msg)
            break
    except:
        print("Error occurred during login! Disconneting...")
        client.close()
        os._exit(0)

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

def rang(level):
    global rank
    if level >= 0 and level < 10:
        rank = ranks[0]
    if level >= 10 and level < 20:
        rank = ranks[1]
    if level >= 20:
        rank = ranks[2] 
    return rank

def write():
    global level
    global rank
    global msg_count
    while True:
        user_input = input("")
        if user_input.lower() == '.exit':
            print("Disconneting...")
            client.close()
            os._exit(0)
            break

        # TODO .help nicht sichtbar im Chat machen
        if user_input.lower() == '.help':
            print("Commands you can use:\n"\
            ".exit to Disconnet\n" \
            ".lvl to show level\n"\
            ".msgcount to see how many messages you have sent")

        if user_input.lower() == '.lvl':
            print(f"Dein Rank: {rang(level)}")

        if user_input.lower() == '.msgcount':
            print(f"Message Counter: {msg_count}")

        msg = f'{nickname}: {user_input}'
        try:
            client.send(msg.encode('ascii'))
            level += 1
            msg_count += 1
        except socket.error as e:
            print(f"Error sending message: {e}")
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()