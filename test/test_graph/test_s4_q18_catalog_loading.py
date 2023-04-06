# This will work if ran from the root folder.
import sys 
sys.path.append("/home/onyxia/projet_info/delivery_network")

import unittest 
from graph import catalog_from_file

data_path = "/home/onyxia/projet_info/"

class Test_CatalogLoading(unittest.TestCase):
    def test_trucks0(self):
        c = catalog_from_file(data_path + "input/trucks.0.in")
        self.assertEqual(len(c), 2)
        self.assertEqual((2000000, 200000) in c, True)

    def test_trucks1(self):
        c = catalog_from_file(data_path + "input/trucks.1.in")
        self.assertEqual(len(c), 19)
        self.assertEqual((2500000, 370000) not in c, True)
        self.assertEqual((3000000, 360000) in c, True)

    def test_trucks2(self):
        c = catalog_from_file(data_path + "input/trucks.2.in")
        self.assertEqual((3000, 365) not in c, True)
        self.assertEqual((4000, 220) in c, True)
    
    def test_trucks_perso(self):
        c = catalog_from_file(data_path + "input/trucks.testperso.in")
        self.assertEqual(len(c), 2)
        self.assertEqual((1500000, 170000) in c, True)

if __name__ == '__main__':
    unittest.main()