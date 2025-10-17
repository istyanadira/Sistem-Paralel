import socket
import threading

HOST = '127.0.0.1'  
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} telah keluar chat.".encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    print("Server sedang berjalan dan menunggu koneksi...")
    while True:
        client, address = server.accept()
        print(f"Terhubung dengan {address}")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname user: {nickname}")
        broadcast(f"{nickname} bergabung dalam chat!".encode('utf-8'))
        client.send("Kamu berhasil terhubung ke server!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()