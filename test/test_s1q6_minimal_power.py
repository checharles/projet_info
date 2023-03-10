# This will work if ran from the root folder.
import sys 
sys.path.append("/home/onyxia/projet_info/delivery_network")

from graph import graph_from_file
import unittest   # The test framework

data_path = "/home/onyxia/projet_info/"


class Test_MinimalPower(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file(data_path + "input/network.00.in")
        self.assertEqual(g.min_power(1, 4)[1], 11)
        self.assertEqual(g.min_power(2, 4)[1], 10)

    def test_network1(self):
        g = graph_from_file(data_path + "input/network.04.in")
        self.assertEqual(g.min_power(1, 4)[1], 4)

    def test_network2(self):
        g = graph_from_file(data_path + "input/network.03.in")
        self.assertEqual(g.min_power(1, 4)[1], 10)
        self.assertEqual(g.min_power(1, 4)[0], [1, 2, 3, 4])

    def test_network3(self):
        g = graph_from_file(data_path + "input/network.05.in")
        self.assertEqual(g.min_power(2, 4)[1], 6)
        self.assertEqual(g.min_power(5, 4), None)


if __name__ == '__main__':
    unittest.main()
