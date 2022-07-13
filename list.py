"""List(Array) Tutorial"""

from copy import deepcopy


fruits = ["banana", "apple"]
print("ORIGINAL fruits: ", fruits)

fruits3 = fruits
fruits3.append("watermelon")
print("fruits3: ", fruits3)
print("fruits: ", fruits)
# this resulting in fruits3 to be a pointer to fruits
# hence when we append 'watermelon' to fruits 3,
# we also append to fruits

fruits2 = deepcopy(fruits)
fruits2.append("oranges")
print("fruits2: ", fruits2)
print("fruits: ", fruits)

fruits.sort()
print("sorted fruits: ", fruits)

last_item = fruits.pop()
print("last item: ", last_item)
print("fruits: ", fruits)

for index, item in enumerate(fruits2):
    print(index, item)
