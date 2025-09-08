import pqcrypto.sign.dilithium2 as dilithium

def generate_keys():
    public_key, secret_key = dilithium.generate_keypair()
    return public_key, secret_key

def sign(message, secret_key):
    signature = dilithium.sign(message.encode(), secret_key)
    return signature

def verify(message, signature, public_key):
    try:
        dilithium.verify(message.encode(), signature, public_key)
        return True
    except Exception:
        return False
