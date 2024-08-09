def greet(*num):
    total = 1
    for x in num:
        total *= x
    return total


print('start')
print(greet(1, 2, 3))
