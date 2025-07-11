import socket

def start_receiver(host='localhost', port=5000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Receiver server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    with open('data/received_train.csv', 'wb') as f:
        print("Receiving data...")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    print("Data received successfully.")
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_receiver()