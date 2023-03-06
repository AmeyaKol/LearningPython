# create a new dictionary
my_dict = {"apple": 2, "banana": 3, "cherry": 5}

# dict.clear()
#removes all elements from the dictionary, but the variable my_dict still exists
my_dict.clear()
print(my_dict) # Output: {}

# dict.copy()
#creates a new dictionary object, copies an existing dictionary's data into the new object
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
new_dict = my_dict.copy()
print(new_dict) # Output: {"apple": 2, "banana": 3, "cherry": 5}

# dict.fromkeys(seq[, value])
#creates a new dictionary, takes an iterable as argument. all the elements in the iterable are set as keys, and each key is given the same corresponding value, which is equal to val
keys = ["a", "b", "c"]
values = 0
new_dict = dict.fromkeys(keys, values)
print(new_dict) # Output: {"a": 0, "b": 0, "c": 0}
newnewdict = dict.fromkeys(keys,keys)
print(newnewdict) # Output: {'a': ['a', 'b', 'c'], 'b': ['a', 'b', 'c'], 'c': ['a', 'b', 'c']}

# dict.get(key[, default])
# a safer version of dict[key], as it will return default value if key is not present, instead of a key not found exception
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
value = my_dict.get("banana", 0)
print(value) # Output: 3

# dict.items()
#returns a list of key-value tuples
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
items = my_dict.items()
print(items) # Output: [("apple", 2), ("banana", 3), ("cherry", 5)]

# dict.keys()
#returns a dict.keys() object, which contains a list of the keys
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
keys = my_dict.keys()
print(keys) # Output: dict_keys(['apple', 'banana', 'cherry'])
#this can be converted to a list simply by using list(keys)

# dict.pop(key[, default])
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
value = my_dict.pop("banana", 0)
print(value) # Output: 3
print(my_dict) # Output: {"apple": 2, "cherry": 5}
#pops element with given key, and returns the value. if the key dooesn't exist, returns default value

# dict.popitem()
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
key, value = my_dict.popitem()
print(key, value) # Output: "cherry", 5
print(my_dict) # Output: {"apple": 2, "banana": 3}
#popitem directly pops the last added item from the dictionary

# dict.setdefault(key[, default])
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
value = my_dict.setdefault("banana", 0)
print(value) # Output: 3
value = my_dict.setdefault("orange", 0)
print(value) # Output: 0
print(my_dict) # Output: {"apple": 2, "banana": 3, "cherry": 5, "orange": 0}
#setdefault: setdefault(key,def) will return the value associated wtih key, if the key exists in the dictionary. else it will retrn the default value

# dict.update([other])
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
other_dict = {"banana": 4, "durian": 7}
my_dict.update(other_dict)
print(my_dict) # Output: {"apple": 2, "banana": 4, "cherry": 5, "durian": 7}
#update will add a key if the key doesn't exist, and will update the value associated with the key if the key exists
#this is a safer way of doing dict[key]=

# dict.values()
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
values = my_dict.values()
print(values) # Output: [2, 3, 5]
