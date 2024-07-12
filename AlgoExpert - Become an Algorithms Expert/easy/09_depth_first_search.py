class Node : 
    
    #these two function is to create the tree
    
    def __init__(self, name): 
        self.children = []
        self.name = name
        
    def addChild(self, child):
        self.children.append(child)
      
        
        
    #this below is actal DFS algo
                             
    def depthFirstSearch(self, array):
    
        
        array.append(self.name)
        
        
        for child in self.children:

            child.depthFirstSearch(array)
        return array
        



def main():
    print("Hello World!")
    
# Create nodes
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")
    nodeH = Node("H")
    nodeI = Node("I")
    nodeJ = Node("J")
    nodeK = Node("K")
    
    # Build the tree
    nodeA.addChild(nodeB)
    nodeA.addChild(nodeC)
    nodeA.addChild(nodeD)
    nodeB.addChild(nodeE)
    nodeB.addChild(nodeF)
    nodeD.addChild(nodeG)
    nodeD.addChild(nodeH)
    nodeF.addChild(nodeI)
    nodeF.addChild(nodeJ)
    nodeG.addChild(nodeK)

    
    # Perform depth-first search
    result = nodeA.depthFirstSearch([]) #the empty array is passed at start of root node and series of recursive functions happens and return the array filled with nodes using DFS method
    print("Depth First Search:", result)

if __name__ == "__main__":
    main()