class Brt:

    def __init__(self):
        self.root = None

    def setRoot(self, root):
        self.root = root

    def getRoot(self):
        return self.root

    def inorder_tree_walk(self, x):
        if x is not None:
            self.inorder_tree_walk(x.left)
            print(x.key)
            self.inorder_tree_walk(x.right)

    def search(self, x, k):
        if x is None or k is x.key:
            return x
        if k < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def maximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def successor(self, x):
        if x.right is not None:
            return self.minimum(x.right)
        y = x.father
        while y is not None and x is y.right:
            x = y
            y = y.father
        return y

    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.father = y
        if y is None:
            self.setRoot(z)
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def trapianto(self, u, v):
        if u.father is None:
            self.root = v
        elif u is u.father.left:
            u.father.left = v
        else:
            u.father.right = v
        if v is not None:
            v.father = u.father

    def delete_node(self, z):
        if z.left is None:
            self.trapianto(z, z.right)
        elif z.right is None:
            self.trapianto(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.father is not z:
                self.trapianto(y, y.right)
                y.right = z.right
                y.right.father = y
            self.trapianto(z, y)
            y.left = z.left
            y.left.father = y
