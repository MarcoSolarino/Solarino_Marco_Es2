import BrtNode


class RBnode(BrtNode.BrtNode):
    def __init__(self, key):
        BrtNode.BrtNode.__init__(self, key)
        self.red = False

    def set_color(self, color):
        self.red = color

    pass
