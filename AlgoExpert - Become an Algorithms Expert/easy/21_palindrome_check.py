
# abcdcba 
# a palindrome will read same from forward and backward

# there are many methods to check if a string is palindrome or not. SOme are more optimum than other


# 1st method -  
# we make a new reversed string and check if they are equal

# space complexity is O(n) as we create a new n size string
#time complexity is O(n^2) as newtring += string[i] , we go thru all the char of newString everytime we add new char to it. hence NxN

def isPalindrome_1(string):
    newtring = ""
    for i in reversed(len(string)):
        newString += string[i]
    
    return string == newString


# 2nd Merhod :
# similar, but we use append function 
# space complexity is O(n) as we create a new n size string
#time complexity is O(n) as append is constant addition and do not go thru all the chars when a new char is appended. So only once 'N'. 

def isPalindrome_2(string):
    newChars = []
    for i in reversed(len(string)):
        newChars.append(string[i])
    return string == "".join(newChars) #joins all the chars into a string



# 3rd Method :
# this is done by recursion.  We check if first and last element matches, and again check the same for middle elements using recursion  and keep going until hit  base case.

# space complexity is O(n) as we create call stacks due to recursion 
#time complexity is O(n) as we going thru half the string, so N/2 or (1/2)N , which is O(N) (1/2 is constant)

def isPalindrome_recur(string, i=0):
    j = len(string) - 1 - i
    
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome_recur(string, i+1)



    
    
#4th method : [optimum]
# iterative solution. do not use recursion 
# the space complexity is O(1) , as only space we need are for left and right idx, which are constants
# time complexity is O(n)

def isPalindrome_iter(string):
    leftidx = 0 
    rightidx = len(string)-1
    
    while leftidx < rightidx :
        if(string[leftidx] != string[rightidx]):
            return False
        
        leftidx +=1
        rightidx -= 1
            
    return True




def main():
    
    string =  "12345854321"
    
    isPalindrome = isPalindrome_iter(string )
    
    print(isPalindrome)
    
    
if __name__ == '__main__':
    main()
    
    
