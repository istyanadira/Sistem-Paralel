import socket

# Konfigurasi Server
HOST = '127.0.0.1'  # Alamat IP standar localhost
PORT = 65432        # Port yang akan digunakan

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # *** PENTING: Mengatasi WinError 10048 (Address already in use) ***
    # Opsi ini memungkinkan server untuk menggunakan kembali alamat port
    # yang mungkin masih dalam kondisi TIME_WAIT setelah penutupan sebelumnya.
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        # Mengikat socket ke alamat dan port
        s.bind((HOST, PORT))
        # Mendengarkan koneksi masuk (max 1 koneksi antrian)
        s.listen()
        print(f"[*] Server mendengarkan di {HOST}:{PORT}")

        # Menerima koneksi dari client
        conn, addr = s.accept()
        with conn:
            print(f"[*] Terhubung dengan {addr}")
            
            # Menerima data dari client (maksimal 1024 bytes)
            data = conn.recv(1024)
            
            if data:
                pesan_client = data.decode('utf-8')
                print(f"[<] Pesan diterima dari client: {pesan_client}")
                
                # Membuat pesan balasan
                balasan = "Pesan Anda telah diterima dan dikonfirmasi oleh server!"
                
                # Mengirim balasan ke client
                conn.sendall(balasan.encode('utf-8'))
                print("[>] Balasan konfirmasi dikirim ke client.")
            
    except Exception as e:
        print(f"[!] Terjadi kesalahan pada server: {e}")