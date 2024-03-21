### Binary search
This has to be sorted first and is fast O(log n)

### Selection sort
Selection sort is a neat algorithm but it's not very fast. It takes O(n x n) time. Quicksort is faster

### Recursion
* Recursion is when a function calls itself.
* Every recursive function has two cases: the base case and the recursive case.
* A stack has two operations push and pop.
* All function calls go onto the call stack.
* The call stack can get very large, which takes up a lot of memory.

### Divide and Conquer
* D&C works by breaking a problem down into smaller and smaller pieces. If you're using d&C on a list, the base case is probably an empty array or an array with one element.
* If you're implementing quicksort, chhose a random element as the pivot. The average runtime of quicksort is O(n log n)!
* Given two algorithms with same big O running time, one can be consitently faster than the other. That's why quicksort is faster than merge sort.
* The constant almost never matters for simple search versus binary search because O(log n) is so much faster than o(n) when your list gets big.

### Hash Tables
Hash tables are good for
* Modeling relationships from one thing to another thing
* Filtering out duplicates
* Caching/memorising data instead of making server do the work
* You'll almost never have to implement a hash table yourself. The programming language shouldprovide an implementation for you. you can use python's hash tables and assume you'll get the average-case performance: constant time
 

