from collections import defaultdict
import heapq


class node:
    def __init__(self, state, parent=None, hc=True):
        self.state = state
        self.parent = parent
        self.h = self.manhattan(state)
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

    def manhattan(self, st):
        m = 0
        for i in range(9):
            if st[i] == 0:
                continue
            m += abs(st[i] // 3 - i // 3) + abs(st[i] % 3 - i % 3)
        return m


class puzzle:
    def __init__(self):
        self.states = defaultdict(list)

    def addEdge(self, u, v):
        self.states[u].append(v)

    def uninformed(self, start, goal):
        explored = set()
        queue = [[start]]
        while queue:
            route = queue.pop(0)
            node = route[-1]

            if node not in explored:
                neighbours = self.states[node]
                for neighbour in neighbours:
                    new_path = list(route)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == goal:
                        return new_path, len(explored)
            explored.add(node)
        return "SORRY CANT REACH GOAL STATE", 0

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

    def traceback(self, res):
        x = list()

        while True:
            x.append(res.state)
            if (res.parent == None):
                break
            res = res.parent
        x.reverse()
        display(x, 1)


def next_states(state):
    v = list()
    empty = state.index(0)
    if empty == 4:
        for i in range(0, 4):
            temp = list(state[:])
            j = 2 * (i + 1) - 1
            temp[4], temp[j] = temp[j], temp[4]
            v.append(tuple(temp))
        return v
    elif empty % 2 == 1:
        temp = list(state[:])
        if empty == 1:
            temp[empty], temp[0] = temp[0], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            temp[empty], temp[2] = temp[2], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            temp[empty], temp[4] = temp[4], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            return v
        elif empty == 3:
            temp[empty], temp[0] = temp[0], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            temp[empty], temp[6] = temp[6], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            temp[empty], temp[4] = temp[4], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            return v
        elif empty == 5:
            temp[empty], temp[8] = temp[8], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            temp[empty], temp[2] = temp[2], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            temp[empty], temp[4] = temp[4], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            return v
        elif empty == 7:
            temp[empty], temp[8] = temp[8], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            temp[empty], temp[6] = temp[6], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            temp[empty], temp[4] = temp[4], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            return v
    else:
        temp = list(state[:])
        if empty == 0:
            temp[empty], temp[1] = temp[1], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            temp[empty], temp[3] = temp[3], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            return v
        elif empty == 2:
            temp[empty], temp[1] = temp[1], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            temp[empty], temp[5] = temp[5], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            return v
        elif empty == 6:
            temp[empty], temp[3] = temp[3], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            temp[empty], temp[7] = temp[7], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            return v
        elif empty == 8:
            temp[empty], temp[7] = temp[7], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            temp[empty], temp[5] = temp[5], temp[empty]
            v.append(tuple(temp))
            temp = list(state[:])
            return v


def display(l, flag):
    if flag == 0:
        print(l)
    else:
        for i in l:
            for j in range(9):
                if j % 3 == 0:
                    print()
                if i[j] == 0:
                    print(" ", end=" ")
                else:
                    print(i[j], end=" ")
            print()


puz = puzzle()
print("NOTE : Enter 0 for empty space")
# s = tuple(map(int, input("Start State > ").split(" ")))
# e = tuple(map(int, input("End State > ").split(" ")))
s = (7, 2, 4, 5, 0, 6, 8, 3, 1)
e = (0, 1, 2, 3, 4, 5, 6, 7, 8)

q = set()
q.add(s)
while len(q) != 0:
    x = q.pop()
    for i in next_states(x):
        puz.addEdge(x, i)
        if i not in puz.states.keys():
            if i not in q:
                q.add(i)
print("\nUninformed Breadth First search")
path, length = puz.uninformed(s, e)
if length >0:
    print("\n No of nodes Discovered : ",length)
    display(path, 1)
else:
    display(path, length)
print("\nInformed A* Search")
r, l = puz.A_star(s, e)
print("\n No of nodes Discovered : ",l)
puz.traceback(r)
print("\nInformed Greedy Best First Search")
r, l = puz.Greedy_BFS(s, e)
print("\n No of nodes Discovered : ",l)
puz.traceback(r)


'''
"F:\SEM 5\AIlab\venv\Scripts\python.exe" "F:\SEM 5\AIlab\8puzzle.py"
NOTE : Enter 0 for empty space

Uninformed Breadth First search

 No of nodes Discovered :  156122

7 2 4 
5   6 
8 3 1 

7 2 4 
  5 6 
8 3 1 

  2 4 
7 5 6 
8 3 1 

2   4 
7 5 6 
8 3 1 

2 5 4 
7   6 
8 3 1 

2 5 4 
7 6   
8 3 1 

2 5 4 
7 6 1 
8 3   

2 5 4 
7 6 1 
8   3 

2 5 4 
7 6 1 
  8 3 

2 5 4 
  6 1 
7 8 3 

2 5 4 
6   1 
7 8 3 

2 5 4 
6 1   
7 8 3 

2 5 4 
6 1 3 
7 8   

2 5 4 
6 1 3 
7   8 

2 5 4 
6 1 3 
  7 8 

2 5 4 
  1 3 
6 7 8 

2 5 4 
1   3 
6 7 8 

2 5 4 
1 3   
6 7 8 

2 5   
1 3 4 
6 7 8 

2   5 
1 3 4 
6 7 8 

  2 5 
1 3 4 
6 7 8 

1 2 5 
  3 4 
6 7 8 

1 2 5 
3   4 
6 7 8 

1 2 5 
3 4   
6 7 8 

1 2   
3 4 5 
6 7 8 

1   2 
3 4 5 
6 7 8 

  1 2 
3 4 5 
6 7 8 

Informed A* Search

 No of nodes Discovered :  6172

7 2 4 
5   6 
8 3 1 

7 2 4 
  5 6 
8 3 1 

  2 4 
7 5 6 
8 3 1 

2   4 
7 5 6 
8 3 1 

2 5 4 
7   6 
8 3 1 

2 5 4 
7 3 6 
8   1 

2 5 4 
7 3 6 
  8 1 

2 5 4 
  3 6 
7 8 1 

2 5 4 
3   6 
7 8 1 

2 5 4 
3 6   
7 8 1 

2 5   
3 6 4 
7 8 1 

2   5 
3 6 4 
7 8 1 

  2 5 
3 6 4 
7 8 1 

3 2 5 
  6 4 
7 8 1 

3 2 5 
6   4 
7 8 1 

3 2 5 
6 4   
7 8 1 

3 2 5 
6 4 1 
7 8   

3 2 5 
6 4 1 
7   8 

3 2 5 
6   1 
7 4 8 

3 2 5 
6 1   
7 4 8 

3 2   
6 1 5 
7 4 8 

3   2 
6 1 5 
7 4 8 

3 1 2 
6   5 
7 4 8 

3 1 2 
6 4 5 
7   8 

3 1 2 
6 4 5 
  7 8 

3 1 2 
  4 5 
6 7 8 

  1 2 
3 4 5 
6 7 8 

Informed Greedy Best First Search

 No of nodes Discovered :  695

7 2 4 
5   6 
8 3 1 

7 2 4 
5 6   
8 3 1 

7 2   
5 6 4 
8 3 1 

7   2 
5 6 4 
8 3 1 

  7 2 
5 6 4 
8 3 1 

5 7 2 
  6 4 
8 3 1 

5 7 2 
6   4 
8 3 1 

5 7 2 
6 3 4 
8   1 

5 7 2 
6 3 4 
  8 1 

5 7 2 
  3 4 
6 8 1 

5 7 2 
3   4 
6 8 1 

5 7 2 
3 4   
6 8 1 

5 7 2 
3 4 1 
6 8   

5 7 2 
3 4 1 
6   8 

5 7 2 
3   1 
6 4 8 

5   2 
3 7 1 
6 4 8 

  5 2 
3 7 1 
6 4 8 

3 5 2 
  7 1 
6 4 8 

3 5 2 
7   1 
6 4 8 

3   2 
7 5 1 
6 4 8 

3 2   
7 5 1 
6 4 8 

3 2 1 
7 5   
6 4 8 

3 2 1 
7   5 
6 4 8 

3   1 
7 2 5 
6 4 8 

3 1   
7 2 5 
6 4 8 

3 1 5 
7 2   
6 4 8 

3 1 5 
7   2 
6 4 8 

3 1 5 
  7 2 
6 4 8 

  1 5 
3 7 2 
6 4 8 

1   5 
3 7 2 
6 4 8 

1 7 5 
3   2 
6 4 8 

1 7 5 
3 2   
6 4 8 

1 7   
3 2 5 
6 4 8 

1   7 
3 2 5 
6 4 8 

1 2 7 
3   5 
6 4 8 

1 2 7 
3 4 5 
6   8 

1 2 7 
3 4 5 
6 8   

1 2 7 
3 4   
6 8 5 

1 2   
3 4 7 
6 8 5 

1   2 
3 4 7 
6 8 5 

1 4 2 
3   7 
6 8 5 

1 4 2 
3 7   
6 8 5 

1 4 2 
3 7 5 
6 8   

1 4 2 
3 7 5 
6   8 

1 4 2 
3   5 
6 7 8 

1   2 
3 4 5 
6 7 8 

  1 2 
3 4 5 
6 7 8 

Process finished with exit code 0

'''
