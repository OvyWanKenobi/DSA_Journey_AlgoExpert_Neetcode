# [-1 , -5 , -10, -1100, -1100, -1101 , -1102 , -9001]

# monoatomic mean, a array is following a direction (increase or decrease) and there is no change in opposite direction
# but monoatomic can have duplicates meaning there can be flat, but it can not go up once it go down , or vice versa
#it is like proofing the array is sorted(can be reserve) or not

#so first we need to determine the direction. After that we need to check by comparing two numbers and move thru array

# Time complex is O(n) and space is O(1)


# def monotonicArray(arr):
    
#     direction = None

#     for i in range(len(arr)-1):  
#         if direction == None:
#             if(arr[i] == arr[i+1]):
#                 continue
#             else:
#                 if arr[i] < arr[i+1]:
#                     direction = 'increasing'
#                 else:
#                     direction = 'decreasing'
#         else:
#             if( arr[i] > arr[i+1] and direction == "increasing"):
#                  return False
#             if( arr[i] < arr[i+1] and direction == "decreasing" ):
#                  return False
#     return True



#we check if array is non decreasing or is non increasing, 
#we will first say is both non decreasing and non increasing, until we find a direction change
#we will make isNonDeceasing false, if i is greater than i+1 , meaning it is decreasing
#we will make isNonIncreasing false, if i is smaller than i+1, meaning it is inceasing
#only one can be false at the end. If both are false, meaning there is ups and downs
#if both remained true, meaning the array is constant, which is also monotonic

def monotonicArray(arr):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]: #increasing
            isNonDecreasing = False #NOT non decreasing
        if arr[i] > arr[i+1]: #decreasing
            isNonIncreasing = False #NOT non increasing
    return isNonDecreasing or isNonIncreasing
    
def main():
    
    array =  [-1 , -5 , -10, -1100, -1100, -1101 , -1102 ,  -9001]
    # array = [9,9,9,8,7,6,5,4,4,4,4,4,3,2,1]
    # array = [1,1,1,3,3,3,5,6,7,9,9,9]
    
    result = monotonicArray(array)
    
    print(result)
    
    
    
if __name__ == '__main__':
    main()