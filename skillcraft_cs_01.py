'''
Task-01
Implement Caesar Cipher
Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. 
Allow users to input a message and a shift value to perform encryption and decryption.

'''
# made by Ashwak_N

def encryption(message, shift):
   
    result = ""
    for char in message:
        if char == " ":
            result += " "
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  
    return result


def decryption(message, shift):
    
    return encryption(message, -shift)


def main():
   
    print("Caesar Cipher Encryption and Decryption")

   
    message = input("Enter the message to encrypt: ")
    while True:
        try:
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the shift value.")

   
    encrypted_message = encryption(message, shift)
    decrypted_message = decryption(encrypted_message, shift)

   
    print("\nEncrypted message:", encrypted_message)
    print("\nDecrypted message:", decrypted_message)
    print("\n")


if __name__ == "__main__":
    main()



        
