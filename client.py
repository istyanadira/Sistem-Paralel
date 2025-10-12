import socket

# Konfigurasi Server (Harus sama dengan di server.py)
HOST = '127.0.0.1'  
PORT = 65432        

# Pesan yang akan dikirim ke server
PESAN_KIRIM = "Halo Server! Saya berhasil terhubung dan ini pesan saya."

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # Mencoba terhubung ke server
        s.connect((HOST, PORT))
        print(f"[*] Terhubung ke server di {HOST}:{PORT}")
        
        # Mengirimkan pesan ke server
        s.sendall(PESAN_KIRIM.encode('utf-8'))
        print(f"[>] Pesan dikirim: {PESAN_KIRIM}")
        
        # Menerima balasan dari server
        data = s.recv(1024)
        balasan_server = data.decode('utf-8')
        print(f"[<] Balasan diterima dari server: {balasan_server}")
        
    except ConnectionRefusedError:
        print("[!] Gagal terhubung: Pastikan program server sedang berjalan.")
    except Exception as e:
        print(f"[!] Terjadi kesalahan: {e}")