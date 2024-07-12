
# [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
# in here we need to find the longest peak.  A peak is set of numbers which initially will strictly increase and reach a peak and strictly decrease. 
# for example, here it went 0 to 10 and then decrease with 6,5,-1,-3 until it went up with 2 again.
# So 0,10,6,5,-1,-3 is the set of the longest peak, and so longest peak is 6
# For a peak to be consider minimum 3 numbers are needed like 3 4 0
# a platuea is not considered peak, like in 1 2 3 3 , it was increaseing but a constant hit when 3 3

# time complexity -  O(n) as we  go thru each item in array once
# space complex - O(1) always same variables no matter how big array

def longestPeak(arr):
    
    longestPeakFound = 0
    peakFound=False
    potentialLongPeak = 1
    
    for i in range(1, len(arr)-1):
        
        # print('current',arr[i])

        if(peakFound == False):
            
            if(arr[i-1] < arr[i]):
                potentialLongPeak += 1
                # print('potential',potentialLongPeak)
            elif((arr[i-1] > arr[i]) and (potentialLongPeak>1)):
                peakFound = True
                # print('peakfound', peakFound)
                potentialLongPeak += 1
                # print('potential',potentialLongPeak)
            elif((arr[i-1] == arr[i])):
                potentialLongPeak = 1
                # print('potential',potentialLongPeak)
  
        elif (peakFound == True):
            if((arr[i-1] < arr[i]) or (arr[i-1] == arr[i])):
                peakFound = False
                # print('peakfound', peakFound)
                if(longestPeakFound < potentialLongPeak and potentialLongPeak >= 3):
                    longestPeakFound = potentialLongPeak
                    # print('longestpeakfound', longestPeakFound)
                potentialLongPeak = 2
                # print('potential',potentialLongPeak)
            elif((arr[i-1] > arr[i]) ):
                potentialLongPeak += 1
                # print('potential',potentialLongPeak)

    return longestPeakFound

            

def main():
    array = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
    # array = [1,2,3,4,5,6,7,8,8,8,6,4,3,2,4,0,10,2,3]
    # array = [1,2,3,3,4,5,6,3,2,1,0,-5,-6,-9,10,6,5,-3,2,3]
    
    result = longestPeak(array)
    
    print('result',result)

if __name__ == "__main__":
    main()