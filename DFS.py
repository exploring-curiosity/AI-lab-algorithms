from collections import defaultdict


class graph:
    def __init__(self):
        self.states = defaultdict(list)

    def addEdge(self, u, v):
        self.states[u].append(v)

    def DFS(self,s):
        K = list(self.states.keys())
        stack = []
        visited = {}
        for i in K:
            visited[i] = False
        stack.append(s)
        visited[s] = True
        while len(stack) != 0:
            s = stack.pop(-1)
            print(s, end=" ")
            for i in self.states[s]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True
        print()


nodes = set()
dfs= graph()
n=int(input("Enter number of edges > "))
for i in range(n):
    x=input("Edge > ").split(" ")
    dfs.addEdge(x[0],x[1])
s=input("Enter Start State > ")
dfs.DFS(s)