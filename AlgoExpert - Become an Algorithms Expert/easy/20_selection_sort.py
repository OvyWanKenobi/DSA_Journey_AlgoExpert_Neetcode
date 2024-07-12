# array = [8,5,2,9,7,6,3,10]

# we find the smallest numbers and put them in sorted partition

# time - O(n^2)
# space - O(1)

def selectionSort(array):
    
    currentidx = 0
    
    while currentidx < len(array)-1:
        smallestIdx = currentidx
        for i in range(currentidx+1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
         
        print(array)    
        array[currentidx], array[smallestIdx] = array[smallestIdx], array[currentidx]
        currentidx += 1
        
    return array 
        
        
def main():
    
    array = [8,5,2,9,7,6,3,10]
    
    sortedArray = selectionSort(array)
    
    print(sortedArray)
    
    
if __name__ == '__main__':
    main()
    
    
    