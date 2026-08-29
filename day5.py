class Graph:
    def __init__(self):
        self.graph = {}
    def Addvertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print(f"Vertex {vertex} already exists.")
    def AddEdge(self, vertex1, vertex2,isDirected=False):
       self.Addvertex(vertex1)
       self.Addvertex(vertex2)
       self.graph[vertex1].append(vertex2)
       if not isDirected:
            self.graph[vertex2].append(vertex1)
    def Display(self):
        for key,values in self.graph.items():
            print(key, "======>", values) 
    def remove(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for key in self.graph:
                if vertex in self.graph[key]:
                    self.graph[key].remove(vertex)
    def isedgeexist(self,vertex1,vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            return True
        return False                
    def removeEdge(self,vertex1,vertex2):
       if self.isedgeexist(vertex1,vertex2):
            if vertex1 in self.graph:
                self.graph[vertex1].remove(vertex2)
            if vertex2 in self.graph:    
                self.graph[vertex2].remove(vertex1)
       else:
            print("edge does not exist")        
    def dfstraversal(self,start,visited=set()):
        visited.add(start)
        print(start,end=" ")
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfstraversal(neighbor, visited)
    def bfstraversal(self,start):
        visited={start}
        queue=[start]
        while queue:
            current=queue.pop(0)
            print(current,end=" ")
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    def shortestpath(self,start,end):#("A","D")
        visited={start}#{"A"}
        queue=[(start,[start])]#[("A",["A"])]
        while queue:
            current, path = queue.pop(0)
            if current == end:
                return path
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None                            
g=Graph()
g.AddEdge("A","B")
g.AddEdge("A","C")
g.AddEdge("B","D")
g.AddEdge("C","D")
g.Display()
# print("graph after removing vertex C:")
# g.remove("C")
# g.removeEdge("A","B")
# print("graph after removing edge A-B:")
# print("DFS traversal starting from vertex A:")
# g.dfstraversal("A")
# print("\nBFS traversal starting from vertex A:")
# g.bfstraversal("A")
print("\nShortest path from A to D:")
path = g.shortestpath("A", "D")
if path:
    print(" -> ".join(path))
else:
    print("No path found.")
g.Display()
