class BrtNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.father = None

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

