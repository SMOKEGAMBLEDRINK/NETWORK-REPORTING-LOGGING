import socket as skt

# Set up server to listen on UDP port 514
UDP_IP = "0.0.0.0"          # Listen on all network interfaces
UDP_PORT = 514              # Syslog Port
BUFFER_SIZE = 4096          # Buffer Size

# Create a socket
sock = skt.socket(skt.AF_INET, skt.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening for syslog messages on {UDP_IP}:{UDP_PORT}")

while True:
    # Receive syslog message
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"Received message from {addr}:{data.decode()}")