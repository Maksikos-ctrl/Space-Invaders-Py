import socket
import json

SERVER_ADDRESS = ('localhost', 5000)

def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(SERVER_ADDRESS)
        s.sendall(json.dumps(data).encode())
        response = s.recv(1024).decode()
    return json.loads(response)

def add_client(nickname):
    data = {'action': 'add_client', 'nickname': nickname}
    return send_data(data)

def save_result(nickname, max_level):
    data = {'action': 'save_result', 'nickname': nickname, 'max_level': max_level}
    return send_data(data)