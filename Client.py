import socket
import threading
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = '127.0.0.1'
server_port = 12222
client_socket.connect((server_host, server_port))
user_name = input("Введи свое имя: ")
client_socket.send(user_name.encode('utf-8'))
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')# набор дв формат
            print(message)
        except:
            print("Соединение разорвано. Нажмите Enter, чтобы выйти.")
            client_socket.close()
            break
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()
while True:
    message = input()
    if message.lower() == "exit":
        client_socket.close()
        break
    client_socket.send(message.encode('utf-8'))
receive_thread.join()#поток
