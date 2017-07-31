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
    print("This program calculates the windchill temperature given:")
    print("\t(1) Temperature (T in degrees Farenheit)")
    print("\t(2) Wind Speed (v in miles/hour)")
    print("")

def get_temp():
    temperature = float(input("Enter Temperature: "))
    return temperature

def get_wind_speed():
    wind_speed = float(input("Enter Wind Speed: "))
    return wind_speed

def calculate_wind_chill(temperature, wind_speed):
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * math.pow(wind_speed, 0.16) + (0.4275 * temperature * math.pow(wind_speed, 0.16))
    return wind_chill

def main():
    print_welcome_message()
    temperature = get_temp()
    wind_speed = get_wind_speed()
    wind_chill = calculate_wind_chill(temperature, wind_speed)
    print("The wind chill temperature is {:.2f}".format(wind_chill))

    # T = 20, v = 30

if __name__ == "__main__":
    main()
