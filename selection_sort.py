# Function to find the smallest element in an array

def findSmallest(arr):
    smallest = arr[0] # stores the smallest value
    smallest_index = 0 # stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    
# Now use this function to write selection sort
    
def selectionSort(arr):   # sorts an array
    newArr = []
    copiedArr = list(arr)  # copy array before mutating
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
    
