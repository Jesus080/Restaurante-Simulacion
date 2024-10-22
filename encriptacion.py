from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Función para rellenar el texto a un múltiplo de 16 bytes
def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

# Encriptar el mensaje
def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_ECB)  # Usamos el modo ECB
    padded_message = pad(message)
    encrypted_bytes = cipher.encrypt(padded_message.encode('utf-8'))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

# Desencriptar el mensaje
def decrypt_message(key, encrypted_message):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded_encrypted_message = base64.b64decode(encrypted_message)
    decrypted_bytes = cipher.decrypt(decoded_encrypted_message)
    return decrypted_bytes.decode('utf-8').strip()

# Generar una clave de 16 bytes
key = get_random_bytes(16)

# Mensaje a encriptar
message = "Este es un mensaje secreto"

# Encriptar el mensaje
encrypted_message = encrypt_message(key, message)
print(f"Mensaje encriptado: {encrypted_message}")

# Desencriptar el mensaje
decrypted_message = decrypt_message(key, encrypted_message)
print(f"Mensaje desencriptado: {decrypted_message}")
