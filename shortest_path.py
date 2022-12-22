
class path():
    def __init__(self,vertices):
        self.N=vertices
        self.graph=[[0 for col in range(vertices)] for row in range(vertices)]
    def print_ans(self,src,value,des,parent):
        print("minimum cost from "+str(src)+" to "+str(des)+" is :",value[des])
    def min_distance(self, value, parent):
        min = 1e7
        for i in range(self.N):
            if value[i] < min and  parent[i] == False:
                min = value[i]
                min_index = i
        return min_index
    def dijkstra(self, src,des):
        value = [1e7] * self.N
        value[src] = 0
        parent = [False] * self.N
        for cout in range(self.N):
            u = self.min_distance(value, parent)           
            parent[u] = True         
            for v in range(self.N):
                if (self.graph[u][v] > 0 and
                    parent[v] == False and
                   value[v] > value[u] + self.graph[u][v]):
                    value[v] = value[u] + self.graph[u][v]
        self.print_ans(src,value,des,parent)
g = path(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
g.dijkstra(5,8)