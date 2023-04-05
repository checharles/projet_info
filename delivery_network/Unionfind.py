"""this document define UnionFind, a type of data structure used in Kruskal algorithm"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)
    
    def find(self, x):
        """
        the function find the parent of the node x

        Parameter :
        -----------
        x: NodeType
            the studied node

        Outputs : 
        -----------
        parent[x] : NodeType
            the parent of x
        """

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """
        this function merges the set containing x with the set containing y

         Parameter :
        -----------
        x: NodeType
            the studied node
        y: NodeType
            the studied node
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
    
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y

        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
