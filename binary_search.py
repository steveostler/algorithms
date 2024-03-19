def binary_search(arr, item):
    # low and high keep track of which part of the list you'll search in
    low = 0
    high = len(arr)-1

    while low <= high: # while not narrowed down to 1 element
        mid = (low + high) // 2 # check the middle element
        guess = arr[mid]
        if guess == item: # found the item
            return mid
        elif guess > item: # too high
            high = mid - 1
        else:
            low = mid + 1 # too low
    return None # does not exist

my_list = [1,3,5,7,9,11]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))