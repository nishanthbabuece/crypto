# File: examples/run_all_examples.py
from kyber.kyber import generate_keys as kyber_gen, encapsulate, decapsulate
from dilithium.dilithium import generate_keys as dilithium_gen, sign, verify

# Kyber Example
pk, sk = kyber_gen()
ciphertext, shared_secret = encapsulate(pk)
recovered_secret = decapsulate(ciphertext, sk)
print('Kyber shared secret valid:', shared_secret == recovered_secret)

# Dilithium Example
pk, sk = dilithium_gen()
message = 'Test PQC'
signature = sign(message, sk)
print('Dilithium valid:', verify(message, signature, pk))

