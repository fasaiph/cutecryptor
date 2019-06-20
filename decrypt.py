from schemes.bitops import bitOpsDecrypt

"""
decryptor decrypts the encrypted file if the user knows the correct answer to the pop-up question specified by encryptor
Arguments:
    encryptedFile: file encrypted by the sender (.txt format)
Returns:
    decryptedFile: file path of decrypted file
"""
def decryptor():
    encryptedFile = input("Path to file to be decrypted: ")
    decryptedFile = bitOpsDecrypt(encryptedFile)
    return decryptedFile

if __name__ == "__main__":
    filePath = decryptor()
    print("Saved to: " + filePath)