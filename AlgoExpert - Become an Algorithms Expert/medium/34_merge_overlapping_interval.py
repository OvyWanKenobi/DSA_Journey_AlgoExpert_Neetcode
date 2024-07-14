# array = [[1,2], [3,5], [4,7], [6,8], [9,10]]

# 1,2   3, 4,5  4,5,6,7   6,7,8   9,10
#         |overlaps||overlaps|   

# we need to make a new output array with no overlapping 

# time- complexity : O(n)
# space complexity : O(n)


def merge_overlapping_interval(array) : 
    
    arr = sorted(array, key=lambda x: x[0])
    
    output = []
    for i in range(len(arr)):
        if i == 0 :
            output.append(arr[i])
        elif (arr[i][0] > output[-1][1]) and (arr[i][1] > output[-1][1]):
            output.append(arr[i])
        elif (arr[i][0] <=  output[-1][1]): #if overlaps keep the last output[0] same and update the output[1] with whatever the max between current arr[1] and last output[1]
            output[-1][1] = max(output[-1][1], arr[i][1])
        print(output)
            
    return output
    
    
    
def main():
    array = [[1,2], [3,5], [4,7], [6,8], [9,10]]
    # array = [[1,2], [3,5], [2,4], [6,8], [9,10]]
        
    output = merge_overlapping_interval(array)
    
    print(output)
    
    
if __name__ == '__main__':
    main()