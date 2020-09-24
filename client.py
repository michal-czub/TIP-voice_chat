import socket
import threading
import pyaudio


class Client:
    def __init__(self):
        self.IP = "192.168.0.12"
        #self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 5050
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ADDR = (self.IP, self.PORT)
        self.FORMAT = 'utf-8'
        self.HEADER = 64

    def connect(self):
        print("DUPA connect")
        try:
            self.SOCKET.connect(self.ADDR)
        except Exception as err:
            print(err)
            print(f"[CAN'T CONNECT TO]: {self.ADDR}")

        CHUNK = 1024
        RATE = 44100
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        self.py_aud = pyaudio.PyAudio()
        self.check_config()
        self.inputStream = self.py_aud.open(format=FORMAT, rate=RATE, frames_per_buffer=CHUNK,
                                            channels=CHANNELS, input=True)
        self.outputStream = self.py_aud.open(format=FORMAT, rate=RATE,
                                             frames_per_buffer=CHUNK,
                                             channels=CHANNELS, output=True)
        thread = threading.Thread(target=self.receive)
        thread.start()

        self.send(CHUNK)

    def __str__(self):
        return "{}, {}, {}".format(self.IP, self.PORT, self.SOCKET)

    def check_config(self):
        devinfo = self.py_aud.get_device_info_by_index(0)
        if self.py_aud.is_format_supported(44100.0,
                                           input_device=devinfo['index'],
                                           input_channels=devinfo['maxInputChannels'],
                                           input_format=pyaudio.paInt16):
            print('works')

    def receive(self):

        while True:
            try:
                data = self.SOCKET.recv(1024)
                self.outputStream.write(data)
            except Exception as err:
                print(err)
                break

    def send(self, CHUNK):
        while True:
            try:
                data = self.inputStream.read(CHUNK)
                self.SOCKET.sendall(data)
            except Exception as err:
                print(err)
                break


# client = Client()
# print(client.__str__())
