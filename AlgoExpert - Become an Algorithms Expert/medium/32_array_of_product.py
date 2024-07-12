     
# [5,1,4,2] -> [8,40,10,20]
# here we need to make a new result array which will have the product of other index in a index.
# for example at index 0 , we will product 1x4x2 and put 8 in the result array


# there are few approch. 1st way is brute force , which is non-optimum  and has time complexity of O(n^2) as we have two forloop and space complex is O(n) as we need to create a new output array

def arrayOfProducts_bf(arr):
    
    result = []
    
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if(arr[j] != arr[i]):
                product *= arr[j]  
        result.append(product)
    
    return result


# optimum way

def arrayOfProducts(arr):
    
    products= [1 for _ in range(len(arr))]
    
    leftRunningProduct = 1
    for i in range(len(arr)):
        products[i] = leftRunningProduct
        leftRunningProduct *= arr[i]
    
    rightRunningProduct = 1
    for i in reversed(range(len(arr))):
        products[i] = products[i] * rightRunningProduct
        rightRunningProduct *= arr[i]
    
    
    return products
        
        
def main():
    array = [5,1,4,2]

    # result = arrayOfProducts_bf(array)
    result = arrayOfProducts(array)
    
    print('result',result)

if __name__ == "__main__":
    main()