

def runLineEncoding(string):
    encodedStringCharacters = []
    currentRunLength = 1
    
    for i in range (1, len(string)) :
        
        currentChar = string[i]
        previousChar = string[i-1]
    
        if  currentChar != previousChar or currentRunLength == 9 :
            
            
            
            encodedStringCharacters.append(str(currentRunLength)) #it is integer
            encodedStringCharacters.append(previousChar)
            currentRunLength = 0
            # print(encodedStringCharacters)
            
        currentRunLength += 1
        
        
    encodedStringCharacters.append(str(currentRunLength)) #it is integer
    encodedStringCharacters.append(string[len(string)-1])
    
    return "".join(encodedStringCharacters)
    
    
def main():
    
    string =  "aaaaaaaabbbbbbbcccccddddee"
    
    encoded = runLineEncoding(string )
    
    print(encoded)
    
    
if __name__ == '__main__':
    main()
    
    

        
        
        
        
            
    