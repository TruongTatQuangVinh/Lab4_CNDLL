import socket
import pandas as pd
import os

def send_data(file_path, host='localhost', port=5000):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the receiver server
        s.connect((host, port))
        
        # Read the CSV file
        if os.path.exists(file_path):
            data = pd.read_csv(file_path)
            # Convert DataFrame to CSV string
            csv_data = data.to_csv(index=False)
            # Send the data
            s.sendall(csv_data.encode('utf-8'))
            print("Data sent successfully.")
        else:
            print("File not found.")

if __name__ == "__main__":
    send_data('data/train.csv')