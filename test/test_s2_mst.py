# This will work if ran from the root folder.
"""This function tests the kruskal methode for the class Graph"""
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

    def test_network01(self):
        g = graph_from_file(data_path +"input/network.05.in")
        g_mst = g.kruskal()
        mst_expected = {1: [(3, 2, 1), (4, 4, 1), (2, 6, 1)],
                        2: [(1, 6, 1)],
                        3: [(1, 2, 1)],
                        4: [(1, 4, 1)],
                        }
        self.assertEqual(g_mst.graph, mst_expected)


    def test_network02(self):
        g = graph_from_file(data_path +"input/network.04.in")
        g_mst = g.kruskal()
        mst_expected = {1: [(2, 4, 89)],
                        2: [(1, 4, 89), (3, 4, 3)],
                        3: [(2, 4, 3), (4, 4, 2)],
                        4: [(3, 4, 2)],
                        5: [],
                        6: [],
                        7: [],
                        8: [],
                        9: [],
                        10: [],
                        }
        self.assertEqual(g_mst.graph, mst_expected)

    def test_network1(self):
        g = graph_from_file(data_path + "input/network.1.in")
        g_mst = g.kruskal()
        mst_expected = {1: [(2, 2, 6312.0), (5, 2, 1209.0), (14, 11, 231.0), (8, 13, 5452.0)],
                        2: [(1, 2, 6312.0), (3, 5, 6891.0), (13, 8, 7816.0)],
                        3: [(2, 5, 6891.0)],
                        4: [(12, 5, 4713.0), (8, 8, 7291.0)],
                        5: [(1, 2, 1209.0)],
                        6: [(17, 15, 9883.0)],
                        7: [(16, 13, 1315.0), (14, 15, 4757.0)],
                        8: [(11, 1, 8542.0), (4, 8, 7291.0), (20, 11, 3351.0), (1, 13, 5452.0)],
                        9: [(12, 9, 3330.0)],
                        10: [(16, 37, 4618.0)],    
                        11: [(8, 1, 8542.0)],
                        12: [(4, 5, 4713.0), (9, 9, 3330.0)],
                        13: [(19, 1, 5082.0), (2, 8, 7816.0)],
                        14: [(1, 11, 231.0), (7, 15, 4757.0)],
                        15: [(19, 27, 3013.0)],
                        16: [(7, 13, 1315.0), (10, 37, 4618.0)],
                        17: [(18, 11, 8087.0), (20, 14, 5459.0), (6, 15, 9883.0)],
                        18: [(17, 11, 8087.0)],
                        19: [(13, 1, 5082.0), (15, 27, 3013.0)],
                        20: [(8, 11, 3351.0), (17, 14, 5459.0)],
                        }
        self.assertEqual(g_mst.graph, mst_expected)

    

if __name__ == '__main__':
    unittest.main()
