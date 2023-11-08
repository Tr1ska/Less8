import unittest
from deffff import*

class Test(unittest.TestCase):
    def add_positive(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def add_videmni(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def add_mix(self):
        result = add(-2, 3)
        self.assertEqual(result, 1)

if __name__ == "deffff":
    unittest.main()
