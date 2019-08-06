import BrtNode as bn
import Brt as brt
import RBnode
import RbTree
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

t1 = []
t2 = []



'''
a = 0
while a < 10**6:
    a = a + 50000
    N.append(a)

for i in N:
    print("ne faccio: ")
    print(i)
    v1 = []

    for j in range(i+1):
        v1.append(random.randint(0, 10**4))

    btree = brt.Brt()
    rbtree = RbTree.RbTree()

    vbrt = []
    vrb = []
    for x in v1:
        vbrt.append(bn.BrtNode(x))
        vrb.append(RBnode.RBnode(x))

    bstart = timer()
    for x in vbrt:
        btree.insert(x)
    bend = timer()
    t1.append(bend - bstart)

    
    rbstart = timer()
    for x in vrb:
        rbtree.insert(x)
    rbend = timer()
    t2.append(rbend - rbstart)
    

plt.plot(N, t1)
plt.title("Binario")
plt.show()


plt.title("Rossonero")
plt.plot(N, t2)
plt.show()

plt.title("insieme")
plt.plot(N, t1)
plt.plot(N, t2)
plt.show()

'''
num_nodi = 10000
iterazioni = 10000
V = []
N = []

for i in range(num_nodi):
    N.append(i)


bNodes = []
btimes = []
bcurrent = []

for i in range(iterazioni):
    btree = brt.Brt()
    print((i+1).__str__()+"di"+iterazioni.__str__())

    for x in N:
        V.append(random.randint(0, 1000))

    for j in V:
        bNodes.append(bn.BrtNode(j))

    for k in bNodes:
        init = timer()
        btree.insert(k)
        end = timer()
        bcurrent.append(end - init)

    insert = bcurrent[:]
    btimes.append(insert)
    bcurrent.clear()
    V.clear()
    bNodes.clear()



averagetime = []

for i in range(num_nodi):
    sum = 0
    for j in range(len(btimes)):
        sum += btimes[j][i]
    averagetime.append((sum/num_nodi))
    print(i.__str__())


plt.title("Albero Binario")
plt.plot(N, averagetime)
plt.show()
