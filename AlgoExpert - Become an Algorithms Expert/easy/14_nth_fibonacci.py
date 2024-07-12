
# if fibonacci series a nth number is addition of its previous 2 numbers in the series 

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 

# equation for nth fib , fib(n) = fib(n-1) + fib(n-2)  (when n>2)

#we can do it in three ways... One is better than their last one.

# 1st WAY  -
# if (n==1) we return 0 , as first number in fibonacci is 0
# if (n==2) we return 1 , as second number in fibonacci is 1
# else now of any other nth number except first two, we can add the previous 2 and achieve using recursion of fibonacci number, using fib(n) = fib(n-1) + fib(n-2) 
# Time Complexity - O(2^n) | Space - O(n)
#this take n space as some recursion is paused until there inner recursions is not complete. 
#also some recursion is repeated. for example, in a scenario fib(3) is called in fib(4) branch also and also in fib(5), and some other branches also of recursions.  we going through each fibonacci fib(n) more than once
# Hence this is not the OPTIMUM SOLUTION



# 2nd WAY (better than 1st way) :
# We keep a hash table(memorize) to memorize the recursions 
# We have fib(1)=0 and fib(2)=1 in hash table
# ANd whenever we go down the recursion tree, we save the output of a fib(n) value,
# For example, if we know the output of fib(5), we save it and use it in hash table, when ever we need it again for any other recursion branch like fib(7)=fib(6)+fib(5), we dont have to go more down with recursion for fib(5) 
#fib(5) will be then a constant operation, we dont have to fib(5)=fib(4)+fib(3)

# if n is memorize:
#     return memorize[n]
# else:
#     memorize[n] = fib(n-1) + fib(n-2)
#     return memorize[n]

#This method time complexity is O(n) as we going through each fibonacci fib(n) only once. ANd Space complexity is still O(n) as it still have the call stack issue



#3rd WAY - (OPTIMUM) - No recursion needed

# we take a array of size 2, and store first two number in fibonacci series-> [ 0 , 1]
#Now if we have find a nth fibonacci number we just need to find all the number in the series until we reach the nth number, 
# first we add the present numbers in array, array[0] + array[1] = NEXT, 
# and then replace the first index with second index, array[0] = array[1], and put the NEXT in array[1]
#and then we continue adding and removing first index, and putting NEXT in the array until we reach the nth fib

# This has time complexity of O(n) as we go through each fibs once till nth fib, | and Space comp of O(1) as we are not using recursion hence no call stack issue




def getNthFib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        lastTwo=[0,1]
        counter = 3
        while counter<=n:
            nextFib = lastTwo[0] + lastTwo[1]
            lastTwo[0]=lastTwo[1]
            lastTwo[1]= nextFib
            counter += 1
            
        return lastTwo[1]
    
      
      

def main():
    
    while True:
        try:
            nth = int(input("Enter nth of fibonacci series: "))
            if nth <= 0:
                print("Please enter positive integer number")
                continue
            
            break
        except ValueError:
            print("Invalid. Please enter valid Integer")
        
    nthFib = getNthFib(nth)
    
    print(nthFib)
   
    


if __name__ == "__main__":
    main() 