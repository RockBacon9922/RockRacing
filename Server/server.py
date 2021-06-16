from communication import send_message
import socket
from .. import communication

server = socket.socket()

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
print(ADDR)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"




