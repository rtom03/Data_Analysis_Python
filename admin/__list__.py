
# list unpacking
number = [1, 2, 3, 4, 5, 4]

first, sec, *other = number

print(first, sec, other)


# looping over list

letters = ['a', 'b', 'c']

for index, letter in enumerate(letters):
    print(letter)


# adding items

letter = ['a', 'b', 'c']
letter.append('d')
print(letter)


items = [
    ("product1", 9),
    ("product1", 10),
    ("product1", 11),
]

items.sort(key=lambda x: x[1])
print(items)

# map

items = [
    ("product1", 9),
    ("product1", 10),
    ("product1", 11),
]

x = list(map(lambda x: x[1], items))

print(x)


# filter

x = list(filter(lambda x: x[1] >= 10, items))
print(x)


# list comprehension
prices = [x[1] for x in items]
print(prices)


# zip function

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))
