# Code your solution here
list_dup = ['a', 'b', 'a', 'c', 'b']

tot = dict((i, list_dup.count(i)) for i in list_dup)
print(tot)