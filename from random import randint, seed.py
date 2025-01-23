from random import randint, seed

# Use the same seed and random sequence as in the encryption function
seed(10)
randoms = [randint(1, 100) for _ in range(624)]

class EmptyError(Exception):
    pass

def decrypt(ciphertext, key):
    pt = []
    try:
        if key == '':
            raise EmptyError
        key = int(key)
    except ValueError:
        return "Error: Key must be an integer less than 256"
    except EmptyError:
        return "Enter a key as an integer less than 256"

    try:
        # Convert the ciphertext from hex to bytes
        ct_bytes = bytes.fromhex(ciphertext)

        for n, byte in enumerate(ct_bytes):
            # Reverse the encryption logic to retrieve the original character
            pt.append(chr(byte - randoms[n] - key))

        return ''.join(pt)
    except ValueError:
        return "Error: Invalid ciphertext or incorrect key"

def brute_force_flag(ciphertext):
    for key in range(256):
        plaintext = decrypt(ciphertext, key)
        if plaintext.startswith("flag{") and plaintext.endswith("}"):
            return f"Key: {key}, Plaintext: {plaintext}"
    return "No valid key found"

# Example usage:
ciphertext = "db9cc3d0f0a1ae98ddaee8b38fe2d2ba94bef0bda0cfa1d8bfc8c2b7ff"
result = brute_force_flag(ciphertext)
print(result)
