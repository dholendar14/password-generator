from pbkdf2 import PBKDF2
from Crypto.Cipher import AES
from base64 import b64encode,b64decode
import master_password_hash_generator

'''replace **** in salt with "special word".
   The "salt" is used to encrypt and decrypt the password.
'''
salt = b"*****"
'''Use master_password_hash_generator and replace '****' with the hash'''
master_password_hash = "****"

def query_master_pwd():
    master_hash = master_password_hash_generator.master_password_gen()
    if master_hash == master_password_hash:
        return True


def encrypt_password(password_to_encrypt):
    key = PBKDF2(str(master_password_hash), salt).read(32)
    data_convert = str.encode(password_to_encrypt)
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data_convert)
    add_nonce = ciphertext + nonce
    encoded_ciphertext = b64encode(add_nonce).decode()
    return encoded_ciphertext


def decrypt_password(password_to_decrypt):
    if len(password_to_decrypt) % 4:
        password_to_decrypt += '=' * (4 - len(password_to_decrypt) % 4)
    convert = b64decode(password_to_decrypt)
    key = PBKDF2(str(master_password_hash), salt).read(32)
    nonce = convert[-16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(convert[:-16])
    return plaintext