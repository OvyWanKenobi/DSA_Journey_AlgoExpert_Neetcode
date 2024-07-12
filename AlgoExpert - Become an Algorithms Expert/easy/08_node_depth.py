
#sum of all the node depth from the root

#There is a iterative method, but resursive method is simpler

#recursive approach = 

def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)

#in here , we will be going down all the way down to each node using resursive method, assigning a depth to each node in the way, and sum them as we return to the calling functions 

# Time complexity - O(n) where n is number of nodes,  and space complexity is O(h) where h is number of recursive calls




    
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
    
    
    values = [1, 2, 3, 4,5,6,7,8,9]
    
    root = build_binary_tree(values, 0)
    
    sums = nodeDepths(root)
    print("Sum of Node Depths:", sums)
    

if __name__ == "__main__":
    main()