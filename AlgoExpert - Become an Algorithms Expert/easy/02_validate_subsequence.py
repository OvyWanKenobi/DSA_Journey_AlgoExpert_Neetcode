

#subsquence is a valid sequence of element that can be derived from another, by deleting elements or keeping it same, but not changing the order

# Q/A - Validate if a subsequence is present in the main array
#main sequence - [ 5,1,22,25,6,-1,8,10] | subsequence - [1,6,-1,10]

#trick- first check if the first element present in main ,if not present, the sequence is not possible, return null | 
# we dont need to go backward in mai sequence as sequence matters, we keep looking forward in main sequence
# we only move forward in  sub sequence when a match found with main
 
 
 #1ST WAY - WHILE LOOP
 
def validateSequence_whileloop (arr, sequence):
    arrIdx = 0 
    subIdx = 0
    while (arrIdx < len(arr) and subIdx < len(sequence)):
        if (arr[arrIdx] == sequence[subIdx]):
            subIdx += 1
        arrIdx += 1
    return subIdx == len(sequence)  #returns true if subIdx reached the last and exceed the sub sequence , meaning all found in main arr


 
 #2nd WAY - for LOOP
 
def validateSequence_forloop (arr, sequence):
    subIdx = 0
    for num in arr :
        if (subIdx == len(sequence)) :
            return True
        if sequence[subIdx] == num :
            subIdx += 1 
    return subIdx == len(sequence)

# this iterates over the main array and checks if subidx reached last of sub sequence if not increase subidx


#BOTH THE METHOD IS SAME, HENCE # O(n) time | O(1) space - where n is the length of the array


def main():
    print("Hello World!")
    
    array = [ 5,1,22,25,6,-1,8,10]
    subseq = [1,6,-1,10]
    
    print(validateSequence_whileloop(array, subseq))
    print(validateSequence_forloop(array, subseq))

if __name__ == "__main__":
    main()

