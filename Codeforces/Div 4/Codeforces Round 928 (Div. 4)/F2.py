from collections import defaultdict
from heapq import *
t = int(input())

for _ in range(t):
    M = []  
    
    n = 7

    for i in range(n):
        M.append(list(input().strip()))


    D1 = [[] for i in range(14)]
    D2 = [[] for i in range(14)]

    def check(M,ck):
        for i in range(1,n-1):
            for j in range(1,n-1):
                if( ((i+j)&1) == ck ):
                    if M[i][j] == "B":
                        if M[i-1][j-1] == "B" and M[i-1][j+1] == "B" and M[i+1][j-1] == "B" and M[i+1][j+1] == "B":
                        
                            return False
        return True
    
    done = False

    odb = []
    evb = []


    
    for i in range(1,n-1):
        for j in range(1,n-1):
            if ((i+j) & 1) and M[i][j] == "B":
                odb.append((i,j))
            elif ((i+j) % 2 == 0) and M[i][j] == "B":
                evb.append((i,j))

    # print(odb, evb)

    mi1 = 1000
    for i in range((1<<len(odb))):
        
        cm = 0
        for j in range(len(odb)):
            if (1<<j) & (i):
                M[odb[j][0]][odb[j][1]] = "W"
                cm += 1

        if check(M,1):
            mi1 = min(mi1, cm)

        for j in range(len(odb)):
            if (1<<j) & (i):
                M[odb[j][0]][odb[j][1]] = "B"

    mi2 = 1000
    odb = evb[:]
    # print(odb)
    for i in range((1<<len(odb))):
        
        cm = 0
        for j in range(len(odb)):
            if (1<<j) & (i):
                M[odb[j][0]][odb[j][1]] = "W"
                cm += 1

        if check(M,0):
            # print(cm)
            mi2 = min(mi2, cm)
            

        for j in range(len(odb)):
            if (1<<j) & (i):
                M[odb[j][0]][odb[j][1]] = "B"



    print(mi1 + mi2)