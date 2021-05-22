from collections import defaultdict


class cans:
    def __init__(self):
        self.states = defaultdict(list)

    def addEdge(self, u, v):
        self.states[u].append(v)

    def BFS(self, s):
        K = list(self.states.keys())
        visited = {}
        for i in K:
            visited[i] = False
        queue = []
        queue.append(s)
        visited[s] = True
        while len(queue) != 0:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.states[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        print()

    def sequence(self, start, goal):
        explored = []
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in explored:
                neighbours = self.states[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == goal:
                        return new_path, len(explored) + 1
            explored.append(node)
        return "SORRY CANT REACH GOAL STATE", len(explored)


def next_states(s):
    x = list()
    c8 = s[0]
    c5 = s[1]
    c3 = s[2]
    if (c8 == 8):
        s8 = "full"
    elif c8 == 0:
        s8 = "empty"
    else:
        s8 = "par"
    if (c5 == 5):
        s5 = "full"
    elif c5 == 0:
        s5 = "empty"
    else:
        s5 = "par"
    if (c3 == 3):
        s3 = "full"
    elif c3 == 0:
        s3 = "empty"
    else:
        s3 = "par"
    if (s8 != "full"):
        if (s5 != "empty"):
            a = c8 + c5
            b = 0
            if (a > 8):
                b = a - 8
                a = 8
            c = c3
            x.append((a, b, c))
        if (s3 != "empty"):
            a = c8 + c3
            c = 0
            if (a > 8):
                c = a - 8
                a = 8
            b = c5
            x.append((a, b, c))
    if (s5 != "full"):
        if (s8 != "empty"):
            b = c8 + c5
            a = 0
            if (b > 5):
                a = b - 5
                b = 5
            c = c3
            x.append((a, b, c))
        if (s3 != "empty"):
            b = c5 + c3
            c = 0
            if (b > 5):
                c = b - 5
                b = 5
            a = c8
            x.append((a, b, c))
    if (s3 != "full"):
        if (s5 != "empty"):
            c = c3 + c5
            b = 0
            if (c > 3):
                b = c - 3
                c = 3
            a = c8
            x.append((a, b, c))
        if (s8 != "empty"):
            c = c8 + c3
            a = 0
            if (c > 3):
                a = c - 3
                c = 3
            b = c5
            x.append((a, b, c))
    return x


decant = cans()
s = tuple(map(int, input("Start State > ").split(" ")))
e = tuple(map(int, input("End State > ").split(" ")))
queue = []
nodes=[s]
for i in next_states(s):
    decant.addEdge(s, i)
    queue.append(i)
    nodes.append(i)
while len(queue)!=0:
    x = queue.pop(0)
    for i in next_states(x):
        decant.addEdge(x, i)
        if i not in nodes:
            queue.append(i)
            nodes.append(i)
print("Breadth First Search Tracing :")
decant.BFS(s)
path, length = decant.sequence(s, e)
print("Shortest possible path found using BFS :")
print(path)
print("Number of explored Nodes : ", length)

'''
OUTPUT

Start State > 8 0 0
End State > 4 1 3
Breadth First Search Tracing :
(8, 0, 0) (3, 5, 0) (5, 0, 3) (3, 2, 3) (0, 5, 3) (5, 3, 0) (6, 2, 0) (2, 3, 3) (6, 0, 2) (2, 5, 1) (1, 5, 2) (7, 0, 1) (1, 4, 3) (7, 1, 0) (4, 4, 0) (4, 1, 3) 
Shortest possible path found using BFS :
[(8, 0, 0), (5, 0, 3), (5, 3, 0), (2, 3, 3), (2, 5, 1), (7, 0, 1), (7, 1, 0), (4, 1, 3)]
Number of explored Nodes :  38



'''