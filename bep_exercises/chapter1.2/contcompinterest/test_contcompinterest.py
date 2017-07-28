'''
Author: Brian Peterson | https://github.com/brianpeterson28
Pytest Tests for Creative Exercise 1.2.21 - Intro to Programming In Python
'''

import contcompinterest as cci
import decimal

def test_calculateFutureValue():
	fv = cci.calculateFutureValue(0.1, 10, 100)
	fv = decimal.Decimal(fv)
	fv = "{:,.2f}".format(fv)
	assert fv == "271.83"

	fv = cci.calculateFutureValue(0.1, 5, 100000)
	fv = decimal.Decimal(fv)
	fv = "{:,.2f}".format(fv)
	assert fv == "164,872.13"
