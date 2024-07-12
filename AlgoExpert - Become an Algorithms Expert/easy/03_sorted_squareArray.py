
#to ssquare and sort an arrray, we can just square it and apply .sort() .

def sortedSquaredArray_usingSortLib(arr):
    sortedSquares = [ 0 for _ in arr] #this make a new array soredsquares and put 0 in all index for length of arr
    
    #now we take each value from arr and square them and put in sortedSquares
    for idx in range(len(arr)):
        value = arr[idx] 
        sortedSquares[idx] = value * value
        
    sortedSquares.sort() #simple sort the array
    return sortedSquares

#THIS METHOD HAS A TIME COMPLEXITY OF O(nlogn) as it uses .sort() funtion | space - O(N)

#but WE HAVE ANOTHER METHOD WHICH HAS LESS TIME COMPLEXITY O(n) 

#also this below method is also effective when we have negative values in array

def sortedSquaredArray_optimum(arr):
    sortedSquares = [ 0 for _ in arr] 
    
    #here we first put pointers at start and end of array
    leftId = 0
    rightId = len(arr)-1
    
    for i in reversed(range(len(arr))): #revered so the idx starts from end rear/ largest i
        
       
        leftvalue = arr[leftId]
        rightvalue = arr[rightId]
        
         #we take the value of left and right end and compare which MODULUS is bigger.
         #which ever is bigger we square them and put the squared in largest i index
         #then we move the left/right, which ever is bigger , more inward in array
         
        if abs(leftvalue) > abs(rightvalue):
            sortedSquares[i] = leftvalue * leftvalue
            leftId += 1  
            
        else:
            sortedSquares[i] = rightvalue * rightvalue 
            rightId -=1
    
    return sortedSquares 




def main():
    print("Hello World!")
    
    array = [ -9, -7, 0 ,1,2,3,4,5]

    
    print(sortedSquaredArray_usingSortLib(array))
    print(sortedSquaredArray_optimum(array))
    

if __name__ == "__main__":
    main()
