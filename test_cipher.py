import unittest
from collatz_cipher import CollatzCipher

class TestCollatzCipher(unittest.TestCase):

    def test_basic_encryption_decryption(self):
        key = "secret_key"
        plaintext = "Merhaba Dünya!"
        cipher = CollatzCipher(key)
        encrypted = cipher.encrypt(plaintext)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(plaintext, decrypted)

    def test_empty_string(self):
        key = "key"
        plaintext = ""
        cipher = CollatzCipher(key)
        encrypted = cipher.encrypt(plaintext)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(plaintext, decrypted)

    def test_long_string(self):
        key = "long_key"
        plaintext = "A" * 1000
        cipher = CollatzCipher(key)
        encrypted = cipher.encrypt(plaintext)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(plaintext, decrypted)

    def test_special_characters(self):
        key = "special"
        plaintext = "Şifre: 1234! @#$½{[]}"
        cipher = CollatzCipher(key)
        encrypted = cipher.encrypt(plaintext)
        decrypted = cipher.decrypt(encrypted)
        self.assertEqual(plaintext, decrypted)

    def test_wrong_key_decryption(self):
        key1 = "correct_key"
        key2 = "wrong_key"
        plaintext = "Gizli Mesaj"
        
        cipher1 = CollatzCipher(key1)
        encrypted = cipher1.encrypt(plaintext)
        
        cipher2 = CollatzCipher(key2)
        try:
            decrypted = cipher2.decrypt(encrypted)
            self.assertNotEqual(plaintext, decrypted)
        except UnicodeDecodeError:
            # If it fails to decode, that also means it's not the original text
            pass

    def test_different_seeds(self):
        # Ensure different keys produce different ciphertexts for the same input
        plaintext = "Ayni mesaj"
        cipher1 = CollatzCipher("key1")
        cipher2 = CollatzCipher("key2")
        
        enc1 = cipher1.encrypt(plaintext)
        enc2 = cipher2.encrypt(plaintext)
        
        self.assertNotEqual(enc1, enc2)

if __name__ == '__main__':
    unittest.main()
