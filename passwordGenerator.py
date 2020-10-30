#!/bin/python3

# By idefixkaputt

import sys
import random

charsTotal = 'qwertzuioplkjhgfdsayxcvbnmWERTZUIOPLKJHGFDSAYXCVBNM1234567890!"$%&/()=?<>.,:;-_'
charsLow = 'qwertzuioplasdfghjklyxcvbnmQWERTZUIOPLKJHGFDSAYXCVBNM'
charsMedium = 'qwertzuioplkjhgfdsayxcvbnmWERTZUIOPLKJHGFDSAYXCVBNM1234567890'
password = ''
numChar = 0
numPasswords = 1

print('****************************')
print('*****Password Generator*****')
print('****************************')


#####################################################
# Primary Functions - Main Menu Functions
#####################################################
# Main menu selection A
# It just creates a random password with 12 characters including letters, numbers and symbols
def simple_pass():
    global password
    for a in range(12):
        password += random.choice(charsTotal)
    print(password)

# Main menu selection B
# Jumps to functions to select level of security according to characters type to be included
# This function can be eliminated and send from menu directly to next function
# but might serve as middle point for improvements
def one_pass():
    menu_security()

# Main menu selection C
# This function can be eliminated and send from menu directly to next function
# but might serve as middle point for improvements
def mul_pass():
    menu_multi()
#####################################################
#####################################################


#####################################################
# When multiple passwords, same or different characteristics
#####################################################
def same():
    global numPasswords
    numPasswords = int(input('How many passwords do you want?: '))
    menu_security()

def diff():
    num_passwords_diff = 0
    num_passwords_diff = int(input('How many passwords do you want?: '))
    for a in range(num_passwords_diff):
        menu_security()
#####################################################
#####################################################


#####################################################
# Security level definition
#####################################################
# Low security password generator
# Password generator for only letters
def low_sec():
    global password
    global numChar
    global charsLow
    global numPasswords
    for b in range(numPasswords):
        for a in range(numChar):
            password += random.choice(charsLow)
        print(password)
        password = ''

# Medium security password generator
# Letters and numbers
def medium_sec():
    global password
    global numChar
    global charsMedium
    global numPasswords
    for b in range(numPasswords):
        for a in range(numChar):
            password += random.choice(charsMedium)
        print(password)
        password = ''

# High security password generator
# Letters, numbers and symbols
def high_sec():
    global password
    global numChar
    global charsTotal
    global numPasswords
    for b in range(numPasswords):
        for a in range(numChar):
            password += random.choice(charsTotal)
        print(password)
        password = ''
#####################################################
#####################################################


#####################################################
# Menu for multiple or equal characteristics
#####################################################
def menu_multi():
    m3 = input("""Do you want your multiple passwords to have the same characteristics? Y/N: """)
    if m3 == "Y" or m3 == "y":
        same()
    elif m3 == "N" or m3 == "n":
        diff()
    else:
        print('Invalid option, you must select either Y or N')
        print('Please try again')
        menu_multi()
#####################################################
#####################################################

#def append(m3):
# how to append variables
# create variable that will be collecting the data and append every time password gets a value
#    passresultslist = 0
#return m3


#####################################################
# Menu for Security Level
#####################################################
def menu_security():
    global numChar
    numChar = int(input('How long you want your password(s) to be?: '))
    m2 = input("""A: Low (Just numbers)
B: Medium (Numbers and letters)
C: High (numbers, letters and symbols)
E: Exit
Please choose the level of security: """)

    if m2 == "A" or m2 == "a":
        low_sec()
    elif m2 == "B" or m2 == "b":
        medium_sec()
    elif m2 == "C" or m2 == "c":
        high_sec()
    elif m2 == "E" or m2 == "e":
        sys.exit()
    else:
        print('Invalid option, you must select either A, B, C or E')
        print('Please try again')
        menu_security()
#####################################################
#####################################################


#####################################################
# Main Menu
#####################################################
def menu():
    print()
    m1 = input("""+++++Main Menu+++++
A: Just give me a secure password now!
B: One Password (specific requirements)
C: Multiple passwords
E: Exit
Please enter your choice: """)

    if m1 == "A" or m1 == "a":
        simple_pass()
    elif m1 == "B" or m1 == "b":
        one_pass()
    elif m1 == "C" or m1 == "c":
        mul_pass()
    elif m1 == "E" or m1 == "e":
        sys.exit()
    else:
        print('Invalid option, you must select either A, B, C or E')
        print('Please try again')
        menu()
#####################################################
#####################################################


menu()
