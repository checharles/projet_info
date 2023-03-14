class Graph:
    """
    A class representing graphs as adjacency lists and implementing various 
    algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, 
        float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor2, p2, d2), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    

    def add_edge(self, node1, node2, power_min, dist):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is 
        added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """

        """Check if the nodes exist in the graph, if not, add them to the 
        nodes list"""

        """check if the first node exist and add it if not"""
        if node1 not in self.nodes: 
            """add the node"""
            self.nodes.append(node1) 
            self.graph[node1] = []
        
        """Same but for the second node"""
        if node2 not in self.nodes:
            self.nodes.append(node2)
            self.graph[node2] = []
        

        """Add the edge to the adjacency list of node1 and node2"""
        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))

           
    def get_path_with_power(self, src, dest, power):
        """this function determine a path, if it exists, between two nodes 
        possible with a certain power using a depth-first search.

        Parameters: 
        -----------

        src: NodeType
            source of path
        dest: NodeType
            destination of the path
        power :  numeric (int or float)
            power used to travel between the path

        Outputs : 
        -----------
        path : list
            a list of node to travel to src from dest
        dist : int
            the lenght of the path in distance
        """
        
        """ Check if there is a path between the source and destination nodes, using connected_components_set"""

        path_exists = False
        
        for component in self.connected_components_set():
            if src in component and dest in component:
                path_exists = True
                break
        """if there is no path, the function return none"""    
        if path_exists is False:
            return None

        visited_node = {node :False for node in self.nodes}
        visited_node[src] = True
        def search_path(node, path):
            if node == dest:
                return path
            for neighbor in self.graph[node]:
                neighbor, power_min, dist = neighbor
                if not visited_node[neighbor] and power_min <= power:
                    visited_node[neighbor] = True
                    result = search_path(neighbor, path+[neighbor])
                    if result is not None:
                        return result
            
        return search_path(src, [src])


    def get_short_path_with_power(self, src, dest, power):
        """this function determine the shortest path, if it exists, between two nodes, 
        possible with a certain power. It use the Dijkstra algorithm.

        Parameters: 
        -----------
        self: GraphType
              a graph
        src: NodeType
            source of path
        dest: NodeType
            destination of the path
        power : numeric (int or float)
            power used to travel between the path

        Outputs : 
        -----------
        path : list
            a list of node to travel to src from dest
        distances[dest] : int
            the lenght of the path in distance
        """


        """ Check if there is a path between the source and destination nodes using connected_components_set"""

        path_exists = False
        
        for component in self.connected_components_set():
            if src in component and dest in component:
                path_exists = True
                break
        """if there is no path, the function return none"""    
        if path_exists is False:
            return None
        
        
        """Create a set of unvisited nodes and initialize the distances to all nodes to infinity"""
        unvisited_nodes = set(self.graph.keys())
        distances = {node: float('inf') for node in unvisited_nodes}

        """Create a dictionary to keep track of the previous node in the shortest path to a node"""
        previous_visited_nodes = {node: None for node in unvisited_nodes}
        
        """Initialization of the distance and of the path"""
        distances[src] = 0
        path = []

        """ the loop enable to visit every node with help of the Dijkstra algorithm"""
        while unvisited_nodes: 
            
            current_node = min(unvisited_nodes, key=distances.get)
            """If the distance to the current node is infinity, the algorithm end"""
            if distances[current_node] == float('inf'):
                break

            """  the current node is removed from the unvisited set and the destination is check"""
            unvisited_nodes.remove(current_node)
            
            """the algorithm is specialize to stop when the minimun distance between src and dest is find"""
            if current_node == dest:
            
                while current_node is not None:
                    path.append(current_node)
                    current_node = previous_visited_nodes[current_node]
                path.reverse()

                lenght_path = distances[dest]
                return path

            """Check the distances to each neighbor of the current node and update 
            it is shorter than the previous distance """
            for neighbor in self.graph[current_node]:
                if neighbor[1] <= power:
                    distance = distances[current_node] + neighbor[2]
                
                    if distance < distances[neighbor[0]]:
                        distances[neighbor[0]] = distance
                        previous_visited_nodes[neighbor[0]] = current_node
                        
         
    def connected_components_set(self):

        """this function take a graph as an argument and return a list of  
        every connected nodes in the graph

        Parameters : 
        -----------
        self : GraphType

        Outputs : 
        -----------
        set_components : a set of frozensets
            a set of frozensets of connecting components
                """

        """indicate the nodes visited during the search for the connected 
        component"""
    
        nodes_visited = list()

        """components is a list of, each list representing a component 
        (a set of nodes connected together, i.e a subgraph)"""
        components = list()
    

        def dfs_function(node, component):
            """this function is a recursive function enabling depth-first search 
        (dfs). From a starting node, the function search if one of the neighbor 
        node is not visited. If such a node existed,the function visites it 
        and search again for a neighbor node not visited. 
        It goes as far as possible each branch and then do it again in an other 
        branch, until every path beginning with the node is completly visited
        """
            component.append(node)

            for neighbor in self.graph[node]:
                if neighbor[0] not in nodes_visited:
                    nodes_visited.append(neighbor[0])
                    dfs_function(neighbor[0], component)

        """ the dfs_function is now used in each node in order to visited the 
        whole graph and to discover every component."""

        for node in self.nodes:
            if node not in nodes_visited:
                component = []
                dfs_function(node, component)
                components.append(component)  
               
        set_components = set(frozenset(component) for component in components)
        return set_components


        
    def max_power_graph(self):
        """this function finds the maximun power of an edge in the whole graph
        

        Parameters : 
        -----------
        self : GraphType

        Outputs : 
        -----------
        power_max : int
            the maximun power find in a graph
        """
        
        power_max = float('-inf')

        for node in self.nodes:
            for neighbor in self.graph[node]: 
                power_max = max(power_max, neighbor[1]) 
        return power_max


    def min_power(self, src, dest):
        """This function uses binary research to find the minimun power needed to travel between 
        two nodes, called src and dest.
        
        Parameters : 
        -----------
        src: NodeType
            First end (node) of the path
        dest: NodeType
            Second end (node) of the path
        self: GraphType
            the graph studied

        Outputs: 
        -----------
        path: a list of nodes
            indicate the nodes in the order they are visited to travel between src and dest

        power_needed : integer
            the minimum power needed to be enable to travel between the node src and the node dest.
        """

        power_max = self.max_power_graph()

        if self.get_short_path_with_power(src, dest, power_max) is None:
            return None

        power_min = 0
        power_needed = power_max 

        path = self.get_short_path_with_power(src, dest, power_needed)

        while power_max - power_min > 1:
            
            if path is None:
                power_min = power_needed
            else:
                power_max = power_needed

            power_needed = (power_max + power_min) //2

            path = self.get_short_path_with_power(src, dest,power_needed )
        
        power_needed = power_needed + 1
        path = self.get_short_path_with_power(src, dest,power_needed )

        return path, power_needed

      

     
    def kruskal(self):
        """Returns the minimum spanning tree of the graph, with the help of the Kruskal algorithm.
            
            Parameters : 
            -----------
            self : GraphType

            Output :
            -----------
            g_mst : GraphType
                the minimun spanning tree from self
            
            """
        
        """importation of the UnionFind structure"""
        from Unionfind import UnionFind

        uf = UnionFind(self.nb_nodes)
        
        edges = [(power, src, dest, dist) for src in self.nodes for dest, power, dist in self.graph[src] if src < dest]
        edges.sort()

        mst = Graph(self.nodes)
        for power, src, dest, dist in edges:
            """find the sets that contain src and dest"""
            src_set = uf.find(src)
            dest_set = uf.find(dest)
            if src_set != dest_set:
                mst.add_edge(src, dest, power, dist)
                uf.union(src_set, dest_set)
        
        return mst

    def min_power_greedy(self, src, dest):
        """this function find the minimun power needed to travel from src to dest using the minimun spanning 
        tree of self
        Be aware that this function is only efficient if the graph is a tree

        Parameters : 
        -----------
        src  : NodeType
            the source node of the traject
        dest : NodeType
            the destination node of the traject
        
        Outputs:
        -----------
        path: list
            the list contains the node to travel from src and dest
        min_power: int
            the minimun power to the travel along the path


        """

        visited_node = {node :False for node in self.nodes}
        def search_path_with_power(node, path, min_power):

            visited_node[node] = True
            if node == dest:
                return path, min_power
                
            for neighbor in self.graph[node]:
                node_neighbor, power_min, dist = neighbor
                if visited_node[node_neighbor] is False :
                    min_power = max(min_power, power_min )
                    result = search_path_with_power(node_neighbor, path+[node_neighbor], min_power)
                    if result is not None:
                        return result
            
        return search_path_with_power(src, [src], 0)



    def search_parent(self):
        """This function finds the parents in a graph and the depth of each node in the graph
        

        Outputs :
        -----------
        parents: dict
            A dictionary of parents for each node.
        depths: dict
            A dictionary of depths for each node.
        """
        parents = {}
        depths = {node: 0 for node in self.nodes}
        visited_node = {node: False for node in self.nodes}

        def search_parent_dfs(node, depth, depths, parents):
            visited_node[node] = True
            depths[node] = depth
            for neighbor, power, dist in self.graph[node]:
                if not visited_node[neighbor]:
                    parents[neighbor] = (node, power)
                    search_parent_dfs(neighbor, depth + 1, depths, parents)

        search_parent_dfs(1, 0, depths, parents)
        return depths, parents


    def find_path(parents, depths, src, dest):
        """
        Finds the path between two nodes given their depths and the dictionary of parents.

        Parameters:
        -----------
        parents: dict
            A dictionary of parents for each node.
        depths: dict
            A dictionary of depths for each node.
        src: NodeType
            First node.
        dest: NodeType
            Second node.

        Outputs:
        -----------
        list
            A list of nodes representing the path from node1 to node2, including node1 and node2.
            If no path exists, returns an empty list.
        """


        node1 = src
        node2 = dest
        path_1 = [node1]
        path_2 = [node2]
        min_power_1 = 0
        min_power_2 = 0
        """Compare the depths of the two nodes and go up the tree until they have the same depth"""

        while depths[node1] > depths[node2]:
            node1 = parents[node1][0]
            path_1.append(node1)
            if node1 != 1:
                min_power_1 = max(min_power_1, parents[node1][1])


        while depths[node2] > depths[node1]:
            node2 = parents[node2][0]
            path_2.append(node2)
            if node1 != 1:
                min_power_2 = max(min_power_2, parents[node2][1])

            


        """Go up the tree from both nodes until a common ancestor is found"""
        
        while node1 != node2:
            node1 = parents[node1][0]
            node2 = parents[node2][0]
            path_1.append(node1)
            if node1 != 1:
                min_power_1 = max(min_power_1,parents[node1][1])

            if node1 != node2 and node2 != 1:
                path_2.append(node2)
                min_power_2 = max(min_power_2,parents[node2][1])


        """Reverse the path to get it from node1 to node2"""
        
        path_2.reverse()
        path = path_1 + path_2
        min_power = max(min_power_1, min_power_2)

        

        return path, min_power


    def display_graph(self):

        """
        This function displays a graph with the help of the graphviz module.

        Parameters : 
        ------------

        self : GraphType
            the graph used
        Outputs : 
        ------------
        a png file containing the graph
        """
        import graphviz
        
        dot = graphviz.Graph()
    
        """add node"""
        for node in self.nodes:
            dot.node(str(node))
    
        """add edge"""
        edges = set()

        for node in self.nodes:
            for neighbor in self.graph[node]:
                edge = tuple(sorted([node, neighbor[0]])) 
                if edge not in edges: 
                    edges.add(edge)
                    dot.edge(str(edge[0]), str(edge[1]), label=str(neighbor[1]))
                    
        """display of the graph"""
        print("voila le graphe au formart png")
        dot.render('graph G.png', format='png', view=True)
        dot.view()
        return dot


    def display_path(self, dest, src) : 
        """this function displays the shortest path between the node src and the node dest
        
        Parameters : 
        ------------
        src : NodeType
            the source node of the travel

        dest : NodeType
            the destination node of the travel

        self : GraphType

        Outputs : 
        ------------
        a png file containing the graph
        """

        graph_with_path = self.display_graph()

        travel = self.min_power(dest, src)

        if travel is None:
            return None

        for i in range(0, len(travel[0]) - 1):
            edge = tuple(sorted([travel[0][i], travel[0][i+1]]))
            graph_with_path.edge(str(edge[0]), str(edge[1]), color='blue')
            graph_with_path.node(str(travel[0][i]), color='blue', style='filled')

        graph_with_path.node(str(travel[0][-1]), color='blue', style='filled')
        
        """display of the graph"""
        graph_with_path.render('path in the graph G', format='png', view=True)




def graph_from_file(filename):
        """
        Reads a text file and returns the graph as an object of the Graph class.

        The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

        Parameters: 
        -----------
        filename: str
            The name of the file

        Outputs: 
        -----------
        G: Graph
            An object of the class Graph with the graph from file_name.
        """

        with open(filename, 'r') as file:

            nb_nodes, m_edges = map(int, file.readline().split()) 
            """the first line of the file is read to extract the number of edges and the number of nodes"""
        
            """creating the nodes for the graph as a list of nb_nodes elements """
            nodes = list(range(1, nb_nodes + 1))
        
            """initializing G, a object from class Graph with nb_nodes nodes"""
            G = Graph(nodes)
            G.nb_edges = m_edges

            for i in range(m_edges):
                line = file.readline().split()
                node1 = int(line[0])
                node2 = int(line[1])
                power_min = int(line[2])

                """checking if the distance is indicated, else default value is 1"""
                if len(line) == 4: 
                    dist = float(line[3])
                else:
                    dist = 1

                G.add_edge(node1, node2, power_min, dist)

        G.file = filename

        return G
