

# array = [141, 1, 17, -7, -17, =27, 18, 541, 8 , 7 , 7 ]

# for unsorted array we need to find the three largest number,
# what we do is we take a three size temp array [- ,- ,-] and traverse through the array and fill with largest number in array,
# if we find a number larger than a number in temp array, we shift the numbers from the tobereplaced index to the left and put the new larget number

# Time complex = O[n]
# SPace = O[1]

def threeLargestNumber(array):
    
    threeLargest = [None,None,None]
    
    for num in array:
        
        if threeLargest[2] is None or num > threeLargest[2]:
            shiftAndUpdate(threeLargest, num, 2)
            
        elif threeLargest[1] is None or num > threeLargest[1]:
            shiftAndUpdate(threeLargest, num, 1)
            
        elif threeLargest[0] is None or num > threeLargest[0]:
            shiftAndUpdate(threeLargest, num, 0)
    
    return threeLargest
            
            
def shiftAndUpdate(threeLargest, num, idx):
    
    for i in range(idx+1):
        if i == idx:
            threeLargest[i] = num
        else:
            threeLargest[i] = threeLargest[i+1]
            
    # print(threeLargest)
            
        
        
def main():
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8 , 7 , 1052 ]
    
    threeLargest = threeLargestNumber(array)
    
    print(threeLargest)
    
    
if __name__ == '__main__':
    main()
    
            
        
    