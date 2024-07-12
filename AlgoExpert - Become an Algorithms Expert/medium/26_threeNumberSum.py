#given a array =  [12, 3, 1,2,-6,5,-8,6 ]
#we need to find the three number sum which is equal to a target 
# like if target is 0 , the output will be [[-8,2,-6], [-8,3,5], [-6,1,5]]

#first we need to sort the array
#then for each index we need to find two more number which sums to the target (if exist)
#for this we take left and right pointers. Left will start from the next index after the chosen index, and right is last index
#if the sum of Chosen number + left+ right is not target, and is less than target, we shift the left pointer one index to right, and if the sum is greater than target we shift the right pointer one index to the left. 
#we keep the shifting and finding the right three number sum candidates until left pointer greater than right pointer. 

# TIme complexity is O(n^2) and space is O(n)


def threeNumberSum(arr, target):
    
    arr.sort() 
    print(arr)
    
    result = []
    
  
    for i in range(len(arr)-2): 

        left = i+1
        right = len(arr)-1
        
        while left<right:
            
            currentSum = arr[i] + arr[left] + arr[right]
            
            # print(arr[i] , arr[left], arr[right], currentSum)
            
        
            if currentSum == target:
                result.append([arr[i] , arr[left] , arr[right]])
                left += 1
                right -= 1
                
            elif currentSum > target:
                right -= 1
                
            elif currentSum < target:
                left += 1
                
    
    return result
                


def main():
    array = [12, 3, 1,2,6 ,5,6,3,7,0]
    
    target = 0

    threeNumSumResult = threeNumberSum(array, target)
    
    print(threeNumSumResult)


if __name__ == "__main__":
    main()
    