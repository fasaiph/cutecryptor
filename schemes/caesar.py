# Caesar encryption


alphabet = "abcdefghijklmnopqrstuvwxyz "
Caesar_correct_key = 5

def Caesar_encode(key):
    encrypted = ""

    message = input("Enter the Message: ")  # hello
    for i in message:
        position = alphabet.find(i) # return index of i
        newposition = (position + key) % 27
        encrypted += alphabet[newposition]

    return encrypted

def Caesar_decode(encryptedmsg):
    decrypted = ""

    guessed_key = input("What is the key? ")
    print(guessed_key)

    if guessed_key != str(Caesar_correct_key):
        print("Key is wrong.")
        exit(0)

    for i in encryptedmsg:
        position = alphabet.find(i)
        newposition = (position - Caesar_correct_key) % 27
        decrypted += alphabet[newposition]

    return decrypted


if __name__ == "__main__":
    Caesar_key = 5
    myencrypted = Caesar_encode(5)
    print("Encrypted Message: " + myencrypted)
    mydecrypted = Caesar_decode(myencrypted)
    print("Decrypted Message: " + mydecrypted)
