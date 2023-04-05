# This will work if ran from the root folder.

"""this function test the function search_parent in a tree created by Graph.kruskal """

import sys 
sys.path.append("/home/onyxia/projet_info/delivery_network")

from graph import Graph, graph_from_file
import unittest   # The test framework

data_path = "/home/onyxia/projet_info/"

class Test_find_parent(unittest.TestCase):

    def test_network1(self):
        g = graph_from_file(data_path + "input/network_importation/network.1.in")
        g_mst = g.kruskal()
        depths, parents = Graph.search_parent(g_mst)
        self.assertEqual(Graph.find_path_with_distance(parents, depths, 6, 11)[0],[6, 17, 20, 8, 11])
        self.assertEqual(Graph.find_path_with_distance(parents, depths, 6, 11)[1],15) 
        self.assertEqual(Graph.find_path_with_distance(parents, depths, 6, 11)[2],27235.0) 
        self.assertEqual(Graph.find_path_with_distance(parents, depths, 13, 20)[0],[13, 2, 1, 8, 20])
        self.assertEqual(Graph.find_path_with_distance(parents, depths, 13, 20)[1],13)
        self.assertEqual(Graph.find_path_with_distance(parents, depths, 13, 20)[2],22931.0) 


if __name__ == '__main__':
    unittest.main()