'''
basic list comprehension:
 newlist = [expression for item in iterable]
expression : any operation or function that is to be performed on each item of the iterable
item: placeholder that will represent a single element in the list/dict/tuple
iterable: list/set/dict/tuple
'''
sq_10 = [i**2 for i in range(1,10)]

myset = set([i%10 for i in range(100)])

print(sq_10)
print(myset)

'''
list comprehension with conditionals:
[expression for item in iterable if condition]
for if and else:
[exp1 if cond1 else exp2 for item in iterable]
'''
#eg1, only if
oddnums = [i for i in range(10) if i%2!=0]
#eg2, if and else
oddevlist = [f'{i} is even' if i%2==0 else f'{i} is odd' for i in range(10)]
print(oddnums)
print(oddevlist)

'''
list comprehension with nested loops:
newlist = [expression for outer_loop for inner_loop in iterable if condition]
'''
list1 = [1,2,3]
list2 = [4,5,6]
newlist = [(a,b) for b in list2 for a in list1]
print(newlist)
#output:[(1, 4), (2, 4), (3, 4), (1, 5), (2, 5), (3, 5), (1, 6), (2, 6), (3, 6)]
#a changes first due to inner loop, then b gets changed

'''
creating dictionary using list comprehension
new_dict = {key_expression: value_expression for item in iterable if condition}
'''
wordlist = 'hello my name is ameya'.split()
mydict = {word:len(word) for word in wordlist}
print(mydict)

'''
Basic list methods:

append(item) - Adds an item to the end of the list.
'''
lst = [1, 2, 3]
lst.append(4)
print(lst) # [1, 2, 3, 4]
#extend(iterable) - Adds all the elements of an iterable to the end of the list.


lst = [1, 2, 3]
lst.extend([4, 5])
print(lst) # [1, 2, 3, 4, 5]
'''
insert(index, item) 
Inserts an item at the specified index in the list.
'''

lst = [1, 2, 3]
lst.insert(1, 4)
print(lst) # [1, 4, 2, 3]

'''
remove(item) 
Removes the first occurrence of an item from the list.
'''


lst = [1, 2, 3, 2]
lst.remove(2)
print(lst) # [1, 3, 2]
'''
pop(index) - Removes and returns the item at the specified index. If no index is specified, removes and returns the last item in the list
'''


lst = [1, 2, 3]
popped = lst.pop(1)
print(popped) # 2
print(lst) # [1, 3]
'''
clear() - Removes all the items from the list.
'''

lst = [1, 2, 3]
lst.clear()
print(lst) # []
'''
index(item) -# Returns the index of the first occurrence of an item in the list. Raises a ValueError if the item is not found.'''


lst = [1, 2, 3]
idx = lst.index(2)
print(idx) # 1

'''
count(item) - Returns the number of occurrences of an item in the list.
'''

lst = [1, 2, 3, 2]
cnt = lst.count(2)
print(cnt) # 2
# sort(key=None, reverse=False) - 
#Sorts the items in the list in ascending order. The optional key parameter specifies a function to be called on each item to determine its sort order, and the optional reverse parameter specifies whether to sort the list in descending order.


lst = [3, 2, 1]
lst.sort()
print(lst) # [1, 2, 3]


lst = ["ccc", "bb", "a", "dddd"]

lst.sort(key=len, reverse=True)
print(lst) # ['dddd', 'ccc', 'bb', 'a']
'''
reverse() - Reverses the order of the items in the list.
'''

lst = [1, 2, 3]
lst.reverse()
print(lst) # [3, 2, 1]

