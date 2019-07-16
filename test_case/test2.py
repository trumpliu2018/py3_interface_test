import unittest

def setUpModule():
    print('=== setUpModule ===')

def tearDownModule():
    print('=== tearDownModule ===')

class TestClass2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('--- setUpClass2 ---')

    @classmethod
    def tearDownClass(cls):  
        print('--- tearDownClass2 ---')
        
    def setUp(self):
        print('... setUp2 ...')
        
    def tearDown(self):
        print('... tearDown2 ...')
        
    def test_a2(self):
        print("a")
        
    def test_B2(self):
        print("B")


if __name__ == '__main__':
    unittest.main()