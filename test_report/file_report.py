import unittest

suite = unittest.defaultTestLoader.discover("./")

with open("result.txt","w") as f:
    unittest.TextTestRunner(stream=f,verbosity=2).run(suite)