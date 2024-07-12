
# Q/A - in a given array of coins, what minimum change  you cant make with the coins
# like [5,7,1,1,2,3,22] - cannot make 20 with the coins

#we sort the array first, | then we keep adding each number to currentChange, what ever currentChange updates to we can make the change for each number up to that. 
#BUT IF a next number is greater than currentChange+1 , then we cant make change for currentChange+1. SO that should be the minimum chnage we cant not construct

def nonContructibleChange(coins):
    
    coins.sort()
    
    currentChange = 0
    
    for coin in coins:
        if coin <= currentChange+1 :
          currentChange = currentChange + coin
        else :
          return currentChange+1
      
    return currentChange+1 


#TIme comp = O(nlogn) | space comp = O(1)   || know that if we 


def main():
    print("Hello World!")
    
    coins = [5,7,1,1,2,3,22]
    print(nonContructibleChange(coins))

    #here in this example, 20 shall be the min non constructive change, as before the last index currentChange will be 19, and 19+1 is less than 22, Hence 19+1 is min non constructive change
    

if __name__ == "__main__":
    main()
