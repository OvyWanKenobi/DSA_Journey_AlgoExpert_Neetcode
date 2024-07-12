
# BINARY SEARCH IS IN A SORTED ARRAY OR LIST, WHEN YOU HAVE TO FIND A ELEMENT YOU LOOK AT THE MIDDLE AND SEE DO THE TARGET IS IN FORST HALF OR SECOND HALF, THEN YOU AGAIN LOOK IN THE MIDDLE OF THE HLAF THE ELEMENT IS, AND CONTINUE REPEATING IT UNTIL YOU REACH HALVES WITH ONLY ONE ELEMENT. MEANING TARGET IS ANY ONE OF THEM


# Time complexity is O(log(n)) as we omit half remaining array everytime we traverse
#space - O(1) in iterative method and  O(log(n)) in recursive as call stacks


# in recursive method:
# def binarySearch(array , target, left, right):
    
#     if left >  right : 
#         return -1
    
#     middle = (left + right) // 2
    
#     if(array[middle] < target):
#         return binarySearch(array, target,  middle + 1, right )
#     elif (array[middle] > target):
#         return binarySearch(array, target, left, middle - 1)
#     else:
#         return middle



#in iterative method :
def binarySearch(array , target, left, right):
    
    while left <=  right :
        middle = (left + right) // 2
    
        if(array[middle] < target):
            left =  middle + 1
        elif (array[middle] > target):
            right = middle - 1
        else:
            return middle 
    
    return -1
        

def main():
    
    array = [1,6, 15, 23,34, 41, 59, 62, 74, 87, 90]
    
    target = 1
    
    targetidx = binarySearch(array, target, 0, len(array)-1)

    if targetidx != -1:
        print(f'{target} found at index {targetidx} ')
    else:
        print(f'{target} not found')
        
        
if __name__ == "__main__":
    main()
        
    

    
    
    
    