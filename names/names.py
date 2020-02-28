import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#runtime: 0.14162158966064453 seconds 
duplicates = []  # Return the list of duplicates in this data structure

bsTree = BinarySearchTree (names_1[0])

# loop through names_1, insert names in tree
for name in names_1:
    bsTree.insert(name)

# loop through names_2, checking if tree contains the name. If it does, add to duplicates 
for name in names_2:
    if bsTree.contains(name):
        duplicates.append(name)

# Replace the nested for loops below with your improvements
# Runtime is O(n^2) runtime: 10.204684495925903 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
