# array = [8,5,2,9,7,6,3,10]

# we sort as we traverse through the array, like if we are travering, and reached index 4, we have to sort all the number ahead of it


# time - O(n^2)
# space - O(1)

def insertionSort(array):
    
    for i in range(1, len(array)-1):
        
        j = i 
        
        
        
        while j > 0  and array[j] < array[j -1]:
            
            print(array)
            
            array[j], array[j-1] = array[j -1], array[j]
            j-=1 
            
    return array

  
                
def main():
    
    array = [8,5,2,9,7,6,3,10]
    
    sortedArray = insertionSort(array)
    
    print(sortedArray)
    
    
if __name__ == '__main__':
    main()
    
    
    