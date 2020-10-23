import socket
import pyaudio
import wave
import time
from Crypto.Cipher import AES
import random
import string
import simpleaudio as sa


#keys
AES_KEY = 'KP877IxMZSq25zTDEyy8NDbSFQ8Uiljq'
AES_IV = 'rxugdew3oOhNj5RH'
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "server_output.wav"
WIDTH = 2
frames = []

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
data = conn.recv(1024)
if AES_KEY == 'KP877IxMZSq25zTDEyy8NDbSFQ8Uiljm':
    i=1
    while data != '':
        decryptor = AES.new(AES_KEY.encode("utf-8"), AES.MODE_CFB, AES_IV.encode("utf-8"))
        data = decryptor.decrypt(data)
        stream.write(data)
        data = conn.recv(1024)
        i=i+1
        frames.append(data)

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
else:
    filename = 'song.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

stream.stop_stream()
stream.close()
p.terminate()
conn.close()

# decryptor = AES.new(AES_KEY.encode("utf-8"), AES.MODE_CFB, AES_IV.encode("utf-8"))
# decrypted_audio = decryptor.decrypt(encrypted_audio)