import unittest
from sort import sorting_stack as sort

class TestPackageSorting(unittest.TestCase):

    def test_standard_package(self):
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")
        self.assertEqual(sort(10, 10, 10, 1), "STANDARD")
    
    def test_bulky_package(self):
        """
        Package is bulky (volume >= 1,000,000 cm³ or any dimension >= 150 cm)
        """
        self.assertEqual(sort(200, 50, 50, 10), "SPECIAL")    # width
        self.assertEqual(sort(50, 200, 50, 10), "SPECIAL")    # height
        self.assertEqual(sort(50, 50, 200, 10), "SPECIAL")    # length
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")  # volume
    
    def test_heavy_package(self):
        """
        Package is heavy (mass >= 20 kg)
        """
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")    # heavy
        self.assertEqual(sort(100, 100, 80, 20), "SPECIAL")  # heavy

    def test_rejected_package(self):
        """
        Package is both bulky (volume >= 1,000,000 cm³) and heavy (mass >= 20 kg)
        """
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED") # bulky | heavy
        self.assertEqual(sort(150, 150, 150, 20), "REJECTED") # bulky | heavy

    def test_edge_cases(self):
        self.assertEqual(sort(99, 100, 100, 19), "STANDARD") 
        self.assertEqual(sort(100, 100, 100, 19), "SPECIAL")  # volume
        self.assertEqual(sort(150, 100, 100, 5), "SPECIAL")  # width
        self.assertEqual(sort(100, 150, 100, 5), "SPECIAL")  # height
        self.assertEqual(sort(100, 100, 150, 5), "SPECIAL")  # length
        self.assertEqual(sort(25, 25, 25, 25), "SPECIAL")  # heavy
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")  # bulky & heavy

if __name__ == '__main__':
    unittest.main()
