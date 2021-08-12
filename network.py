import socket, json

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.81"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.client.connect(self.addr)

    def send(self, data):
        try:
            self.client.send(json.dumps(data))
        except socket.error as e:
            print('Send error', e)
    
    def receive(self):
        try:
            return json.loads(self.client.recv(4096))
        except socket.error as e:
            print('Receive error', e)
