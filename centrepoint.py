class matrix:
    def __init__(self,l):
        self.points=l

    def next(self,point):
        x=list()
        x.append((point[0]-1,point[1]))
        x.append((point[0],point[1]-1))
        x.append((point[0],point[1]+1))
        x.append((point[0]+1,point[1]))
        if point[0]==0:
            x.remove((point[0]-1,point[1]))
        if point[1]==0:
            x.remove((point[0],point[1]-1))
        return x

    def d(self,a,v):
        return abs(a[0]-v[0])+abs(a[1]-v[1])

    def Sum(self,v):
        s=0
        for a in self.points:
           s+= self.d(a,v)
        return s

    def hillClimb(self):
        x=[p[0] for p in self.points]
        y=[p[1] for p in self.points]
        cstate=(sum(x) // len(self.points), sum(y) // len(self.points))
        cval=self.Sum(cstate)
        while(True):
            temp = cstate
            for i in self.next(temp):
                if(self.Sum(i)<cval):
                    cval=self.Sum(i)
                    cstate=i
            if(temp==cstate):
                return cstate


n=int(input("Enter number of points : "))
l=[]
for i in range(n):
    l.append(tuple(map(int,input("point >").split(" "))))
m=matrix(l)
print("The centre is : ",m.hillClimb())

'''
output:
Enter number of points : 5
point >1 2
point >2 3
point >3 4
point >4 5
point >6 7
The centre is :  (3, 4)
'''