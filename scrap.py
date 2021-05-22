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

    def huerestic(self, st):
        # huerestic functon
        h = 0
        return h


class problem:
    def __init__(self, st, goal):
        self.states = defaultdict(list)
        self.start = st
        self.goal = goal

    def is_goal(self, n):
        if (n == self.goal):
            return True
        return False

    def addEdge(self, u, v):
        self.states[u].append(v)

    def next_node(self, n):
        x = []
        return x


def WhatEverFirstSearch(p):
    n = node(p.start)
    Frontier = []
    Frontier.append(n)
    Explored = {}
    Explored[p.start] = n
    while len(Frontier) != 0:
        n = Frontier.pop(0)
        if (p.is_goal(n.state)):
            return n
        for i in p.next_node(n):
            s = i.state
            if s not in Explored.keys() or i.f < Explored[s].f:
                Explored[s] = i
                Frontier.append(i)
    return "Failure"


def BreadthFirstSearch(p):
    n = node(p.start)
    if (p.is_goal(n.state)):
        return n
    Frontier = []
    Frontier.append(n)
    Explored = set()

    while len(Frontier) != 0:
        n = Frontier.pop(0)
        Explored.add(n.state)
        for i in p.next_node(n):
            s = i.state
            if s not in Explored:
                if s not in Frontier:
                    if (p.is_goal(i.state)):
                        return i
                    Frontier.append(i)
    return "Failure"


def UniformCostSearch(p):
    n = node(p.start)
    Frontier = []
    heapq.heappush(Frontier, n)
    Explored = set()
    Explored.add(n.state)
    while len(Frontier) != 0:
        n = Frontier.pop(0)
        if (p.is_goal(n.state)):
            return n
        for i in p.next_node(n):
            s = i.state
            if s not in Frontier:
                if s not in Explored:
                    heapq.heappush(Frontier, i)
            else:
                for z in Frontier:
                    if (z.state == s) and z.f >= i.f:
                        Frontier.remove(z)
                        heapq.heappush(Frontier, i)
    return "Failure"


# global explored
def Recursive_DFS(n, p):
    explored = set()  # to be deleted
    if p.is_goal(n.state):
        return n
    explored.add(n)
    for i in p.next_node(n):
        if i not in explored:
            result = Recursive_DFS(i, p)
            if result != "Failure":
                return result
    return "Failure"


# global explored
def Recursive_DLS(n, p, limit):
    explored = set()  # to be deleted
    if p.is_goal(n.state):
        return n
    if limit == 0:
        return "cutoff"
    cut_off = False
    explored.add(n)
    for i in p.next_node(n):
        if i not in explored:  # no need for explored
            result = Recursive_DLS(i, p, limit - 1)
            if result == "cutoff":
                cut_off = True
            elif result != "Failure":
                return result
    if cut_off:
        return "cutoff"
    return "Failure"


# no need for explored
def PriorityFirstSearch(p):
    n = node(p.start)
    Frontier = []
    heapq.heappush(Frontier, n)
    Explored = set()
    while len(Frontier) != 0:
        n = Frontier.pop(0)
        if (p.is_goal(n.state)):
            return n
        if n not in Explored:
            Explored.add(n)
            for i in p.next_node(n):
                s = i.state
                if s not in Frontier:
                    if s not in Explored:
                        heapq.heappush(Frontier, i)
                else:
                    for z in Frontier:
                        if (z.state == s) and z.f >= i.f:
                            Frontier.remove(z)
                            heapq.heappush(Frontier, i)
    return "Failure"


