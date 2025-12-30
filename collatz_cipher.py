class CollatzCipher:
    """
    Stream Cipher based on Collatz Conjecture (3n+1).
    """
    def __init__(self, key: str):
        self.seed = self._derive_seed(key)

    def _derive_seed(self, key: str) -> int:
        """
        Derives a crude integer seed from the string key.
        """
        seed = 0
        for i, char in enumerate(key):
            # Simple mixing
            seed = (seed * 31 + ord(char) * (i + 1)) 
        
        # Ensure seed is positive and non-zero
        return abs(seed) if seed != 0 else 12345

    def _keystream_generator(self, length: int):
        """
        Yields `length` bytes of keystream.
        """
        n = self.seed
        original_seed = self.seed
        reseed_counter = 0

        for _ in range(length):
            # Collatz Step
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            
            # Loop Avoidance / Entropy Injection
            # If n reaches 1, the sequence enters 4-2-1 loop.
            # We break out by modifying n.
            if n == 1:
                reseed_counter += 1
                # Mix original seed with counter to get a new starting point
                n = original_seed + (reseed_counter * 0xCAFEBABE)
                # Ensure we don't just stay at 0 or something uniform (though Collatz usually grows)
                if n == 0: n = 1

            yield n % 256

    def encrypt(self, plaintext: str) -> bytes:
        """
        Encrypts a string plaintext into bytes.
        """
        data = plaintext.encode('utf-8')
        return self._process(data)

    def decrypt(self, ciphertext: bytes) -> str:
        """
        Decrypts bytes back to string.
        """
        decrypted_bytes = self._process(ciphertext)
        return decrypted_bytes.decode('utf-8')

    def _process(self, data: bytes) -> bytes:
        """
        XOR data with keystream.
        """
        keystream = self._keystream_generator(len(data))
        return bytes([b ^ k for b, k in zip(data, keystream)])

if __name__ == "__main__":
    # Quick sanity check
    cipher = CollatzCipher("secret")
    msg = "Hello World"
    enc = cipher.encrypt(msg)
    dec = cipher.decrypt(enc)
    print(f"Original: {msg}")
    print(f"Encrypted: {enc.hex()}")
    print(f"Decrypted: {dec}")
    assert msg == dec
