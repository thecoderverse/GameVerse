"""
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                                 Information                                              ║
╟──────────────────────────────────────────────────────────────────────────────────────────╢
║   Project : Hangman                                                                      ║
║   Coder : Hanifi CETINKAYA                                                               ║
║   Language: Python                                                                       ║
╠══════════════════════════════════════════════════════════════════════════════════════════╣
║   Code:\>                                                                                ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
"""

import random
import time
import json

hangman=[["  ╔═════╗"],
         ["  O     ║"],
         [" /|\    ║"],
         ["  |     ║"],
         [" / \    ║"],
         ["════════╝"]
        ]

totalWin=0
totalLost=0

def drawTitle():
    drawFrame("top",47)
    print("║{}{:<32}║".format(" "*15,"Welcome to Hangman"))
    drawFrame("bottom",47)

def drawFrame(place,count):
    if place=="top":
        print("{}{}{}".format("╔","═"*count,"╗"))
    elif place=="bottom":
        print("{}{}{}".format("╚","═"*count,"╝"))

def drawHangman(level):
    print("\n")
    for x in range(len(hangman)-level):
        print(hangman[x][0])
    print("\n")

def drawLine(randomWord, guessedLetterList):
    count=0
    for c in randomWord:
        if c==" ": 
                print("  ", end="")
                continue
        if c in guessedLetterList:
            print(c,end="")
            count+=1
        else:
            print(" _ ", end="")
    print("\n")
    return count

def selectRandomBook(data, category):
    books={b["title"] for b in data if b["genre"]==category} 
    books=list(books)
    return random.choice(books)

def giveHint(word, guessedLetterList):
    hintLetter=""
    while(True):
        hintLetter=word[random.randint(0,len(word)-1)]
        if not hintLetter in guessedLetterList:
            break
    return hintLetter

def game(data,category):
    global totalLost
    global totalWin
    word=selectRandomBook(data, category)
    word=word.lower()
    randomWord_=word.replace(" ","")    
    guessedLetterList=[]
    guessCount=6
    while (True):
        count=drawLine(word, guessedLetterList)
        if count==len(randomWord_):
            print("You Won!!!")
            totalWin+=1
            break
        print(f"You have {guessCount} guesses. If you want hint, you can write [ ? ] ")
        if len(guessedLetterList)>0:
            print(f"You use {guessedLetterList} letters")
        a=input("\nWrite your guess letter or word :\> ")
        a=a.lower()
        if a==word:
            print("You Won!")
            totalWin+=1
            break
        elif a in guessedLetterList:
            input(f"Letter {a} guessed before. Please press Enter ⏎   ")
        elif a=="?":
            hintLetter=giveHint(word, guessedLetterList)
            guessedLetterList.append(hintLetter)
            guessedLetterList.append("?")
            guessCount-=1        
        else:
            guessedLetterList.append(a)
            if not a in randomWord_:
                guessCount-=1

        drawHangman(guessCount)
        if guessCount==0:
            print("You lost. Game over")
            totalLost+=1
            break
    return playAgain()

def playAgain():
    print("\nYour Scores: ", end="")
    print(f"{totalWin} Win, {totalLost} Lost")
    answer = input("Would you like to play again? [Y]es / [N]o / [M]ain Menu: ")
    if answer in ("y", "Y", "Yes", "yes", "YES"):
        return answer
    elif answer in ("m", "M"):
        start()
    else:
        print("Thank you!")

def selectCategory(data):
        genres=[g["genre"] for g in data]
        genres=list(set(genres))
        drawFrame("top",47)
        for i in range(0, len(genres),2):
            print("{}{} - {:<20}{} - {:<14}{}".format("║     ",i+1,genres[i],i+2,genres[i+1],"║" if i+1 < len(genres) else ""))
        drawFrame("bottom",47)
        a=input("Select books category > ")
        return genres[int(a)-1]

def mainScreen():
    drawTitle()
    for x in hangman:
        print("{}{}".format(" "*20,x[0]))
        time.sleep(0.25)

    drawFrame("top",47)
    print("║{}{:<38}║".format(" "*9,"1 - Turkish Books Name"))
    print("║{}{:<38}║".format(" "*9,"2 - English Books Name"))
    print("║{}{:<38}║".format(" "*9,"3 - Exit"))
    drawFrame("bottom",47)
    a=input("Select > ")
    return a

def start():
    language=mainScreen()
    if language in ("1","2"):
        if language=="1":
            fileName="booksTR.json"
        else:
            fileName="booksEN.json"

        with open(fileName, "r", encoding="utf-8") as fp:
            data = json.load(fp)

        category=selectCategory(data)

        while game(data,category):
            pass
    else:
        print("Good Bye!")

# Start game
if __name__ == "__main__":
    start()
