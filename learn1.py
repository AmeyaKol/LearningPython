#DICTIONARIES IN PYTHON: a dict is a list of key value pairs, works similar to set, the values are indexed using the keys
capitals = { 'USA': 'Washington DC', 'India': 'Delhi', 'Japan': 'Tokyo'}
# print(capitals.keys())
# print(capitals.values())
print(capitals['India'])
#dictionaries are like keys, where the individual elements are not linearly indexed, but are indexed using keys
print(capitals.get('Germany')) 
capitals.update({'Germany':'Berlin'})
# we can use update to add extra elements to the dictionary, or change values for existing keys
#using get is safer than using indexing, as it will return none if the key is not present
for keys,values in capitals.items():
    #items is a list of keys and values together
    print(keys,values,'.')
#dictionaries use hashing and allow us to access values quickly

# SETS IN PYTHON: sets are unordered and unindexed, they don't allow duplicate values
set1  = {3,4,3,44,5,6,7,2}
print(set1)
set1.add(17) # adds element to set
set1.remove(44) #removes element from set.
set2 = {3,4,5,56,436,92,1}
for i in set2:
    print(i,end=" ")
# set1.update(set2) #update adds all elements of set2 to set1
print(set1)
print(set1.union(set2)) # prints all elements either in set1 or set2 or both
print(set1.difference(set2)) #prints elements in set1 but not in set2
print(set1.intersection(set2)) # only prints elements present in both set1 and set2
set2.clear() # will clear set2 or remove all elements from set2

set3 = {3,4,5,67,22,323,11,2}
set4 = {2,3,11,5,9,55,76}
print(set3.symmetric_difference(set4))
print(set3.union(set4).difference(set3.intersection(set4))) 
# relation between sym diff, intersection and union
# a sym diff b = a union b - a intersection b


#KEYWORD ARGUMENTS FOR FUNCTIONS

def func(fname,lname):
    print("Hello",fname,lname)
func('kolhatkar','ameya') #these are positional arguments, changing their order changes the output
func(fname='ameya',lname='kolhatkar') #these are keyword arguments, they can be specified in any order within the function call
#and the result of the function will remain the same

#SCOPE OF A VARIABLE
# variable has 4 scopes: local, enclosed, global, in built
# it will look for definition in this order
# if variable finds defined value within local scope
# , that will be the value of the variable in that scope
name = "Bob"
def disp():
    name = "John"
    print(name)
disp() #here, it will use the local variable value of name
print(name) # here, it will use the global value of name

#ARGS:
#args are used when it is unkown how many arguments a function can receive
# *args will be used to accept variable number of arguments
# here, we are using * to indicate that we are PACKING the arguments into a tuple
# as tuples are iterable, we can use this tuple of arguments inside the function
def findsum(*args): # we can rename *args as *whatever_you_want
    #the * is important as it indicates we are packing arguments into a tuple
    sum=0
    for i in args:
        sum += int(i)
    print(sum)
findsum(1,2,3,4,'5','7')

