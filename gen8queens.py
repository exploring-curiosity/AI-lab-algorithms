import random
import heapq
class chessboard:
    def __init__(self,state):
        self.state=state
        self.cost=self.collision(state)

    def __str__(self):
        line = "\n"
        for i in range(8):
            temp = "* " * (self.state[i] - 1) + "Q " + "* " * (8 - self.state[i]) + "\n"
            line += '\t' + temp
        return line

    def __lt__(self, otherboard):
        return self.cost <= otherboard.cost
    def collision(self, bd):
        c = 0
        for i in range(8):
            for j in range(i + 1, 8):

                if (self.state[i] == self.state[j]):
                    c += 1
                elif (self.state[i] + i == self.state[j] + j):
                    c += 1
                elif (self.state[i] - i == self.state[j] - j):
                    c += 1
        return c

class solver:
    def __init__(self):
        print("Intializing board....")

    def genChild(self,p1,p2):
        c=random.randint(0,7)
        x=list()
        x.append(chessboard(p1.state[:c] + p2.state[c:]))
        x.append(chessboard(p2.state[:c] + p1.state[c:]))
        return x

    def mutate(self,state):
        c = random.randint(0, 7)
        m = random.randint(1, 8)
        newstate=state.state[:]
        newstate[c]=m
        return chessboard(newstate)

    def best(self,randomstates):
        best=randomstates[0]
        cost=self.collision[best]
        for state in randomstates:
            if self.collision[state]<cost:
                cost=self.collision[state]
                best=state
        return best

    def queens(self,cur_pop,k):
        limit = 10000
        cntr = 0
        gen = 0
        result=None
        while(cntr<limit ):
            cur_pop = cur_pop[:6]
            last_best=cur_pop[0]
            n=random.randint(1,3)
            for itr in range(n):
                children = self.genChild(cur_pop[itr*2],cur_pop[itr*2+1])
                cur_pop += children
                heapq.heapify(cur_pop)
            while len(cur_pop)< k:
                c=random.randint(0,len(cur_pop)-1)
                new_state= self.mutate(cur_pop[c])
                heapq.heappush(cur_pop,new_state)
            heapq.heapify(cur_pop)

            result = cur_pop[0]
            gen+=1
            if result.cost == 0:
                return result,gen
            elif result.cost<last_best.cost:
                cntr=0
            else:
                result =last_best
                cntr+=1
        return result,gen


def random_individual():
    return [random.randint(1, 8) for i in range(8)]


def randomize(k):
    return [chessboard(random_individual()) for i in range(k)]

print("8Queens-Genetic solution")
k=int(input("Enter basic population size : "))
random_pop= randomize(k)
puzzle=solver()
result,gen=puzzle.queens(random_pop,k)
print("close matching Result found on generation : ",gen)
print("the state is :",result)
print("the fitness is :",result.cost)


'''
8Queens-Genetic solution
Enter basic population size : 15
Intializing board....
close matching Result found on generation :  558
the state is : 
	* * * * Q * * * 
	* Q * * * * * * 
	* * * * * * * Q 
	Q * * * * * * * 
	* * * Q * * * * 
	* * * * * * Q * 
	* * Q * * * * * 
	* * * * * Q * * 

the fitness is : 0
'''
