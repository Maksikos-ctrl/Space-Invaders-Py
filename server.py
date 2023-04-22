import socket
import threading
import json

HOST = 'localhost'
PORT = 5000

clients = {}
results_file = 'results.txt'

def handle_client(conn, addr):
    while 1:
        data = conn.recv(1024).decode()
        if not data:
            break
        data = json.loads(data)
        if data['action'] == 'add_client':
            clients[data['nickname']] = conn
            conn.sendall(json.dumps({'status': 'ok'}).encode())
        elif data['action'] == 'save_result':
            with open(results_file, 'a') as f:
                f.write(f"{data['nickname']} {data['max_level']}\n")
            conn.sendall(json.dumps({'status': 'ok'}).encode())
        else:
            conn.sendall(json.dumps({'status': 'error', 'message': 'Invalid action'}).encode())
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == '__main__':
    start_server()
    