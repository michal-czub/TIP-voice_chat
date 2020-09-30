import socket
import threading


class Server:
    def __init__(self):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 5050
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ADDR = (self.IP, self.PORT)
        self.HEADER = 64
        self.FORMAT = 'utf-8'
        self.CONNECTIONS = []
        try:
            print("Trying to bind...")
            self.SOCKET.bind(self.ADDR)
        except Exception as err:
            print(err)

        self.server_start()
        print(self.SOCKET)

    def send_to_logged_clients(self, conn, msg):
        for client in self.CONNECTIONS:
            if client is not self.SOCKET and client is not conn:
                try:
                    client.send(msg)
                except socket.error as err:
                    print(err)

    def handle_client(self, conn, addr):
        print(f"<<< NEW CONNECTION >>> {addr} connected.")
        while True:
            data = conn.recv(1024)
            self.send_to_logged_clients(conn, data)

    def server_start(self):
        self.SOCKET.listen()
        print(f"[LISTENING]: {self.IP}")
        print(f"[PORT]: {self.PORT}")

        while True:
            conn, addr = self.SOCKET.accept()
            self.CONNECTIONS.append(conn)
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")


print("<<< SERVER STARTING >>>")
server = Server()
