import socket
import threading
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12222
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Сервер слушает на {host}:{port}")
chat_history = []
server_clients = []
def handle_client(client_socket, client_name):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"{client_name}: {message}")
        chat_history.append(f"{client_name}: {message}")
        for client in server_clients:
            if client != client_socket:
                try:
                    client.send(f"{client_name}: {message}".encode('utf-8'))
                except:
                    client.close()
                    server_clients.remove(client)
while True:
    client_socket, client_address = server_socket.accept()
    client_name = client_socket.recv(1024).decode('utf-8')
    print(f"{client_name} connected from {client_address}")
    server_clients.append(client_socket)
    for message in chat_history:
        client_socket.send(message.encode('utf-8'))
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_name))
    client_thread.start()
server_socket.close()
