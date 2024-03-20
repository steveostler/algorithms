def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

# recursive function to count the number of items in a list
def count(list):
    if list ==[]:
        return 0 
    return 1 + count(list[1:])

# recursive  function to find the maximum number in a list
def  max(list):
    if len(list) == 2:
        return list [0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(sum([1,2,3,4]))
print(count([1,2,3,4]))
print(max([3,6,2,5,99,2]))