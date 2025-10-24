"""
    encryptors.py. a part of pyagt library
"""
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256
from Cryptodome import Random


def data_encrypt(data, key):
    """
        encrypt data
        args:
            data(bytes[str])
            key(str)
    """

    try:
        key = key.encode("utf-8")
        data = data.encode("utf-8")
    except AttributeError:
        raise ValueError('the values must be str or bytes')
    key = SHA256.new(key).digest()
    encryptor = AES.new(key, AES.MODE_CFB)
    data = encryptor.encrypt(data)
    return encryptor.iv + data

def data_decrypt(data, key):
    """
    encrypt data
    args:
    data(bytes[str])
    key(str)

    """
    try:
        key = key.encode("utf-8")
    except AttributeError:
        pass
    key = SHA256.new(key).digest()
    iv = data[:16]
    data = data[16:]
    decryptor = AES.new(key, AES.MODE_CFB, iv)
    decrypted_data = decryptor.decrypt(data)
    return decrypted_data
