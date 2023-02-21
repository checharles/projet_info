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
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
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
    
    def add_edge(self, node1, node2, power_min, dist=1):
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

        nb_edges += 1 
    
    
    def get_path_with_power(self, src, dest, power):
        """this function determine the shortest path, if it exists, between two nodes possible with a certain
        power

        Parameters: 
        -----------

        src: NodeType
            source of path
        dest: NodeType
            destination of the path
        power :  numeric (int or float)
            power used to travel between the path
        """


        """ Check if there is a path between the source and destination nodes using connected_components_set"""

        path_exists = False
        
        for component in self.connected_components():
            if src in component and dest in component:
                path_exists = True
                break
        """if there is no path, the function return none"""    
        if not path_exists:
            return None
        
        
        """Create a set of unvisited nodes and initialize the distances to all nodes to infinity"""
        unvisited_nodes = set(self.graph.keys())
        distances = {node: float('inf') for node in unvisited}

        """Create a dictionary to keep track of the previous node in the shortest path"""
        previous_visited_nodes = {node: None for node in unvisited}
        
        distances[src] = 0
        

        """ the loop enable to visit every node with help of the Dikjstra algorythm"""
        while unvisited_nodes : 

            current_node = min(unvisited, key=distances.get)
            """If the distance to the current node is infinity, the algorythm end"""
            if distances[current_node] == float('inf'):
                break

            """  the current node is removed from the unvisited set and the destination is check"""
            unvisited.remove(current_node)

            """the algorythm is specialize to stop when the minimun distance between src and dest is find"""
            if current_node == dest:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = previous_visited_nodes[current_node]
                path.reverse()
            return path, distances[dest]

            """Check the distances to each neighbor of the current node and update 
            it is shorter than the previous distance """
            for neighbor, dist in self.graph[current_node]:
                 if dist <= power:
                    distance = distances[current_node] + dist
                
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous_visited_nodes[neighbor] = current_node

            return None

        return 

    

        




         
    def connected_components(self):

        """this function take a graph as an argument and return a list of  
        every connected nodes in the graph """

        """indicate the nodes visited during the search for the connected 
        component"""
    
        nodes_visited = list()

        """components is a list of , each list representing a component 
        (a set of nodes connected together, i.e a subgraph)"""
        components = list()
        
        """this function is a recursive function enabling depth-first search 
        (dfs). From a starting node, the function search if one of the neighbor 
        node is not visited. If such a node existed,the function visites it 
        and search again for a neighbor node not visited. 
        It goes as far as possible each branch and then do it again in an other 
        branch, until every path beginning with the node is completly visited"""

        def dfs_function(node, component):
            c
            component.add(node)
            for neighbor in self.graph[node]:
                if neighbor[0] not in nodes_visited:
                    dfs_function(neighbor[0], component)

        """ the dfs_function is now used in each node in order to visited the 
        whole graph and to discover every component."""

        for node in self.nodes:
            if node not in nodes_visited:
                component = []
                dfs_function(node, component)
                components.add(component)  
               
        return components 


    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        """the result components from connected_component is transform in a frozen set by the function"""
        
        set_components = set(frozenset(component) for component in components)
        return set_components
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        raise NotImplementedError


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
            nb_nodes, m_edge = map(int, file.readline().split()) 
            """the first line of the file is read to extract the number of edges and the number of nodes"""
            graph = [] 

            """creating the nodes for the graph as a list of nb_nodes elements """

            nodes = list(range(1, nb_nodes +1))
        
            """initializing G, a object from class Graph with nb_nodes nodes"""
            G = Graph(nb_nodes)

            for i in range(m_edges):
                line = f.readline().split()
                node1 = int(line[0])
                node2 = int(line[1])
                power_min = int(line[2])

                """checking if the distance is indicated, else default value is 1"""
                if len(line) == 4: 
                    dist = int(line[3])
                else:
                    dist = 1

                G.add_edge(node1, node2, power_min, dist)

        return G



            
        
        
    