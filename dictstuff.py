# create a new dictionary
my_dict = {"apple": 2, "banana": 3, "cherry": 5}

# dict.clear()
my_dict.clear()
print(my_dict) # Output: {}

# dict.copy()
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
new_dict = my_dict.copy()
print(new_dict) # Output: {"apple": 2, "banana": 3, "cherry": 5}

# dict.fromkeys(seq[, value])
keys = ["a", "b", "c"]
values = 0
new_dict = dict.fromkeys(keys, values)
print(new_dict) # Output: {"a": 0, "b": 0, "c": 0}

# dict.get(key[, default])
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
value = my_dict.get("banana", 0)
print(value) # Output: 3

# dict.items()
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
items = my_dict.items()
print(items) # Output: [("apple", 2), ("banana", 3), ("cherry", 5)]

# dict.keys()
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
keys = my_dict.keys()
print(keys) # Output: ["apple", "banana", "cherry"]

# dict.pop(key[, default])
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
value = my_dict.pop("banana", 0)
print(value) # Output: 3
print(my_dict) # Output: {"apple": 2, "cherry": 5}

# dict.popitem()
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
key, value = my_dict.popitem()
print(key, value) # Output: "cherry", 5
print(my_dict) # Output: {"apple": 2, "banana": 3}

# dict.setdefault(key[, default])
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
value = my_dict.setdefault("banana", 0)
print(value) # Output: 3
value = my_dict.setdefault("orange", 0)
print(value) # Output: 0
print(my_dict) # Output: {"apple": 2, "banana": 3, "cherry": 5, "orange": 0}

# dict.update([other])
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
other_dict = {"banana": 4, "durian": 7}
my_dict.update(other_dict)
print(my_dict) # Output: {"apple": 2, "banana": 4, "cherry": 5, "durian": 7}

# dict.values()
my_dict = {"apple": 2, "banana": 3, "cherry": 5}
values = my_dict.values()
print(values) # Output: [2, 3, 5]
