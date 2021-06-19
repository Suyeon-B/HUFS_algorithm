class Prims:
    def __init__(self,vertex):
        self.vertex = vertex
        self.data = [[0 for i in range(self.vertex)] for j  in range(self.vertex)]

    def AddAdges(self,src,dest,cost):
        if src == dest:
            print('same')
        else:
            self.data[src][dest] = cost
            self.data[dest][src] = cost

        return self.data

    def GetNeighbour(self,vertex):
        a = []
        for i in range(len(self.data[vertex])):
            if self.data[vertex][i] > 0:
                a.append(i)
        return a

    def weight(self,src,dest):
        return self.data[src][dest]

    def rasta(self,source):
        visited = []
        dct = {i:999999 for i in range(len(self.data))}
        dct[source] = 0
        temp = {i: dct[i] for i in dct}

        while temp:
            minNode = 99999
            key = None
            for i in temp:
                if temp [i] < minNode:
                    minNode = temp[i]
                    key = i
            temp.pop(key)
            if key not in visited:
                visited.append(key)
                x = self.GetNeighbour(key)
                for j in x:
                    if (self.weight(key,j)< dct[j]) and (j not in visited):
                        dct[j] = self.weight(key,j)
                        temp[j] = self.weight(key,j)
        print(sum(dct.values()))



n = int(input())
m = int(input())
g = Prims(n)
for i in range(m):
    (a, b, c) = tuple([int(x) for x in input().split()])
    g.AddAdges(a, b, c)

g.rasta(3)
