
def firstNonRepeatingCharacter(string):
    characterFrequencies ={}
    
    for character in string:
        characterFrequencies[character] = characterFrequencies.get( character, 0 )+1
        
    for idx in range(len(string)):
        
        character = string[idx]
        
        if characterFrequencies[character] == 1:
            return idx
        
    return False
        
        

def main():
    
    
    string =  "abcdeafdbe"
    
    firstNonRepeatIdx = firstNonRepeatingCharacter(string)
    
    if(firstNonRepeatIdx != False):
        print(f"first non repeat character is {string[firstNonRepeatIdx]} found at index {firstNonRepeatIdx}")
    else :
        print("no non repeating character found")
    
if __name__ == '__main__':
    main()

            