from schemes.bitops import bitOpsEncrypt

"""
encryptor encrypts the sender's file with the sender's question and the correct answer to the question as the key
Arguments:
    mediaFile: the file to be encrypted
Returns:
    encryptedFile: file encrypted
"""
def encryptor():
    mediaFile = input("Path to file to be encrypted: ")
    encryptedFile = bitOpsEncrypt(mediaFile)

    return encryptedFile


if __name__ == "__main__":
    filePath = encryptor()
    print("Encrypted file saved to: " + filePath)