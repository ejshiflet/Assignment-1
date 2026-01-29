import random
import string
import os
import time

wordList = [] #This will add all the words from the file to a list
with open("top_english_nouns_lower_100000.txt", 'r') as file:
    for line in file:
        word = line.strip()
        if word: 
                wordList.append(word)

#==============================================================================================================

#this block of code will display the main menu and do what the user wants after taking input

def displayMainMenu():
    while(True):
        print("--------------------Main Menu---------------------")
        print("Type the number next to the menu choice you want:")
        print("1. Generate Memorable Password")
        print("2. Generate Random Password")
        print("3. Generate 1000 Memorable and Random Passwords")
        print("4. Exit Program")
        userInput = input()
        if userInput == "1":
            generateMemorablePassword()
        elif userInput == "2":
            generateRandomPassword()
        elif userInput == "3":
            generateMemorableAndRandomPasswords()
        elif userInput == "4":
            print("Closing Program...")
            break
        else:
            print("Please enter the number with no spaces.")

#==============================================================================================================

def generateMemorablePassword():
    while(True):
        print("Enter the amount of words you want in your password from 4-7: ")
        wordAmount = input() # ask the user how many words they want
        if wordAmount == "4": 
            break
        elif wordAmount == "5":
            break
        elif wordAmount == "6":
            break
        elif wordAmount =="7":
            break
        else:
            print("Please enter the number with no spaces.")
    amount = int(wordAmount)# converts it to a number
    password = ""
    i = 1
    while(True):# loop creates a string of words and numbers with a '-' in between for the amount of words the user decided
        word = random.choice(wordList)
        password = password + word
        number = random.randint(0,9)
        numberString = str(number)
        password = password + numberString
        if i == amount:
            break
        else:
            password = password + "-"
            i = i + 1
    while(True):
        print("Here is your password: " + password)
        timeNow = time.ctime()# logs the time it was created
        print("Type '1' and click enter to continue")
        finished = input()
        if finished == "1":
            break
        else:
            print("Please enter the number with no spaces.")
    os.makedirs("Memorable", exist_ok=True)# makes directory if it does not exist and appends to file
    full_path = os.path.join("Memorable", "Generated_Passwords.txt")
    with open(full_path, 'a') as file:
        file.write(password + "," + timeNow + "\n")
 
#==============================================================================================================

def generateRandomPassword():
    while(True):# while loop gets how long the user want the password to be
        print("Enter the amount of characters you want in your password from 8-24: ")
        characterAmount = input()
        if characterAmount.isdigit():
            amount = int(characterAmount)
            if amount >= 0 and amount <= 24:
                break
            else:
                print("Please enter a number between 8 and 24.")
        else:
            print("Please enter a number between 8 and 24.")

    while(True):# for loop ask if they want symbols included or not and constructs a character string
        print("Would you like symbols in your password? Enter '1' for yes or '2' for no")
        choice = input()
        if choice == "1":
            characters = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
            break
        elif choice == "2":
            characters = string.ascii_uppercase + string.ascii_lowercase
            break
        else:
            ("Please enter the number with no spaces.")
    characterList = list(characters) # all the available characters are put in a list to be used for password
    password = ""
    i = 1
    while(True):
        characterSingle = random.choice(characterList)# chooses a random character from list and appends to password
        password = password + characterSingle
        if i == amount:
            break
        else:
            i = i + 1
    while(True):
        print("Here is your password: " + password)
        timeNow = time.ctime()# time password was created
        print("Type '1' and click enter to continue")
        finished = input()
        if finished == "1":
            break
        else:
            print("Please enter the number with no spaces.")
    os.makedirs("Random", exist_ok=True)
    full_path = os.path.join("Random", "Generated_Passwords.txt")# this part of code appends to existing file if it already exist of makes a new one
    with open(full_path, 'a') as file:
        file.write(password + "," + timeNow +  "\n")

#==============================================================================================================

# this block of code rewrites what the previous 2 function did but without user inputs

def generateMemorablePasswordNoInputs():
    amount = random.randint(4,7)
    password = ""
    i = 1
    while(True):# while loop makes password with words numbers and '-'
        word = random.choice(wordList)
        password = password + word
        number = random.randint(0,9)
        numberString = str(number)
        password = password + numberString
        if i == amount:
            break
        else:
            password = password + "-"
            i = i + 1
    os.makedirs("ManyPasswords", exist_ok=True)# adds password to the list of 1000 passwords
    full_path = os.path.join("ManyPasswords", "Generated_Passwords.txt")
    with open(full_path, 'a') as file:
        file.write(password + "\n")


def generateRandomPasswordNoInputs():
    amountOfCharacters = random.randint(8,24)
    choice = random.randint(1,2)
    if choice == 1:
            characters = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    elif choice == 2:
            characters = string.ascii_uppercase + string.ascii_lowercase 
    characterList = list(characters)# chooses randomly between no or yes to symbols and the amount of characters is random
    password = ""
    i = 1
    while(True):# this while loop crafts a random password with the amount of characters and other choices
        characterSingle = random.choice(characterList)
        password = password + characterSingle
        if i == amountOfCharacters:
            break
        else:
            i = i + 1
    os.makedirs("ManyPasswords", exist_ok=True)# this part of code appends to existing file if it already exist of makes a new one
    full_path = os.path.join("ManyPasswords", "Generated_Passwords.txt")
    with open(full_path, 'a') as file:
        file.write(password + "\n")


def generateMemorableAndRandomPasswords():
    i = 0
    while(i<1000):# while loop runs 1000 times adding passwords and randomly chooses between memorable and random passwords
        choice = random.randint(1,2)
        if choice == 1:
            generateMemorablePasswordNoInputs()
            i = i + 1
        elif choice == 2:
            generateRandomPasswordNoInputs()
            i = i + 1

#==============================================================================================================

displayMainMenu()