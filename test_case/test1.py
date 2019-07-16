import unittest

def setUpModule():
    print('=== setUpModule ===')

def tearDownModule():
    print('=== tearDownModule ===')

class TestClass1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('--- setUpClass ---')

    @classmethod
    def tearDownClass(cls):  
        print('--- tearDownClass ---')
        
    def setUp(self):
        print('... setUp ...')
        
    def tearDown(self):
        print('... tearDown ...')
        
    def test_a(self):
        print("a")
        
    def test_B(self):
        print("B")


if __name__ == '__main__':
    unittest.main()