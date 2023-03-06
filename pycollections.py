'''
The collections module is a built-in module in Python that provides alternatives to the built-in data types like list, dict, set, and tuple. It offers additional data structures that are specialized and optimized for specific use cases.

Some of the common data structures provided by the collections module include:

namedtuple: A factory function that creates a tuple subclass with named fields.

deque: A double-ended queue implementation that allows fast appends and pops from both ends.

Counter: A dictionary subclass that counts the occurrences of elements in a sequence.

OrderedDict: A dictionary subclass that remembers the order in which its items were added.

defaultdict: A dictionary subclass that calls a factory function to provide default values for missing keys.
'''
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'email'])
#first arg is name of tuple, second list of args is name of fields
#can be used in place of simple classes
p = Person(name='John', age=30, email='john@example.com')
print(p.name) # 'John'
print(p.age)  # 30
print(p.email) # 'john@example.com'

#deque is a double ended queue, you can add and remove elements from either side
#add elements: append(right) and appendleft
#remove elements: pop(right) and popleft
#extend and extendleft to add all the elements of an iterable to the deque
#rotate(n) rotates the deque to the right by n steps
from collections import deque

queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
queue
print(queue.popleft()) # 'A'
print(queue.popleft()) # 'B'
print(queue.popleft()) # 'C'

from collections import Counter

sentence = "The quick brown fox jumps over the lazy dog"
word_count = Counter(sentence.split())
print(word_count) # Counter({'The': 1, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog': 1})

from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d) # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

from collections import defaultdict

sentence = "The quick brown fox jumps over the lazy dog"
letter_count = defaultdict(int)
for letter in sentence:
    letter_count[letter] += 1
print(letter_count) # defaultdict(<class 'int'>, {'T': 1, 'h': 2, 'e': 3, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 2, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 't': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1})

#more info about counter:
'''
counter is used to count the frequency of elements in a list. 
it can work on list, tuple or any other iterable
'''
from collections import Counter

l1= [int(i) for i in '1 3 4 2 2 1 4 1 4 5 2 61 3 1 1 3 2 5 8 8 9'.split()]
cntr = Counter(l1)
print(list(cntr))
#Output: 1 3 4 2 2 1 4 1 4 5 2 61 3 1 1 3 2 5 8 8 9 
#Counter({1: 5, 2: 4, 3: 3, 4: 3, 5: 2, 8: 2, 61: 1, 9: 1})
#it returns a counter object, with decreasing value of counts

'''
more counter methods:
cnt.most_commmon(n) -> returns n most common elements, along with the number of occurences
if n not defined, returns entire cntr list, with all elements and their frequencies, in decreasing order.
'''
print(cntr.most_common(3))
#output: [(1, 5), (2, 4), (3, 3)]
print(cntr.most_common())