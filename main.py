import random
import time
import os
import animation
import app
import csvcontrol
import api
import scraper


# List of words
words = ['word1', 'word2']
#words = ['']



##8##
def hang(turn):
    if turn < 7:
        print('  _______  ')
        print('  |/    | ')
    else:
        print('  _______  ')
        print('  |/         ')
        
    if turn < 6:
        print('  |     o  ')
    else:
        print('  |          ')
        
    if turn < 5:
        print('  |   \_|_/  ')
    else:
        print('  |          ')
        
    if turn < 4:
        print('  |     |    ')
    else:
        print('  |          ')
        
    if turn < 3:
        print('  |    / \\   ')
    else:
        print('  |          ')
        
    if turn < 2:
        print('  |   /   \\ ')
    else:
        print('  |          ')
        
    print(' _|___')

## 1 ##
def splash():
    os.system("cls")
    # introduction to the game
    delay = 3
    while delay:
        print ('  ====================')
        print ('  LET\'s PLAY HANGMAN')
        print ('  ', delay, "secs to start")
        print ('  ====================')
        print('''
        _______
        |/    |
        |     O
        |   \_|_/
        |     |
        |    / \\
        |   /   \\
     ___|___      
        \n''')
        print ('  =====================')
        time.sleep(1)
        delay = delay - 1
        os.system("cls")


#2

def game():
    #Randomly choose a word from the list
    global secret
    secret = random.choice(words)
    secret = secret.upper()
    guessed = ''
    turns = 7
    placed = '_'*len(secret)
    l = list(placed)
    done = 0

    while turns:

        while True:
            os.system("cls")
            hang(turns)
            print("\n\nSecret Word.....:",' '.join(l))
            print("\n\nLetters Used.....:",guessed)
            print("\n\nTries to go.....: ",turns)
            typed = input("\n\nGuess a Letter..: ")
            if typed not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or len(typed) > 1:
                input("Single Upper Case Letters ONLY!. Press ENTER to continue...")
            else:
                break

##5##
        turns = 7
        if typed not in guessed:
            guessed = guessed + typed
        g = list(guessed)
        s = list(secret)

        for k in range(len(g)):
            kstr = guessed[k]
            if kstr in s:
                for i in range(len(s)):
                    if kstr == s[i]:
                        l[i] = kstr
            else:
                turns = turns - 1

#7

        if l == s:
            os.system("cls")
            hang(turns)
            print("=========================================================")
            print("CONGRATULATIONS! YOU GUESSED: ", secret)
            print("=========================================================")
            input("Press Enter to continue...")
            break

        if turns == 0:
            os.system("cls")
            hang(turns)
            print("=========================================================")
            print("GAME OVER! SECRET WORD: ", secret)
            print("=========================================================")
            input("Press ENTER to continue...")
            break

## 6 ##
def Add_word():
    os.system("cls")
    print("Old word list: ", ", ".join(words))
    New_word = input('Input New word: ')
    if len(New_word) > 0:
        words.append (New_word)
    os.system("cls")
    print("New word list", ", ".join(words))
    input("Press ENTER to continue...")


def import_SQL():
    os.system("cls")
    
    new_word_list = app.get_word_list()
    return new_word_list

def viewSQL():
    print(import_SQL())
    addList=input('Import this list?  y/n')
    if addList == 'y':
        global words
        words=import_SQL()
        animation.loading(0.5)
        main()
    elif addList == 'n':
        pageSQL()
    else:
        input("Please Input Valid Option")
    viewSQL()

def pageSQL():
    os.system("cls")
    print ("==================\n\n")
    print ("    SQL Options\n\n")
    print (" 1) See List")
    print (" 2) Add New Word")
    print (" 3) Delete Word")
    print (" 4) Back\n\n")
    Choice= input('Input An Option: ')
    if Choice == "1":
        viewSQL()
    elif Choice == "2":
        print(import_SQL())
        app.update_word_list(input('Add a new word: '))
    elif Choice == "3":
        print(import_SQL())
        app.delete_word_list(input('Which word would you like to delete?'))
    elif Choice == "4":
        main()
    else:
        input("Please Input Valid Option")
    pageSQL()


