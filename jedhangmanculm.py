# -*- coding: utf-8 -*-
"""JedHangmanCulm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FLpusGtfnT-oLFSTRcSGf5tx73IH-pEZ
"""

import random
#my dictionary of words consits of only countries, get a map!
words = ["afghanistan", "albania", "algeria", "andorra", "angola", "antigua and barbuda", "argentina", "armenia", "australia", "austria", "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium", "belize", "benin", "bhutan", "bolivia", "bosnia and herzegovina", "botswana", "brazil", "brunei", "bulgaria", "burkina faso", "burundi", "cambodia", "cameroon", "canada", "cape verde", "central african republic", "chad", "chile", "china", "colombia", "comoros", "congo", "costa rica", "croatia", "cuba", "cyprus", "czech republic", "denmark", "djibouti", "dominica", "dominican republic", "east timor", "ecuador", "egypt", "el salvador", "equatorial guinea", "eritrea", "estonia", "eswatini", "ethiopia", "fiji", "finland", "france", "gabon", "gambia", "georgia", "germany", "ghana", "greece", "grenada", "guatemala", "guinea", "guinea-bissau", "guyana", "haiti", "honduras", "hungary", "iceland", "india", "indonesia", "iran", "iraq", "ireland", "israel", "italy", "ivory coast", "jamaica", "japan", "jordan", "kazakhstan", "kenya", "kiribati", "kuwait", "kyrgyzstan", "laos", "latvia", "lebanon", "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg", "madagascar", "malawi", "malaysia", "maldives", "mali", "malta", "marshall islands", "mauritania", "mauritius", "mexico", "micronesia", "moldova", "monaco", "mongolia", "montenegro", "morocco", "mozambique", "myanmar", "namibia", "nauru", "nepal", "netherlands", "new zealand", "nicaragua", "niger", "nigeria", "north korea", "north macedonia", "norway", "oman", "pakistan", "palau", "panama", "papua new guinea", "paraguay", "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda", "saint kitts and nevis", "saint lucia", "saint vincent and the grenadines", "samoa", "san marino", "sao tome and principe", "saudi arabia", "senegal", "serbia", "seychelles", "sierra leone", "singapore", "slovakia", "slovenia", "solomon islands", "somalia", "south africa", "south korea", "south sudan", "spain", "sri lanka", "sudan", "suriname", "sweden", "switzerland", "syria", "taiwan", "tajikistan", "tanzania", "thailand", "togo", "tonga", "trinidad and tobago", "tunisia", "turkey", "turkmenistan", "tuvalu", "uganda", "ukraine", "united arab emirates", "united kingdom", "uruguay", "uzbekistan", "vanuatu", "vatican city", "venezuela", "vietnam", "yemen", "zambia", "zimbabwe"]
#a big issue that delayed my completion was that they used to be uppercase meaning Case sensitivity
#^which made me wonder why first letter couldnt be guessed
print("====================================")
print("Welcome to Jed's Hangman Culminating")
#chooses a random word
randomWord = random.choice(words)
tellLength = len(randomWord)#len means length (wow ur so smart and kewll!!!)
print()#im putting a bunch of these for style reasons theres prob a better way just dont wanna do it
print(f"The Length of the word chosen is {tellLength}")#why didnt we bring f strings to notice
for x in randomWord:
    print("_", end=" ")#python T'n'T
def printWord(guessedLetters):
    counter = 0
    rightLetters = 0
    for char in randomWord:
        if char in guessedLetters:
            print(randomWord[counter], end=" ")
            rightLetters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return rightLetters
def printLines():
    print("\r")#this moves the cursor to the beginning of the line (again ur so kewll!!)
    for char in randomWord:
        print("\u203E", end=" ")#u203E is an overline and i bet u didnt know att
wordLength = len(randomWord)#python T'n'T
guesses = 0
totalGuesses = 0
lettersGuessed = []
lettersRight = 0
#this while loop below slowed down my finish as I had an idea but had to troubleshoot
print()
while guesses != 10 and lettersRight != wordLength:
    print("Letters guessed so far: ")
    for letter in lettersGuessed:
        print(letter, end=" ")
        print()
    guessedLetter = input("Guess a letter: ")
    if guessedLetter in randomWord:
      print()
      print("Correct that is in the word!")
    else:
      print()
      print("That's not in the word so why would you guess it???")
    if guessedLetter in randomWord:
        totalGuesses += 1
        lettersGuessed.append(guessedLetter)
        lettersRight = printWord(lettersGuessed)
        printLines()#python T'n'T
    else:
        guesses += 1
        lettersGuessed.append(guessedLetter)
        lettersRight = printWord(lettersGuessed)
        printLines()
print(f"The word was {randomWord}")
print("No ones asking you to play again")
#im so good!!!
#i was promised bonus points at 3 different occasions