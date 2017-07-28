'''
Author: Brian Peterson | https://github.com/brianpeterson28
Creative Exercise 1.2.21 - Intro to Programming In Python
'''
import math
import decimal

print("Calculates Future Value @ Continuously Compounded Rate.")

def askForInterestRate():
	while True:
		try:
			interestrate = float(input("Enter interest rate: "))
			while (interestrate >= 1) or (interestrate < 0):
				print("Please enter the interest rate as a decimal greater than zero but less than one.")
				interestrate = float(input("Enter interest rate: "))
			break
		except ValueError:
				print("That input is not valid.")
				print("Please enter the interest rate as a decimal greater than zero but less than one.")
	return interestrate

def askForYears():
	while True:
		try:
			years = int(input("Enter number of years: "))
			while (years < 0) or (type(years) != type(1)):
				print("The number of years must be an integer greater than zero.")
				years = int(input("Enter number of years:"))
			break
		except ValueError:
			print("That is not a valid entry.")
			print("Please enter the number of years as a non-negative integer.")
	return years

def askForPrincipal():
	while True:
		try:
			principal = float(input("Enter amount of principal: "))
			while principal <= 0:
				print("The principal amount must be greater than zero.")
				principal = float(input("Enter amount of principal: "))
			break
		except ValueError:
			print("That is not a valid entry.")
			print("Please enter a principal amount that is greater than zero.")
			print("Also, please do not include any commas.")
	return principal

def calculateFutureValue(interestrate, years, principal):
	futureValue = principal * (math.exp(interestrate * years))
	return futureValue

'''
Excellent article explaining how to use decimal package
to do math with and round floating point numbers:
https://pymotw.com/3/decimal/
'''
def displayResult(futurevalue):
	futurevalue = decimal.Decimal(futurevalue)
	print("The future value is ${:,.2f}.".format(futurevalue))

def main():
	principal = askForPrincipal()
	years = askForYears()
	inerestRate = askForInterestRate()
	futurevalue = calculateFutureValue(inerestRate, years, principal)
	displayResult(futurevalue)

if __name__ == "__main__":
	main()
