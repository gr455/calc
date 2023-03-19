import calc
import unittest
import math

class SqrtTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testPerfectSquare(self):
		assert calc.sqrt(4) == 2.0

	def testNonPerfectSquare(self):
		assert abs(calc.sqrt(5) - 2.236) < 0.01

	def testBadValue(self):
		self.assertRaises(calc.ImaginaryValueException, calc.sqrt, -5)


class FactTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testGoodValue(self):
		assert calc.fact(4) == 24.0

	def testBadValue(self):
		self.assertRaises(calc.OutOfDomainException, calc.fact, -4)

class NatLogTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testGoodValue(self):
		assert abs(calc.natlog(10) - 2.302) < 0.01

	def testE(self):
		assert calc.natlog(math.e) == 1

	def testBadValue(self):
		self.assertRaises(calc.OutOfDomainException, calc.natlog, 0)

class PowTest(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testGoodValues(self):
		assert calc.poww(2, 3) == 8.0

	def testBadValue(self):
		self.assertRaises(calc.OutOfDomainException, calc.poww, 0, 0)

if __name__ == '__main__':
	unittest.main()