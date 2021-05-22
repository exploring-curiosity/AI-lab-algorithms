from collections import defaultdict
import heapq

class node:
    def __init__(self, state, parent=None, hc=True):
        self.state = state
        self.parent = parent
        self.h = self.heurestic(state)
        if self.parent == None:
            self.g = 0
        else:
            self.g = parent.g + 1
        if hc == False:
            self.f = self.h
        else:
            self.f = self.g + self.h

    def __lt__(self, z):
        if self.f == z.f:
            return self.g < z.g
        return self.f < z.f

    def heurestic(self, st):
        dist = 0
        for i in range(len(self.state)):
            for j in self.state:
                if j != i:
                    dist += 1
        return dist


class puzzle:
    def __init__(self):
        self.states = defaultdict(list)

    def addEdge(self, u, v):
        self.states[u].append(v)

    def Greedy_BFS(self, start, goal):

        frontier = []
        explored = set()
        visited = set()

        heapq.heappush(frontier, node(start, hc=False))
        visited.add(start)

        while frontier:
            n = heapq.heappop(frontier)

            if tuple(n.state) in explored:
                continue

            explored.add(n.state)

            if n.state == goal:
                res = n
                l = len(visited)
                return res, l

            for i in next_states(n.state):
                if i not in visited:
                    z = node(i, n, hc=False)
                    heapq.heappush(frontier, z)
                    visited.add(i)
                elif i not in explored:
                    z = node(i, n, hc=False)
                    heapq.heappush(frontier, z)

        return None, None

    def A_star(self, start, goal):

        frontier = []
        explored = set()
        visited = set()
        f = 0
        heapq.heappush(frontier, node(start))
        visited.add(start)

        while frontier:
            n = heapq.heappop(frontier)

            if n.state in explored:
                continue

            explored.add(n.state)

            if n.state == goal:
                res = n
                l = len(visited)
                return res, l

            for i in next_states(n.state):
                if i not in visited:
                    z = node(i, n)
                    heapq.heappush(frontier, z)
                    visited.add(i)
                elif i not in explored:
                    z = node(i, n)
                    heapq.heappush(frontier, z)

        return None, None

    def traceback(self, res):
        x = list()

        while True:
            x.append(res.state)
            if (res.parent == None):
                break
            res = res.parent
        x.reverse()
        print(x)


def next_states(state):
    next_state = []
    for l in range(len(state)):
        for r in range(l + 1, len(state) + 1):
            s = list(state[l:r])
            o = list([x for x in state])

            for i in range(r - 1, l - 1, -1):
                o.pop(i)

            for i in range(len(o) + 1):
                n = o[:i] + s+ o[i:]

                if n != list(state) and tuple(n) not in next_state:
                    next_state.append(tuple(n))
    return next_state


puz = puzzle()
print("NOTE : Enter 0 for empty space")
s = tuple(map(int, input("Start State > ").split(" ")))
e = tuple(map(int, input("End State > ").split(" ")))
#s = (2, 1, 4, 5, 3, 6)
#e = (1, 2, 3, 4, 5, 6)
q = set()
q.add(s)
while len(q) != 0:
    x = q.pop()
    for i in next_states(x):
        puz.addEdge(x, i)
        if i not in puz.states.keys():
            if i not in q:
                q.add(i)
'''
print(next_states(list(s)))
print(next_states([3,4,5,1,2]))
'''
print("\nInformed Greedy Best First Search")
r, l = puz.Greedy_BFS(s, e)

puz.traceback(r)
print("Discovered States:", l)
print("\nInformed A* Search")
r, l = puz.A_star(s, e)

puz.traceback(r)
print("Discovered States:", l)

'''
OUTPUT
"F:\SEM 5\AIlab\venv\Scripts\python.exe" "F:/SEM 5/AIlab/cat4.py"
NOTE : Enter 0 for empty space
Start State > 2 4 1 5 3 6
End State > 1 2 3 4 5 6

Informed Greedy Best First Search
[(2, 4, 1, 5, 3, 6), (1, 2, 4, 5, 3, 6), (1, 2, 3, 4, 5, 6)]
Discovered States: 672

Informed A* Search
[(2, 4, 1, 5, 3, 6), (1, 2, 4, 5, 3, 6), (1, 2, 3, 4, 5, 6)]
Discovered States: 672

'''