def viewCSV(fileName):
    listCSV=csvcontrol.read_words_from_file(fileName)
    print(listCSV)
    addList=input('Import this list?  y/n')
    if addList == 'y':
        global words
        words=listCSV
        animation.loading(0.5)
        main()
    elif addList == 'n':
        pageCSV()
    else:
        input("Please Input Valid Option")
    viewCSV()

def pageCSV():
    os.system("cls")
    print ("==================\n\n")
    print ("    CSV Options\n\n")
    print (" 1) See List")
    print (" 2) Write new list")
    print (" 3) Change word")
    print (" 4) Delete Word")
    print (" 5) Back\n\n")
    Choice= input('Input An Option: ')
    if Choice == "1":
        fileName=input('Which file would you like to see?')
        viewCSV(fileName)
    elif Choice == "2":
        fileName=input('Which file would you like to use?')
        print(csvcontrol.read_words_from_file(fileName))
        csvcontrol.create_word_list(fileName)
        viewCSV(fileName)
    elif Choice == "3":
        fileName=input('Which file would you like to use?')
        print(csvcontrol.read_words_from_file(fileName))
        csvcontrol.update_word(fileName)
        viewCSV(fileName)
    elif Choice == "4":
        fileName=input('Which file would you like to use?')
        print(csvcontrol.read_words_from_file(fileName))
        csvcontrol.delete_word(fileName)
        viewCSV(fileName)
    elif Choice == "5":
        main()
    else:
        input("Please Input Valid Option")
    pageCSV()


def viewScrape():
    listScrape=scraper.get_words_from_web()
    print(listScrape)
    addList=input('Import this list?  y/n')
    if addList == 'y':
        global words
        words=listScrape
        animation.loading(0.5)
        main()
    elif addList == 'n':
        pageScrape()
    else:
        input("Please Input Valid Option")
    viewScrape()

def pageScrape():
    os.system("cls")
    print ("==================\n\n")
    print ("    Scrape Options\n\n")
    print (" 1) See List")
    print (" 2) Back\n\n")
    Choice= input('Input An Option: ')
    if Choice == "1":
        viewScrape()
    elif Choice == "2":
        main()
    else:
        input("Please Input Valid Option")
    pageScrape()


def viewAPI():
    listAPI=api.formRequest()
    print(listAPI)
    addList=input('Import this list?  y/n')
    if addList == 'y':
        global words
        words=listAPI
        animation.loading(0.5)
        main()
    elif addList == 'n':
        pageAPI()
    else:
        input("Please Input Valid Option")
    viewAPI()

def pageAPI():
    os.system("cls")
    print ("==================\n\n")
    print ("    API Options\n\n")
    print (" 1) See List")
    print (" 2) Back\n\n")
    Choice= input('Input An Option: ')
    if Choice == "1":
        viewAPI()
    elif Choice == "2":
        main()
    else:
        input("Please Input Valid Option")
    pageAPI()


##4##
def main():
    os.system("cls")
    print ("==================")
    print ("WELCOME TO HANGMAN")
    print ("==================\n\n")
    print ("    Main Menu\n\n")
    print (" 1) Play Game")
    print (" 2) Add New Word")
    print (" 3) SQL Options")
    print (" 4) CSV Options")
    print (" 5) Scrape the Web")
    print (" 6) Use API")
    print (" 7) Exit\n\n")
    print ("==================\n\n")
    Choice= input('Input An Option: ')
    if Choice == "1":
        splash()
        game()
    elif Choice == "2":
        Add_word()
    elif Choice == "3":
        pageSQL()
    elif Choice == "4":
        pageCSV()
    elif Choice == "5":
        pageScrape()
    elif Choice == "6":
        pageAPI()
    elif Choice == "7":
        app.closeConnection()
        os._exit(0)
    else:
        input("Please Input Valid Option")
    main()
main()    



    #38125764