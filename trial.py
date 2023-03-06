l1 = ['a','b','c']
mydict = dict.fromkeys(l1,0)
print(mydict)
mydict.pop('a')
print(mydict)
mydict.setdefault('b',5)
# b already exists, it doesn't update its value.
# if i added a new key, it would create key value pair and add it 
print(mydict)
mydict.update([['c',1],['d',2],['e',3]])
#takes an iterable, each element of iterable must be key-value or a tuple, and adds them to the dictionary. if the key already exists, it will update the value
print(mydict)

x = input("Enter numbers")
numlist = list(map(int,x.split()))
print(numlist)