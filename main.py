import BrtNode as bn
import Brt as brt
import RBnode
import RbTree
import random
from timeit import default_timer as timer

v1 = []

for i in range(11):
    v1.append(random.randint(0, 100))

btree = brt.Brt()
rbtree = RbTree.RbTree()

bstart = timer()
for x in v1:
    btree.insert(bn.BrtNode(x))
bend = timer()
btime = bend - bstart

rbstart = timer()
for x in v1:
    rbtree.insert(RBnode.RBnode(x))
rbend = timer()
rbtime = rbend - rbstart

print("u tiempu ri chiddu binariu è: ")
print(btime)

print("l'autru tiempu (chiddu russu e nniuru) eni: ")
print(rbtime)


