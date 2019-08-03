import Brt
import RBnode


class RbTree(Brt.Brt):

    def __init__(self):
        self.NIL = RBnode.RBnode(None)
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.NIL:
            y.left.fater = x
        y.father = x.father
        if x.father is self.NIL:
            self.root = y
        elif x is x.father.left:
            x.father.left = y
        else:
            x.father.right = y
        y.left = x
        x.father = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self.NIL:
            y.right.fater = x
        y.father = x.father
        if x.father is self.NIL:
            self.root = y
        elif x is x.father.right:
            x.father.right = y
        else:
            x.father.left = y
        y.right = x
        x.father = y

    def insert(self, z):
        y = self.NIL
        x = self.root
        while x is not self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.father = y
        if y is self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.NIL
        z.right = self.NIL
        z.red = True
        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.father.red is True:
            if z.father is z.father.father.left:
                y = z.father.father.right
                if y.red is True:
                    z.father.red = False
                    y.red = False
                    z.father.father.red = True
                    z = z.father.father
                else:
                    if z is z.father.right:
                        z = z.father
                        self.left_rotate(z)
                    z.father.red = False
                    z.father.father.red = True
                    self.right_rotate(z.father.father)
            else:
                    y = z.father.father.left
                    if y.red is True:
                        z.father.red = False
                        y.red = False
                        z.father.father.red = True
                        z = z.father.father
                    else:
                        if z is z.father.left:
                            z = z.father
                            self.right_rotate(z)
                        z.father.red = False
                        z.father.father.red = True
                        self.left_rotate(z.father.father)
        self.root.red = False

    pass
