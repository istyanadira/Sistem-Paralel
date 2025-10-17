import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

nickname = input("Masukkan nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
except:
    print("Tidak dapat terhubung ke server.")
    exit()

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Koneksi terputus dari server.")
            client.close()
            break

def write():
    while True:
        try:
            message = f'{nickname}: {input("")}'
            client.send(message.encode('utf-8'))
        except:
            print("Gagal mengirim pesan.")
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()