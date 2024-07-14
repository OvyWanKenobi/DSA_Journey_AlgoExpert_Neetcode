    
# Satisfy BST PROPERTY 
# each node has max of 2 modes
# Each node is stictly smaller than their right child and larger than left child


# BST supports Insertion, Searching , Deletion 

# when traversing thru the tree during Insertion, Searching , Deletion  if we looking for a number and If the we are looking number is greater than the current node  then we shall look into the right subtree because in left subtree  all the nodes will be smaller than the number we are looking for so we look into the right child

# time and space complexity is O(log(N))  as we discard half the tree as we traverse through it , but if there is only one child each node, then the time and space complex is worst O(n) 10-1-2-6-12-5-8, going thru all 
# (space is storing each nodes in stack if we use recursive method as we go down the branches, but if we use iterative, space complexity is always O(1))

class BST:
    
    def __init__(self,value): #this makes a new node 
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        currentNode = self #current to head node (self(bst))
        while True:
            if value < currentNode.value: #look to left
                if currentNode.left is None: #if nothing in left make a new node 
                    currentNode.left = BST(value)
                    break
                else :
                    currentNode = currentNode.left #if there is a node go there and while loop go next iteration
            else: #look to right
                if currentNode.right is None: #if nothing in right make a new node 
                    currentNode.right =BST(value)
                    break
                else:
                    currentNode = currentNode.right #if there is a node go there and while loop go next iteration
                    
        return self
        
        
    def search(self, target):
        currentNode = self
        
        while currentNode is not None :
            if target < currentNode.value:
                currentNode =currentNode.left
                
            elif target > currentNode.value: 
                currentNode = currentNode.right
               
            else:
                return True

        return False
    

        
    def delete(self, target, parentNode = None):
        currentNode = self
        while currentNode is not None :
            if target < currentNode.value:
                parentNode = currentNode #we track the parent node as we need to chain the children of deleting node to the parent node
                currentNode =currentNode.left
            elif target > currentNode.value: 
                parentNode = currentNode
                currentNode = currentNode.right
            else: #target node found  and is current node
                if currentNode.left is not None and currentNode.right is not None: #if target node has two children
                    currentNode.value = currentNode.right.getMinValue() #replace the target currentnode with smallest value from right sub tree
                    currentNode.right.delete(currentNode.value, currentNode) #then delete the smallest value found in right subtree of current node
                elif(parentNode is None) : #no parent node/target node is root node, and there is only one children (two children case is served )
                    if (currentNode.left is not None): #only children node is in left
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right #redirect whatever in right of currentnode.left to currentnode.right 
                        currentNode.left = currentNode.left.left#redirect whatever in left of currentnode.left to currentnode.right 
                        
                    elif (currentNode.right is not None): #only children node is in right
                        currentNode.value = currentNode.right.value
                        currentNode.right = currentNode.right.right #redirect whatever in right of currentnode.right to currentnode.right 
                        currentNode.left = currentNode.right.left #redirect whatever in left of currentnode.right to currentnode.right 
                        
                    else : 
                        currentNode.value =None #no children node, root node is target, remove root node
                elif(parentNode.left == currentNode) :#currentnode is target node and is only child of parenetnode and is in left of parent node
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right #parent node left branch is redirect to left of target node or right which ever is there
                elif(parentNode.right == currentNode) :#currentnode is target node and is only child of parenetnode and is in right of parent node
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right #parent node right branch is redirected to left of target node or right which ever is there
                return "Target deleted"
        return "Target dont exists"
        
    def getMinValue(self):
         currentNode = self
         while currentNode.left is not None:
             currentNode = currentNode.left
         return currentNode.value
     
     
    def inorder_traversal(self): #traverse the bst
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()
        elements.append(self.value)
        if self.right:
            elements += self.right.inorder_traversal()
        return elements
    


def main():
    
    array = [10,3,5,36,4,12,9,24,2,125]
    
    bst = BST(array[0]) #first node made here for "bst" instence
    
    for value in array[1:]:
        bst.insert(value)
        
    print("Inorder Traversal of the BST:", bst.inorder_traversal())
    
    print(bst.search(7))
    
    print(bst.delete(125))
    
    print("Inorder Traversal of the BST:", bst.inorder_traversal())
    
if __name__ == '__main__':
    main()