

# Q/A - Sum of two number in array equals to target number 

# 1st way  - 
#pick each number from array and iterate through all other number to check if equal to target sum

# time complexity - O(n^2) as two loops | space - O (1)

def twoNumberSum_wayone (arr, target):
    for i in range(len(arr)-1):   # len(arr)-1 as last number need no comparision, already compared with others
        firstNum = arr[i]
        for j in range(i+1, len(arr)): # i +1 as j should start from current number's next
            secondNum = arr[j]
            if((firstNum + secondNum) == target):
                return [firstNum, secondNum]
    return ['not found']


# 2nd way  - 
#if target sum = Z  and x+y=Z | so y=Z-x or x=Z-y
#we iterate through each element in array and put them in a temp dict, while also checking if value from (target-num) is already in temp dict or not, if element put earlier in temp array equals (target-num) , that is a possible combination match for target sum

# time complexity - O(n) as one iteration through array | space - O (N)

def twoNumberSum_waytwo (arr, target):
    nums_hashtable = {}
    
    for num in arr:
        potential_match = target-num
        if potential_match in nums_hashtable:
            return [potential_match, num]
        else:
            nums_hashtable[num] = True
    return ['not found']


# 3rd way  - 
#applies on already sorted array
# a left pointer points the first element in array, and right pointer the last element. Then we check if left + right  = target or not. If the sum is less than target, we move the left pointer one element to the right. If the sum is greater than target, move the Right pointer one element to the left. Then keep checking if current sum is equal, lesser, greater than target.keep doing the operation until sum equals to target

# time complexity - O(nlogn)  | space - O (1)

def twoNumberSum_waythree (arr, target):
    arr.sort()
    left = 0
    right = len(arr)-1
    while (left < right):
        currentSum = arr[left] + arr[right]
        if(currentSum == target):
            return[arr[left] , arr[right]]
        elif(currentSum < target): 
            left += 1
        elif(currentSum > target):
            right -= 1
    return ['not found']



# IN TERMS OF TIME COMPLEXITY 2ND WAY IS BEST - O(N), AND IN TERM OF SPACE COMPLEXITY 3RD WAY IS BETTER O(1)



def main():
    print("Hello World!")
    
    array = [3,5,-4,8,11,1,-1,6]
    target = 13
    
    print(twoNumberSum_wayone (array , target))
    print(twoNumberSum_waytwo (array , target))
    print(twoNumberSum_waythree (array , target))

if __name__ == "__main__":
    main()