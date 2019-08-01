import BrtNode as bn
import Brt as brt

root = bn.BrtNode(7)
btree = brt.Brt(root)

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

print("maria friddu")
print(btree.maximum(root).key)

if btree.search(root, 43) is not None:
    print("sono così felice che potrei ruscellare fluidi gastrici")
else:
    print("il nonno adesso caga ghiaccio e per questo ora è muto ma almeno così non racconta più le storie")

print("il numero magico è...")
print(btree.successor(n5).key)
print("manuela è stupida qundi parla da sola ps io e marco siamo ineteligentissimi e manunononnoonononononmachicazzoyammiyammi")



