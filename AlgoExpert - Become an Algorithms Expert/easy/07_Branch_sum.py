



# branch sum is we apply a depth search and a branch (root to leaf) will give a value of the branch sum
# we need to find a list of all the branch sum in binary tree

# TIme complexity - O(n)  | space - O(n)

def branchSum(root):
    branchSumsList = []
    calculateBranchSums(root, 0 , branchSumsList)
    return branchSumsList

def calculateBranchSums(node, runningSum, branchSumsList):
    if node is None:
        return
    
    newRunningSum = runningSum + node.value
    
    if node.left is None and node.right is None :
        branchSumsList.append(newRunningSum)
        return
    
    calculateBranchSums(node.left, newRunningSum, branchSumsList)
    calculateBranchSums(node.right, newRunningSum, branchSumsList)
    
    
    
    
    
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_binary_tree(values, index):
    if index < len(values):
        if values[index] is None:  #if value list passed is empty
            return None
        
        node = TreeNode(values[index])
        node.left = build_binary_tree(values, 2 * index + 1) #For any node at index i, its left child is at index 2 * i + 1. This is because in a binary tree, each node's left child is inserted immediately after itself.
        node.right = build_binary_tree(values, 2 * index + 2)  #Similarly, the right child of a node at index i is at index 2 * i + 2.
        return node
    return None





def main():
    print("Hello World!")
    
    
    values = [1, 2, 3, 4,5,6,7,8,9,10]
    
    root = build_binary_tree(values, 0)
    
    sums = branchSum(root)
    print("Branch Sums:", sums)
    

if __name__ == "__main__":
    main()
    