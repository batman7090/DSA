class Graph:
    def __init__(self):
        """Constructor for Graph class"""
        self.adj_list = {}
    
    def __str__(self):
        text = ''
        for vertex in self.adj_list:
            text += f"'{vertex}' : {self.adj_list[vertex]}\n"
        return text[:-1]

    def add_vertex(self, vertex):
        """Adding vertex to the Graph"""
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        """Adding vertex between node v1 and v2"""
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        """Removing the edge between v1 and v2"""
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, v1):
        """Removing vertex v1 from the graph"""
        if v1 in self.adj_list.keys():
            for other_vertex in self.adj_list[v1]:
                self.adj_list[other_vertex].remove(v1)
            del self.adj_list[v1]
            return True
        return False


if __name__ == '__main__':
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("A", "D")
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')

    g.remove_vertex("D")

    print(g)