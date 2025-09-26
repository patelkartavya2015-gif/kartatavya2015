# Reverse a number in Python

num = int(input("Enter a number: "))

# Method 2: Using mathematics
rev = 0
n = num
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
print("Reversed Number:", rev)
