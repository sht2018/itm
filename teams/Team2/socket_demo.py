import select, socket

UDP_IP = "10.20.80.38"
UDP_PORT = 5000

recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recv_socket.bind((UDP_IP, UDP_PORT))

while True:
    InReady, _, _ = select.select([recv_socket], [], [], 2.0)
    if InReady == []:
        print("Timeout")
        break
    recPacket, addr = recv_socket.recvfrom(1024)
    for p in recPacket:
        print("Person:", p)
        break
recv_socket.close()
