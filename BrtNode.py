class BrtNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.father = None
        if key is not None:
            self.key = key
        else:
            self.key = None


    def setRight(self, right):
        self.right = right

    def setLeft(self, left):
        self.left = left

    def setFather(self, father):
        self.father = father

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getFather(self):
        return self.father

