# File: src/kyber/kyber.py
import pqcrypto.kem.kyber512 as kyber

def generate_keys():
    public_key, secret_key = kyber.generate_keypair()
    return public_key, secret_key

def encapsulate(public_key):
    ciphertext, shared_secret = kyber.encrypt(public_key)
    return ciphertext, shared_secret

def decapsulate(ciphertext, secret_key):
    shared_secret = kyber.decrypt(ciphertext, secret_key)
    return shared_secret
