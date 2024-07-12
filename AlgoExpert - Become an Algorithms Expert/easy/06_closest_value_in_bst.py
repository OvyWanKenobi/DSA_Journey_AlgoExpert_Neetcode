
#Q/A - A target and a bst is given, we need to find a value in bst, which is closest to the target

# There are two ways of doing this. One applied Recursion and another do not 

def findClosestValueInBst_recursion(tree, target, currentClosest):
    if tree is None : #we reached a node in tree which has no value, End Leaves
        return currentClosest
    
    #if the diff btwn target and current tree node(tree.value) is smaller than the target and currentClosest, meaning the tree.value is closer to target than currentClosest, So we make the tree.value as currentClosest 
    if abs(target-currentClosest) > abs(target - tree.value): 
        currentClosest = tree.value
        
    #now we check if the children of current node is more suitable choice | We checking if there is more smaller number btwn target and tree.value.  So we look into nodes values between tree.value and target
    
    if target < tree.value:
        return findClosestValueInBst_recursion(tree.left, target, currentClosest) #as targer smaller than current node value we go tree.left, as smaller children are kept in left side of node in BST. 
    
    elif target > tree.value:
        return findClosestValueInBst_recursion(tree.right, target, currentClosest) #as targer greater than current node value we go tree.right, as larger children are kept in right side of node in BST.
    
    else : 
        return currentClosest
    
    # THE Time comp is O(log(n)) as we go through half of the BST | SPace comp - O(log(n))
    
    # THIS USES A RECURSION WAY TO TRAVERSE THE TREE. WE HAVE ANOTHER METHOD USING ITERATION
    
    
def findClosestValueInBst_withoutRecursion(tree, target, currentClosest):
   
    currentNode = tree
    
    # here using the currentNode we are checking the node with target, and updating the current node as we traverse through the tree
    
    while currentNode is not None:
        if abs(target-currentClosest) > abs(target - currentNode.value): 
            currentClosest = currentNode.value
        
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
        
    return currentClosest
    
    
    
    
    
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):

    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root    
    

def main():
    print("Hello World!")
    
    # Constructing a sample binary search tree
    bstree = None
    values = [10, 5, 15, 2, 5, 13,19, 1, 14]
    for value in values:
        bstree = insert(bstree, value)
    
    
        
    target = 20

    print(findClosestValueInBst_recursion(bstree, target, float('inf')))
    

if __name__ == "__main__":
    main()
