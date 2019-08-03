import BrtNode as bn
import Brt as brt
import RBnode
import RbTree
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

t1 = []
t2 = []

N = []
a = 0
while a < 100:
    a = a + 2
    N.append(a)

for i in N:
    print("ne faccio: ")
    print(i)
    v1 = []

    for j in range(i):
        v1.append(random.randint(0, 100))

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

