
# This is for linked list which is sorted

#we take a current node and check which node is distinct from the current node, and on found we set the next of current node to that distinct node and if any node in middle which is duplicate of current node will be removed

#next we set the current node variable to next district node and contine till we reach NONE


# TIME COMPLEXITY - O(n) as we look through each node only one


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
        
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None :
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next
        
        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
        
    return linkedList





def printLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        print(currentNode.value, end=" -> ")
        currentNode = currentNode.next
    print("None")

def createLinkedList(values):
    if not values:
        return None
    head = LinkedList(values[0])
    currentNode = head
    for value in values[1:]:
        newNode = LinkedList(value)
        currentNode.next = newNode
        currentNode = newNode
    return head

def main():
    # Example list of values with duplicates
    values = [1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6]
    
    # Create a linked list from the values
    linkedList = createLinkedList(values)
    
    # Print the original linked list
    print("Original linked list:")
    printLinkedList(linkedList)
    
    # Remove duplicates from the linked list
    removeDuplicatesFromLinkedList(linkedList)
    
    # Print the linked list after removing duplicates
    print("Linked list after removing duplicates:")
    printLinkedList(linkedList)

if __name__ == "__main__":
    main() 
        
