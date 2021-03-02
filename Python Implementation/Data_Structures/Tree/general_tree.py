class TreeNode:
    def __init__(self, data):
        self.data = data
        self.childern = []
        self.parent = None

    def addChild(self, child):
        if type(child) == TreeNode:
            child.parent = self
            self.childern.append(child)
        else:
            child.parent = self
            self.childern.append(TreeNode(child))

    def getLevel(self):
        level = 0
        currentParent = self.parent
        while currentParent != None:
            level += 1
            currentParent = currentParent.parent
        return level

    def printTree(self):
        print(self.getLevel()*"\t", self.data)
        if len(self.childern) > 0:
            for child in self.childern:
                child.printTree()

if __name__ == "__main__":
    root = TreeNode("Electronics")
    root.addChild(TreeNode("Laptop"))
    root.printTree()
    
