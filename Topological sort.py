from collections import defaultdict


class Graph(object):

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    # 그래프에 에지 추가
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[u].sort(reverse=True)

    # 위상 정렬
    def topologicalSort(self):
        # 처음 차수는 0으로 초기화
        in_degree = [0] * self.V

        # 차수를 업뎃해준다
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # 차수가 0인 정점을 넣는다
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # 방문한 정점의 개수
        count = 0

        # 결과 출력용
        top_order = []

        # 차수가 0이 되는 정점을 순서대로 pop한다
        while queue:
            u = queue.pop(0)
            top_order.append(u)

            # pop한 정점과 인접한 정점의 차수를 -1해준다
            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

            count += 1

        for i in range(n):
            print(top_order[i], end=" ")

n = int(input())
m = int(input())
g = Graph(n)

for i in range(m):
    (a, b) = tuple([int(x) for x in input().split()])
    g.addEdge(a, b)

g.topologicalSort()
