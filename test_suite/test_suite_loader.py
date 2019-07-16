import unittest
from test_case import test1


suite = unittest.TestLoader().loadTestsFromTestCase(test1.TestClass1)
unittest.TextTestRunner(verbosity=2).run(suite)