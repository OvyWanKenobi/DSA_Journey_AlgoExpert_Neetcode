# [5, 2, [7, 1], 3, [ 6, [-13, 8], 4] ]

# product sum is adding all the element in the array
# here any deeper level array is consider an element, like [7,1],  and [ 6, [-13, 8], 4]
#inside these inner array there can be more levels of array like [-13,8] in [ 6, [-13, 8], 4]
# the more depth we go, we multiply the product sum with the depth
# for example, while knowing sum for [ 6, [-13, 8], 4] we multiply each with 2, and to find [-13, 8] we need to multiply with 3


# time is O(n) as it goes through array once, and space complexity is O(d) where d is levels of depth of resursion

def productSum(array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element , multiplier + 1)
        else:
            sum += element
     
    return sum * multiplier




def main():
    
    array = [5, 2, [7, -1], 3, [ 6, [-13, 8], 4] ]
    
    sum =productSum(array)
    
    print(sum)



if __name__ == "__main__":
    main() 