'''
Author: Brian Peterson | github.com/brianpeterson28
Creative Exercise 1.2.22 - Intro to Programming In Python
'''
import sys
import math

BORDER_LENGTH = 75

def print_welcome_message():
    print("=" * BORDER_LENGTH)
    print("\t\t\tTHE WIND CHILL PROGRAM")
    print("=" * BORDER_LENGTH)
    print("")
    print("This program calculates the windchill given:")
    print("\t(1) Temperature (T in degrees Farenheit)")
    print("\t(2) Wind Speed (v in miles/hour)")
    print("")

def main():
    print_welcome_message()

if __name__ == '__main__':
    main()
