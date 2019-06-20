import random

def readMediaFile(mediaFile):
    fo = open(mediaFile, "rb")
    mediaBitstream = fo.read()

    print("Length of Media Bitstream: " + str(len(mediaBitstream)))
    fo.close()
    return mediaBitstream


def createInfoBitstream(question, correctAnswer, keyIdx):
    # probably don't need correctAnswer
    questionSpacer = " QQQQ"
    ender = "EEEE"

    combinedString = question + questionSpacer + str(keyIdx) + ender
    infoBitstream = bytearray(combinedString, "utf-8")

    return infoBitstream


def separate(fileWithInfo):
    fileStartIdx = 0
    questionEndIdx = 0
    randomIdx = 0
    fileLength = len(fileWithInfo)
    idx = 0

    while idx < fileLength:
        if fileWithInfo[idx:idx+4] == bytearray("QQQQ", "utf-8"):
            questionEndIdx = idx
        elif fileWithInfo[idx:idx+4] == bytearray("EEEE", "utf-8"):
            randomIdx = idx - 1
            fileStartIdx = idx + 4
            break
        idx += 1


    fileQuestion = fileWithInfo[:questionEndIdx].decode()
    answerIdx = int(chr(fileWithInfo[randomIdx]))
    file = fileWithInfo[fileStartIdx:]

    return fileQuestion, answerIdx, file


def bitOpsEncrypt(mediaFile):
    question = input("Question to encrypt file with: ")
    correctAnswer = input("Correct answer to question: ")
    correctAnswer = correctAnswer.lower()

    # get key
    keyIdx = random.randint(0, len(correctAnswer)-1)
    key = ord(correctAnswer[keyIdx])
    # print("Random index is: ")
    # print(keyIdx)
    # print("Key is: ")
    # print(key)

    # encode question, correct answer, and key idx as a bitstream
    infoBitstream = createInfoBitstream(question, correctAnswer, keyIdx)
    # print(infoBitstream)

    # read media file
    image = readMediaFile(mediaFile)

    # convert to a byte array
    image = bytearray(image)

    # xor the byte array with the key
    for idx, b in enumerate(image):
        image[idx] = b ^ key

    # open a new file to store the encrypted file
    encryptedFilepath = mediaFile[:-4] + "_encrypted" + mediaFile[-4:]
    fo = open(encryptedFilepath, "wb") # -4 might change depending on file extension
    fo.write(infoBitstream + image)
    fo.close()

    return encryptedFilepath


def bitOpsDecrypt(encryptedFile):

    fo = open(encryptedFile, "rb")
    encryptedImg = fo.read()

    encryptedImg = bytearray(encryptedImg)

    # separate info bitstream from media bitstream
    infoQuestion, infoAnswerIdx, encryptedMedia = separate(encryptedImg)
    # print("Question:")
    # print(infoQuestion)
    # print("infoAnswerIdx: ")
    # print(infoAnswerIdx)

    # See if receiver has key
    guessed_answer = input(infoQuestion)
    key = ord(guessed_answer[infoAnswerIdx])
    # print("Guessed key: ")
    # print(key)

    # if not guessed_answer == str(key):
    #     print("Incorrect Key")
    #     exit(0)


    print("Length of Media Bitstream: "+ str(len(encryptedMedia)))
    for idx, b in enumerate(encryptedMedia):
        encryptedMedia[idx] = b ^ key

    # open a new file to store the decrypted file
    decrypted_filepath = encryptedFile[:-13] + "decrypted" + encryptedFile[-4:]
    fo = open(decrypted_filepath, "wb")
    fo.write(encryptedMedia)
    fo.close()

    return decrypted_filepath


if __name__ == "__main__":
    originalFile = "media/cutecat.jpg"
    # question = "WHAT IS LIFE"
    # answer = "A simulation"
    # keyIdx = 5
    # key = 48

    # bitstream = createInfoBitstream(question, answer, keyIdx)
    # print(bitstream)

    # info, file = separate(bytearray("asdfjkl;aEEEEfilefilefile", "utf-8"))
    # print("Info: ")
    # print(info)
    # print("File: ")
    # print(file)

    myEncryptedFile = bitOpsEncrypt(originalFile)
    print("Saved Encrypted file to: " + myEncryptedFile)

    # myDecryptedFile = bitOpsDecrypt(myEncryptedFile)
    # print("Saved Decrypted file to: " + myDecryptedFile)