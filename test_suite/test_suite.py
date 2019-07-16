import unittest
from test_case import test1
from test_case import test2 

suite = unittest.TestSuite()
suite.addTest(test1.TestClass1('test_a'))
suite.addTests([test2.TestClass2('test_a2'), test2.TestClass2('test_B2')])

unittest.TextTestRunner(verbosity=2).run(suite)