import random
import string

# Function to generate random characters of given length
def generate_random_letters(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Function to Encode word
def encodeWord(word):
    if(len(word) > 2):
        newWord = word[1:len(word)] + word[0]
        newWord = generate_random_letters(3) + newWord + generate_random_letters(3)

    else:
        newWord = "".join(reversed(word))

    return newWord

# Function to Decode Word
def decodeWord(word):
    if(len(word) > 2):
        return word[-4] + word[3:-4]
    else:
        return ''.join(reversed(word))
    
# Function to encode message
def encodeMessage(message):
    message = message.split(' ')
    encodedMessage = ''
    for word in message:
        encodedMessage += encodeWord(word)
        encodedMessage += ' '

    return encodedMessage

# Function to decode message
def decodeMessage(message):
    message = message.split(' ')
    decodedMessage = ''
    for word in message:
        decodedMessage += decodeWord(word)
        decodedMessage += ' '

    return decodedMessage

if __name__ == "__main__":

    print("encode/decode Message".upper().center(100))

    while(True):

        print("""
FUNCTIONALITIES:-
    1. ENCODE MESSAGE
    2. DECODE MESSAGE
    3. EXIT
""")

        functionChoice = int(input("Enter Your Choice: "))

        if(functionChoice == 3): exit()

        message = input("\nEnter Your Message : ")

        newMessage = ''
        if(functionChoice == 1):
            newMessage += encodeMessage(message)
        elif(functionChoice == 2):
            newMessage += decodeMessage(message)

        print(f"\nYour {'Encoded' if functionChoice == 1 else 'Decoded'} message is:- \n{newMessage}")

    