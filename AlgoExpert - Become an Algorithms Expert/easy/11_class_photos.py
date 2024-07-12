
#  there are students of red shirts and blue shirts, each students has different heights, we need to take photo in two rows such a way, the first row students and shorter than the second row students, so everyone is seen
 
#  redShirt = [5,8,1,3,4]
#  blueShirt = [6,9,2,4,5]
 
#  First we need to sort the red and blue students, second we need to find with color has the tallest student, which will go in second row. After that than compare for a index(column) the second row student is taller than 1st row or not.


def classPhoto (redShirtHeights, blueShirtHeights):
    
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    

    
    shirtColorInFirstRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
    
    if shirtColorInFirstRow == 'RED':
        
        print("Blue: ",blueShirtHeights)
        print("Red: ",redShirtHeights)

    
    if shirtColorInFirstRow == 'BLUE':
        
        print("Red: ",redShirtHeights)
        print("Blue: ",blueShirtHeights)

    
    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]
        
        if shirtColorInFirstRow == 'RED':
         
            if redShirtHeight > blueShirtHeight:
                return False
        
        if shirtColorInFirstRow == 'BLUE':
    
            
            if blueShirtHeight > redShirtHeight:
                return False
            
    return True


def main():
    print("Hello World!")
    
    
    redShirtHeights = [5,8,1,3,4]
    blueShirtHeights = [6,9,2,4,5]
    
    classPhotoPossible = classPhoto(redShirtHeights, blueShirtHeights)
    
    print("Class Photo Possible :", classPhotoPossible)
    

if __name__ == "__main__":
    main()

        
        
        
        