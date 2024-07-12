# tandem bicycle is operated by 2 person (one red shirt and one blue short)
# fastest speed of the 2 person is the max speed of the bicycle -> max(r,b)
# slowest speed of the 2 person is the min speed of the bicycle -> min(r,b)

# redShirtSpeeds=[5,5,3,9,2]
# blueShirtSpeeds=[3,6,7,2,1]
#fastest = true/false

# Q/A - we need to pair the red and blue shirt to get Maximum(fastest=true) or Minimum(fastest=false) total speed

# Trick - 
# To get the maximum total speed (fastest=true), sort both arrays, and we need to pair the highest speed from one color and slowest speed from another, and do same for left pairs..like [9,1], [2,7]
# To get the minimum total speed (fastest=false),sort both arrays and reverse one of them, and we need to pair the highest speed from one color and highest speed from another, and do same for left pairs..like [9,7], [6,5]


# TIME COMPLEXITY - O(n log n) 



def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    
    if not fastest:
        reverseArrayInPlace(redShirtSpeeds) #we can also use built in reverse=true in sort()
        
    print(redShirtSpeeds)
    print(blueShirtSpeeds)
        
    totalSpeed = 0
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx] #iterating red short array from start end
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds)-idx-1] #iterating red short array from rear end
        
        totalSpeed = totalSpeed + max(rider1, rider2)
        
    return totalSpeed
        
    
def reverseArrayInPlace(array):
    start = 0
    end = len(array) - 1
    while start < end :
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
        
    


def main():
    print("Hello World!")
    
    
    redShirtSpeeds=[5,5,3,9,2]
    blueShirtSpeeds=[3,6,7,2,1]
    
    fastest_input = input("Check Maximum total speed? (y/n): ")
    if fastest_input.lower() == 'y':
        fastest = True
    else:
        fastest = False
    
    totalSpeed = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
    
    print('fastest = ', fastest)
    print(f"Total {'maximum' if fastest else 'minimum'} speed of all bicycle: {totalSpeed}")
    

if __name__ == "__main__":
    main()

        
        
        
        