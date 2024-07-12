
# [8,5,2,9,5,6,3,10]
#In bubble sort, we sort the largest to smallest number first
# we traverse through each index and compare if index value greater or smaller than next index, if greater, we swap,
# as we go to the end, the largest number will be at its desired position
#now we will traverse again from beginning, but exclude the index which we already sorted

# time - O(n^2) as we need to traverse thru array multiple time | space - O(1)


def bubbleSort(array):
    
    isSorted = False
    counter = 0 #to avoid the recently sorted numbers 
    
    while not isSorted:
        
        isSorted = True  #first it will be made true, if no swapping is done in first iteration, the isSorted   remain True and no more traversal needed meaning array is sorted already
        
        for i in range(len(array) -1 - counter):
            if array[i] > array[i+1]:
                array[i] , array[i+1] = array[i+1], array[i] 
                isSorted = False
        
        counter += 1
        
    return array
                
        
                
def main():
    
    array = [8,5,2,9,7,6,3,10]
    
    sortedArray = bubbleSort(array)
    
    print(sortedArray)
    
    
if __name__ == '__main__':
    main()
    
    
    