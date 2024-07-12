

# Time Complexity - O(n+m)  , n for going thru characters string and m for going thru document string
#space complexity - O(c) , space name for characterCount which number of unique character in characters string

def generateDocument(characters, document):
    characterCounts = {}
    
    for character in characters:
        
        if character not in characterCounts:
            
            characterCounts[character] = 0
        
        characterCounts[character] += 1
        
    
    for character in document:
        
        if character not in characterCounts  or characterCounts[character] == 0 :
            return False
        
        characterCounts[character] -= 1
        
    return True



def main():
    
    characters = "rqnay svihmaR hAuO"
    document =  "Ashiqur Rahman Ovy"
    
    matches = generateDocument(characters, document)
    
    print(matches)
    
    
if __name__ == '__main__':
    main()

            
            
            