import math
import log

# change

class ImaginaryValueException(Exception):
	"Thrown when result of a mathematical computation is not purely real"
	def __init__(self, message="The result of this mathematical computation is not purely real"):
		self.__name__ = "ImaginaryValueException"
		super().__init__(message)

class OutOfDomainException(Exception):
	"Thrown when input value is outside the function domain"
	def __init__(self, message="The input value is outside function domain"):
		self.__name__ = "OutOfDomainException"
		super().__init__(message)

class InvalidOperationException(Exception):
	"Thrown when an invalid input is given on the calculator menu"
	def __init__(self):
		self.__name__ = "InvalidOperationException"

def sqrt(num):
	if  num < 0:
		raise ImaginaryValueException
	return math.sqrt(num)

def fact(num):
	num = int(num)
	if num < 0:
		raise OutOfDomainException
	return math.factorial(num)

def natlog(num):
	if num <= 0:
		raise OutOfDomainException
	return math.log(num)

def poww(num, exp):
	if num == 0 and exp == 0:
		raise OutOfDomainException
	return num ** exp

ops = [sqrt, fact, natlog, poww]
opnames = ["SquareRoot", "Factorial", "NaturalLog", "Power"]

def main():
	logger = log.Logger(mode="FILE", filepath="./log.log")
	menuString = """
		(1) Square Root
		(2) Factorial
		(3) Natural Log
		(4) Power
	"""
	print(menuString)

	choice = int(input())

	try:
		if not (choice > 0 and choice < 5): raise InvalidOperationException

		num = input("Num: ")

		logger.info(opnames[choice - 1])

		if choice == 4:
			exp = input("Exp: ")

			print(poww(float(num), float(exp)))

		else: print(ops[choice - 1](float(num)))
	except Exception as e:
		print(e)
		logger.err(e.__name__)

if __name__ == '__main__':
	while True: main()
