import socket

class rocksocket:
    def __init__(self, ip, port, server, Format="utf-8") -> None:
        self.Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.IP = ip
        self.PORT = port
        if server == True:
            server.bind((ip,port))

        
    def send_message(conn, Message, HEADER, FORMAT):
        conn.send(len(Message))
        conn.send(str(Message).encode(FORMAT) + b' ' * (HEADER - len(Message.encode(FORMAT))))
    def receive_message(conn, HEADER, FORMAT):
        Len_message = int(conn.recv(HEADER).decode(FORMAT))
        return conn.recv(Len_message)