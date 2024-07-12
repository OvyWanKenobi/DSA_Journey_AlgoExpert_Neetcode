# array = [2,1,5,2,3,3,4]

# we need to find the first duplicate value , here in sample array 2 is the first duplicate value

# this can be done in three ways , each better than another

# 1st way is picking the value in first index and check consequtive indexes for duplicate value, if any duplicate found we update the minimunDupIndex to that index, then pick the value in next index and check consequetive indexes for duplicates. and keep going.. update the mininumDupIndex is any lesser index found, return value at minimumDupIndex '
# This has time complexity of O(n^2) as we have to go thru the array nXn times. Space complexity is constant O(1)

# 2nd way is having a seen set, and as we traverse thru the array we keep them in the Seen set , and always check if the value already exist in the set. If a value found existing in th set, return the value as result 
# Time complexity is O(n) as we only have to traverse thru the array once. Space complexity is also O(n) as we need to create a new set of seen values. 

#third way and most optimum way but only works for positive integers array, we go thru the array, for any value we update the index of (abs(value) -1 ) to negative. Like for value 3, we set the value in abs(3)-1 = 2nd index to negative of whatever value in that index. In this way we can keep track of which values we have seen already. Now when traversing if we find a value for which the index abs(value)-1  is negative we can say we have already seen this value before hence the value in that index is already negative. 
#the time complexity is O(n) as we traverse thru the array once and space complexity is constant O(1)


def secondMethod(arr):
    seen = set()
    for value in arr:
        if value in seen:
            return value
        seen.add(value)
    return -1
        
def thirdMethod(arr):
    for value in arr:
        index = abs(value)-1
        if arr[index] < 0:
            return abs(value)
        else: 
            arr[index] *= -1
    return -1

def main():
    
    array = [2,1,5,2,3,3,4]
    
    # result = secondMethod(array)
    result = thirdMethod(array)
    
    print('the first duplicate value is:', result)

if __name__ == "__main__":
    main()
    