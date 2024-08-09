temperature = 35

if temperature > 36:
    print('Its Warm')
elif temperature < 40:
    print('Its Nice')
print('Done')


age = 22

# if age >= 18:
#     message = 'Eligible'
# else:
#     message = 'Not Eligible'
# Ternary operator
message = 'Eligible' if age >= 18 else 'Not Eligible'
print(message)


# logical three logical operator and or not

high_income = True
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print('Eligible')
else:
    print('Not Eligible')

# for loops

for number in range(1, 4):
    print('Attempted', number * '.')
# for else
succesful = False
for number in range(3):
    print('Attempt')
    if succesful:
        print('successful')
        break
else:
    print('attempted failed', number+1)
# nested loops

for x in range(5):
    for y in range(3):
        print(x, y)

# iterables


# while loop
def greet():
    print('Hello')
    print('Welcome Aboard')


greet()
