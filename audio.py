import AES
import random
import string

AES_KEY = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(32))

AES_IV = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))

input_file = 'audio.wav'

encrypted_audio_file = '(encrypted)' + input_file

decrypted_audio_file = '(decrypted)' + input_file

with open(input_file, 'rb') as fd:
    contents = fd.read()

encryptor = AES.new(AES_KEY.encode("utf-8"), AES.MODE_CFB, AES_IV.encode("utf-8"))
encrypted_audio = encryptor.encrypt(contents)

with open(encrypted_audio_file, 'wb') as fd:
    fd.write(encrypted_audio)

decryptor = AES.new(AES_KEY.encode("utf-8"), AES.MODE_CFB, AES_IV.encode("utf-8"))
decrypted_audio = decryptor.decrypt(encrypted_audio)

with open(decrypted_audio_file, 'wb') as fd:
    fd.write(decrypted_audio)