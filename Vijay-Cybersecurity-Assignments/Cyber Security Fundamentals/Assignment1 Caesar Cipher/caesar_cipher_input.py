def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            shifted = chr((ord(char) - ord(base) + shift) % 26 + ord(base))
            result += shifted
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    shift = 4
    
    message = input("Enter message to encrypt: ")
    encrypted = caesar_encrypt(message, shift)
    print("Encrypted message:", encrypted)
    
    ciphertext = input("Enter message to decrypt: ")
    decrypted = caesar_decrypt(ciphertext, shift)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
