from random import shuffle
#hahi
def makeBoard():
    K1=[[9,4,3,1,2,7,8,6,5],
       [1,2,7,6,5,8,3,9,4],
       [5,6,8,3,4,9,7,2,1]]
    K2=[[7,5,2,4,3,1,9,8,6],
       [6,3,9,2,8,5,1,4,7],
       [4,8,1,7,9,6,5,3,2]]
    K3=[[8,1,4,9,7,2,6,5,3],
       [2,9,6,5,1,3,4,7,8],
       [3,7,5,8,6,4,2,1,9]]
    shuffle(K1)
    shuffle(K2)
    shuffle(K3)
    K=K1+K2+K3
    K1,K2,K3 = [[K[e][i] for e in range(9)] for i in range(3)],[[K[e][i+3] for e in range(9)] for  i in range(3)],[[K[e][i+6] for e in range(9)] for  i in range(3)]
    shuffle(K1)
    shuffle(K2)
    shuffle(K3)
    K=K1+K2+K3
    return K


import time
t = -time.time()
T=makeBoard()
t+=time.time()
print(t,*T,sep='\n')

#rossz volt az ötlet
"""
#3 szabály:
#1. Sorokban nem lehet ugyanaz
#2. Oszlopokban nem lehet ugyanaz
#3. Négyzetekben nem lehet ugyanaz
#4. Nem lehet 2 szám egy helyen
#choosen = [0,1] -- 0. sor 1. oszlop 
from random import randrange
def makeBoard(n=9):
    T=[[0]*n for i in range(n)]
    for szam in range(1,n+1):
        Available_1 = {x for x in range(n)}
        Available_3 = {x for x in range(n)}
        #2.
        for col in range(n):
            #4
            Available_4 = {row for row in range(n) if T[row][col] == 0}
            #1.
            nowAvailable = list(Available_4 & Available_1 & Available_3)
            
            if len(nowAvailable)>1:
                choosen = [nowAvailable[randrange(0, len(nowAvailable)-1)],col]
            else:
                choosen = [nowAvailable[0],col]
            #print(szam,"\n", nowAvailable, "\n", choosen)
            Available_1-={choosen[0]}
            #3.
            if col%3 == 2:
                Available_3 = {x for x in range(n)}
            else:
                if choosen[0] < 3:
                    Available_3 -= {0,1,2}
                elif choosen[0] > 5:
                    Available_3 -= {6,7,8}
                else:
                    Available_3 -= {3,4,5}
            T[choosen[0]][choosen[1]] = szam
            print(*T,sep = "\n", end ="\n\n")
    return T
"""
            


