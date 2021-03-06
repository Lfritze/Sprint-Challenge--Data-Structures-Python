# (Hint: You might try importing a data structure you built during the week)

import time

from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# grab the first name to start tree
bst = BSTNode(names_1[0])

# insert the rest from first file into the tree
for name in names_1[1:]:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


end_time = time.time()
print(
    f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds*******Logarithmic Time******")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

stretch_duplicates = []
start_time = time.time()
cache = {}
for name in names_1:
    if name not in cache:
        cache[name] = name

for name in names_2:
    if name in cache:
        stretch_duplicates.append(name)

end_time = time.time()
print(
    f"\n\n{len(stretch_duplicates)} duplicates:\n\n{', '.join(stretch_duplicates)}\n\n")
print(f"runtime: {end_time - start_time} ***********STRETCH is FASTER**********")