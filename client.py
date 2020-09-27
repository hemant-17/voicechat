import socket
import pyaudio
import wave
from Crypto.Cipher import AES
import random
import string

#keys
AES_KEY = 'KP877IxMZSq25zTDEyy8NDbSFQ8Uiljm'
AES_IV = 'rxugdew3oOhNj5RH'

#record
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 40

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("*recording")

frames = []

for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
 data  = stream.read(CHUNK)
 encryptor = AES.new(AES_KEY.encode("utf-8"), AES.MODE_CFB, AES_IV.encode("utf-8"))
 data = encryptor.encrypt(data)
 frames.append(data)
 s.sendall(data)

print("*done recording")

stream.stop_stream()
stream.close()
p.terminate()
s.close()

print("*closed")

# encryptor = AES.new(AES_KEY.encode("utf-8"), AES.MODE_CFB, AES_IV.encode("utf-8"))
# encrypted_audio = encryptor.encrypt(contents)