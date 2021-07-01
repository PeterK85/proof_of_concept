import sys
sys.path.append('../src')
import astro
import unittest

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2+3, 5)
    def test_2(self):
        self.assertEqual(astro.test_func(0), 85)
    def test_fail(self):
        self.assertEqual(astro.test_func(0), 0)


if __name__ == "__main__":
    unittest.main()
