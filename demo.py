import sys
from collatz_cipher import CollatzCipher

def main():
    print("--- Collatz Conjecture Cipher Demo ---")
    
    while True:
        print("\nMenu:")
        print("1. Encrypt Text")
        print("2. Decrypt Hex")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            text = input("Enter text to encrypt: ")
            key = input("Enter encryption key: ")
            
            cipher = CollatzCipher(key)
            encrypted = cipher.encrypt(text)
            
            print(f"\n[+] Encrypted (Hex): {encrypted.hex()}")
            
        elif choice == '2':
            hex_data = input("Enter hex string to decrypt: ")
            key = input("Enter decryption key: ")
            
            try:
                ciphertext = bytes.fromhex(hex_data)
                cipher = CollatzCipher(key)
                decrypted = cipher.decrypt(ciphertext)
                print(f"\n[+] Decrypted Text: {decrypted}")
            except ValueError:
                print("\n[!] Error: Invalid Hex string or UTF-8 decoding issue.")
            except Exception as e:
                print(f"\n[!] Error: {e}")
                
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid toggle.")

if __name__ == "__main__":
    main()
