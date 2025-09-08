# Post-Quantum Examples

Interactive examples of major NIST PQC (Post-Quantum Cryptography) algorithms.

## Overview
Post-Quantum Cryptography (PQC) algorithms are designed to remain secure against attacks from quantum computers, which could break widely-used classical cryptographic algorithms like RSA and ECC. This repository provides hands-on examples of key PQC algorithms to help researchers, developers, and enthusiasts understand their usage, functionality, and performance.

### Included Algorithms
- **Kyber (KEM)** – Key Encapsulation Mechanism, suitable for secure key exchange.
- **Dilithium (Digital Signature)** – Efficient lattice-based digital signature.
- **Falcon (Digital Signature)** – Lattice-based digital signature with compact keys.
- **Rainbow (Digital Signature)** – Multivariate polynomial-based digital signature.
- **SPHINCS+ (Hash-based Signature)** – Stateless hash-based digital signature scheme.

## Why PQC?
Quantum computers can solve certain mathematical problems (like integer factorization and discrete logarithms) exponentially faster than classical computers. This threatens classical cryptography:

- RSA and ECC could be broken by Shor's algorithm.
- Symmetric cryptography would require doubled key lengths to remain secure.

PQC algorithms are designed to be resistant to both classical and quantum attacks, ensuring long-term data security.

## Repository Structure
```
post-quantum-examples/
│
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── notebooks/                 # Interactive Jupyter notebooks for each algorithm
├── src/                       # Python implementations / wrappers of algorithms
├── examples/                  # Scripts to run all examples at once
└── utils/                     # Helper functions
```

## Getting Started
1. **Clone the repository:**
```
git clone https://github.com/yourusername/post-quantum-examples.git
cd post-quantum-examples
```

2. **Install dependencies:**
```
pip install -r requirements.txt
```

3. **Run Jupyter notebooks:**
```
jupyter notebook
```
Open any notebook in the `notebooks/` folder to run examples interactively.

## How to Use the Demo
- Each notebook demonstrates key generation, encryption/signing, and verification.
- You can modify the **message input** to simulate different scenarios.
- For KEM (Kyber), you can generate multiple key pairs and test key exchange.
- For signatures (Dilithium, Falcon, Rainbow, SPHINCS+), you can test signing different messages and verifying them.
- `examples/run_all_examples.py` provides a quick way to test all algorithms with default parameters.

## Customization
- **Change message content**: Update the `message` variable in notebooks or `run_all_examples.py`.
- **Benchmarking / experimentation**: You can add loops to measure performance, test with different key sizes (if supported), or simulate multiple users.

## References
- [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [PQCrypto Python library](https://pypi.org/project/pqcrypto/)

This repository is intended for educational, research, and simulation purposes to understand PQC algorithms and their behavior under different scenarios.
