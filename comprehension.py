numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
print(f"Even numbers are {even} and odd numbers are {odd}")

#convert the first letter of fruits to uppercase and store them in another list
fruits = ['apple', 'banana', 'cherry', 'date']
for i in range(len(fruits)):
    fruits[i] = fruits[i].capitalize()
print(fruits)