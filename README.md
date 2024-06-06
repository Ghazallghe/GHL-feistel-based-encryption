GHL Encryption Algorithm

Overview:
------------
The GHL Encryption Algorithm is a symmetric key encryption technique based on a Feistel network. This algorithm utilizes a Feistel function and operates with a block size of 128 bits and a key size of 64 bits. The algorithm's design incorporates both the Feistel function and key scheduling for encryption and decryption.

Implementation:
-----------------
The provided Python code implements the GHL Encryption Algorithm. Below are the key components and functionalities of the code:

1. Feistel Function:
   - The `f(R, K)` function serves as the Feistel function within the algorithm. It applies a series of permutations and substitutions to the input data.


2. Key Scheduling:
   - The `get_keys(key)` function generates subkeys from the initial key using a key scheduling algorithm. These subkeys are used in the encryption and decryption processes.

3. Permutation and Substitution:
   - The algorithm employs permutation tables and substitution boxes (S-boxes) for data transformation, enhancing security and diffusion.

4. Encryption and Decryption:
   - The `ghl_encryption()` function implements the encryption and decryption processes using the Feistel network. It iteratively applies the Feistel function with the generated subkeys.

Usage:
-------
To use the GHL Encryption Algorithm:

1. Set the plaintext and key variables in the code.
2. Execute the code to perform encryption and decryption.
3. Review the output ciphertext and plaintext results.

Note: Ensure that the plaintext and key are of appropriate lengths and formatted (binary) correctly for proper execution.

Example:
-----------
```python
plaintext = 'COMPUTERSECURITY'
key = 'ghcipher'

# Perform Encryption
ciphertext = ghl_encryption(convert_to_binary(plaintext), convert_to_binary(key), enc=True)
print(f'Encrypted Ciphertext: {ciphertext}')

# Perform Decryption
plaintext_decrypted = ghl_encryption(ciphertext, convert_to_binary(key), enc=False)
print(f'Decrypted Plaintext: {plaintext_decrypted}')
