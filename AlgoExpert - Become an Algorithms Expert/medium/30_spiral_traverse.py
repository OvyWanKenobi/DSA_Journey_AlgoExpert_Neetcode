#       startCol       endCol
# startRow  1   2   3   4
#           12  13  14  5
#           11  16  15  6 
#  endRow   10  9   8   7

# here we need to go spiral in the 2d array like 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

# time complexity is o(N) where N is size of 2d array row x col , as we traverse thru each items once
# space complexity is o(N)

def spiralTraverse(array):
    result = []
    startRow = 0 
    endRow = len(array)-1
    startCol = 0
    endCol = len(array[0])-1
    
    while(startRow <= endRow) and (startCol<= endCol):
        
        for col in range(startCol, endCol+1):
            result.append(array[startRow][col])
        for row in range(startRow+1, endRow+1):
            result.append(array[row] [endCol])
        for col in reversed(range(startCol, endCol)):
            result.append(array[endRow] [col])
        for row in reversed(range(startRow+1, endRow)):
            result.append(array[row][startCol])
            
        startRow+=1
        endRow-=1
        startCol+=1
        endCol-=1
    
    return result


def main():
    
    # array =  [[1,2,3,4] , [12,13,14,5], [11,16,15,6], [10,9,8,7]]
    array =  [[1,2,3,4,5] , [16,17,18,19,6], [15,24,25,20,7], [14,23,22,21,8] , [13,12,11,10,9] ]
    
    result = spiralTraverse(array)
    
    print(result)
    
    
    
if __name__ == '__main__':
    main()