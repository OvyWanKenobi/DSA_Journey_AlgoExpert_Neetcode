# given two arrays:
# A - [-1,5,10,20,28,3]
# B- [26,134,135,15,17]
# we need to find out a pair of number, each from both arrays, which has the smallest diff

#first we need to sort both arrays. and put pointers on first index of each array
#now we compare them, and which ever pointer is smallest, we move the pointer of that array to right.
#and we log the smallest difference found
#continue till we reach the end of any array

# TIme complexity is O(n log(n) + m log(m)) where n and m is for traversing the both array and log() is for sorting 
# and space is O(1), as constant space is used



def smallestDifference(arrA, arrB) :
     
    arrA.sort()
    arrB.sort()
    
    pointerA = 0 
    pointerB = 0
    
    smallestPair = [arrA[pointerA], arrB[pointerB] ] #first differnce is smalled
    smallDiff = abs(arrA[pointerA] - arrB[pointerB]) 
    
    while ( pointerA < len(arrA) and pointerB < len(arrB)):
        
        diff = abs(arrA[pointerA] - arrB[pointerB])
       
        if (diff < smallDiff):
            smallDiff = diff
            smallestPair = [arrA[pointerA], arrB[pointerB] ]
            print(smallestPair, smallDiff)
        
        if (arrA[pointerA] < arrB[pointerB]):
            pointerA += 1
        elif (arrA[pointerA] > arrB[pointerB]):
            pointerB += 1
        else : 
            return smallestPair #difference is 0 
            
    return smallestPair



def main():
   arrayA = [-1,5,10,20,28,3]
   arrayB = [26,134, 135,15,17]
   
   smallestDiff = smallestDifference(arrayA, arrayB)
   
   print('smallest pair found:',smallestDiff)


if __name__ == "__main__":
    main()
    