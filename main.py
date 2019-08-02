import BrtNode as bn
import Brt as brt
import random

root = bn.BrtNode(7)
btree = brt.Brt()

btree.insert(root)

n1 = bn.BrtNode(5)
btree.insert(n1)

n2 = bn.BrtNode(6)
btree.insert(n2)

n3 = bn.BrtNode(2)
btree.insert(n3)

n4 = bn.BrtNode(9)
btree.insert(n4)

n5 = bn.BrtNode(3)
btree.insert(n5)

n6 = bn.BrtNode(8)
n7 = bn.BrtNode(88)
n8 = bn.BrtNode(76)
n9 = bn.BrtNode(4)

btree.insert(n6)
btree.insert(n7)
btree.insert(n8)
btree.insert(n9)

btree.inorder_tree_walk(root)

sottoalbero = brt.Brt()
for i in range (5):
    sottoalbero.insert(bn.BrtNode(random.randint(0, 20)))

btree.delete_node(n7)
