#!/usr/local/bin/python

#NOTES FOR MR. ZAMANSKY:
#Most of the recent stuff I have done in python was over the summer 
#for a company so it isn't code I own/can post in a public github.
#This is something a little bit older

import random

class Card:

    _found = False
    _up = False
    _number = 0
    _value = ""

    def __init__(self, value, number):
        self._value = value
        self._number = number
        self._up = False
        self._found = False

    def __str__(self):
        if self._found:
            return ""
        elif self._up:
            return self._value
        else:
            return str(self._number)

board = [""]*16
baseStrings = ["cat","bat","mat","fat","hat","that","pat","vat"]
playerTurn = random.randrange(2)
changeMove = True
oneScore = 0
twoScore = 0

def setup():
    for base in baseStrings:
        for x in range(2):
            while True:
                location = random.randint(0,15)
                if board[location] == "":
                    board[location] = Card(base, location)
                    break

def printBoard():
    for x in range(len(board)):
        print str(board[x]) + "\t",
        if x != 0 and (x + 1) % 4 == 0:
            print

def play():
    global playerTurn, changeMove, oneScore, twoScore
    printBoard()
    if changeMove == True:
        if playerTurn == 1:
            playerTurn = 2
            whoseMove = "Player 2"
        else:
            playerTurn = 1
            whoseMove = "Player 1"
    else:
        if playerTurn == 1:
            whoseMove = "Player 1"
        else:
            whoseMove = "Player 2"
    print "It's your turn, %s" %whoseMove
    num1 = int(raw_input("Input your first number: "))
    while board[num1]._found == True:
        num1 = int(raw_input("That tile has been found.  Input your first number: "))
    num2 = int(raw_input("Input your second number: "))
    while board[num2]._found == True:
        num2 = int(raw_input("That tile has been found.  Input your second number: "))
    for x in range(100):
        print
    board[num1]._up = True
    board[num2]._up = True
    printBoard()
    if board[num1]._value in board[num2]._value:
        board[num1]._found = True
        board[num2]._found = True
        if playerTurn == 1:
            oneScore += 1
        else:
            twoScore += 1
        changeMove = False
    else:
        board[num1]._up = False
        board[num2]._up = False
        print "No match. Try again."
        changeMove = True
    raw_input("Press enter to continue")
    for x in range(100):
        print
    for x in board:
        if x._found == False:
            play()
            break


def go():
    setup()
    play()
    global playerTurn
    if oneScore > twoScore:
        whoWon = "Player 1"
    elif twoScore > oneScore:
        whoWon = "Player 2"
    else:
        whoWon = "it's a tie"
    print "Congratulations, %s.  Press enter to exit.  Thanks for playing" % whoWon
    
go()
