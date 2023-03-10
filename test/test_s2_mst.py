# This will work if ran from the root folder.
import sys 
sys.path.append("/home/onyxia/projet_info/delivery_network")

from graph import graph_from_file, Graph
import unittest   # The test framework

data_path = "/home/onyxia/projet_info/"

class Test_MST(unittest.TestCase):
    def test_network00(self):
        g = graph_from_file(data_path + "input/network.00.in")
        g_mst = g.kruskal()
        mst_expected = {1: [(8, 0, 1), (2, 11, 1), (6, 12, 1)],
                        2: [(5, 4, 1), (3, 10, 1), (1, 11, 1)],
                        3: [(4, 4, 1), (2, 10, 1)],
                        4: [(3, 4, 1), (10, 4, 1)],
                        5: [(2, 4, 1), (7, 14, 1)],
                        6: [(1, 12, 1)],
                        7: [(5, 14, 1)],
                        8: [(1, 0, 1), (9, 14, 1)],
                        9: [(8, 14, 1)],
                        10: [(4, 4, 1)]}
        self.assertEqual(g_mst.graph, mst_expected)

    def test_network05(self):
        g = graph_from_file(data_path +"input/network.05.in")
        g_mst = g.kruskal()
        mst_expected = {1: [(3, 2, 1), (4, 4, 1), (2, 6, 1)],
                        2: [(1, 6, 1)],
                        3: [(1, 2, 1)],
                        4: [(1, 4, 1)],
                        }
        self.assertEqual(g_mst.graph, mst_expected)

if __name__ == '__main__':
    unittest.main()
