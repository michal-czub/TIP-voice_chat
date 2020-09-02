import socket
import threading
import time


class Server:
    def __init__(self):
        self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 5050
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ADDR = (self.IP, self.PORT)
        self.HEADER = 64
        self.FORMAT = 'utf-8'
        self.CONNECTIONS = []
        self.LOGGED = []
        log_confirm = "Logged in!"
        self.LOGIN_CONFIRMATION = log_confirm.encode("utf-8")
        log_error = "Wrong login or password!"
        self.LOGIN_ERROR = log_error.encode("utf-8")
        self.logged = False
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
            # login = conn.recv(1024)
            # login_decoded = login.decode("utf-8")
            # password = conn.recv(1024)
            # password_decoded = password.decode("utf-8")
            # if login_decoded == "test":
            #     self.LOGGED.append(conn)
            #     self.logged = True
            #     break
            # else:
            #     pass

            # while self.logged:
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
