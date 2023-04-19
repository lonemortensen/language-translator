# =======================================================================
# Project: Language Translator App
# Description: An interactive app built with Python.
# The app lets users:
# - translate English words into Spanish and French.
# Background: Coursework for Skillcrush's "Getting Started with Python" course.

# ==== *** ====

# The main.py file contains code that:
# - promts the user for input and displays translations and messages to the user.
# - converts the CSV file to a Python dictionary so data can be read by Python.
# - uses the CSV module to search in and access data from a premade CSV file containing English, Spanish, and French words.
# =======================================================================

# Imports translations.csv file:
import csv


# Introduction message with greeting and user instructions:
def intro():
    print(
        'Welcome to the Spanish and French translator app!\nPlease enter an English word to translate and press the "Enter" key.'
    )
    print('\nType "done" at any time to exit the app.')


# Exit message:
def exit():
    print('\nThanks for using the translator app. Have a great day!')


# Translations dictionary variable:
translations = {}

# Opens and reads csv file, and converts csv file to Python dictionary using DictReader():
with open("translations.csv", "r") as words:
    reader = csv.DictReader(words, delimiter=",")
    # Loop searches through each line in the csv file for English, Spanish and French words:
    for line in reader:
        # Variables contain refences to column headers in csv file:
        english = line["English"].lower()
        spanish = line["Spanish"].lower()
        french = line["French"].lower()
        # Sets English header in csv file as dictionary key, and Spanish/French words as values:
        translations[english] = [spanish, french]

done = False

intro()

while not done:
    word = input(
        "\nEnter an English word to translate into Spanish and French: ")
    # Returns string where all characters are lower case:
    word = word.lower()

    if word == "done":
        done = True
        exit()
    elif word in translations:
        # Puts Spanish and French translations on separate lines:
        # - word variable represents dictionary key.
        # - index represents language as per order of value positions in for loop.
        print(f'\nSPANISH: {translations[word][0]}')
        print(f'\nFRENCH: {translations[word][1]}')
    else:
        print("\nThe word is not in the dictionary!")
