## find largest number in a list
numbers= [3,5,7,2,8,1,4]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print(largest)

## count vowels in a given string using a for loop.
string = "education"
vowels="aeiou"
count = 0
for i in string:
    if i in vowels:
        count=+1
        print(count)

## calculate the factorial of a number using a for loop.
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(factorial)

## count positive numbers in a list using a for loop.
numbers = [1, -2, 3, -4, 5]
count = 0
for n in numbers:
    if n > 0:
        count += 1
print(count)

##count negative numbers in a list using a for loop.
numbers = [1, -2, 3, -4, 5]
count = 0
for n in numbers:
    if n < 0:
        count += 1
print(count)

