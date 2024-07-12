# [2,1,2,2,3,4,2] -> move 2 to end -> [*,*,*,2,2,2,2]
# there is many way to do it, but most optimum way to have linear time complexity

# we set two pointers and start and end, i and j  
# then we check if i and j is target element, if i is target and j is not, we swap them, and mve the target to end, 
# OR if j is also target and also i we do not swap and move j one indexx to left,
# OR if i not target we move the i one index to right
#we keep doing until j is smaller than i

# Time complexity is O(n) and space is O(1)

def moveElementToEnd(arr, target):
     
    i = 0
    j = len(arr)-1
    
    while (i<j):
        print(arr, i ,j)
        
        # if( arr[i] == target and arr[j] != target):
        #     arr[i], arr[j] = arr[j] , arr[i]
        #     i+=1
        #     j-=1 
        # elif(arr[i] == target and arr[j] == target):
        #     j-=1
        # elif( arr[i] != target):
        #     i+=1
        
        while ( i<j and arr[j] == target):
            j-=1 #keep moving j to right untill we a non target , but if pass over i, we dont move j
        
        #now we have j in non target
        if(arr[i] == target):
            arr[i], arr[j] = arr[j] , arr[i]
        
        #as we swaped, we move i
        i+=1

    return arr



def main():
    
    array = [2,1,2,2,3,4,2]
    targetElement = 2
    
    result = moveElementToEnd(array, targetElement)
    
    print("result array:", result)
    
if __name__ == "__main__":
    main()
