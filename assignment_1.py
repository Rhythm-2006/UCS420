# Assignment 1.1: WAP to print your name three times
name = input("Enter your name: ")
for i in range(3):
    print(name)

# Assignment 2.1: WAP to add three numbers and print the result
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
print("Sum of three numbers is:", num1 + num2 + num3)

# Assignment 2.2: WAP to concatenate three strings and print the result.
a = input("Enter first string: ")
b = input("Enter second string: ")
c = input("Enter third string: ")
print("Concatenated string =", a + b + c)

# Assignment 4.1: WAP to print the table of 7, 9.
for n in (7, 9):
    for i in range(1, 11):
        print(n, "*", i, "=", n * i)
    print()

# Assignment 4.2: WAP to print the table of n and n is given by user.
n = int(input("Enter n: "))
for i in range(1, 11):
    print(n, "*", i, "=", n * i)

# Assignment 4.3: WAP to add all the numbers from 1 to n and n is given by user.
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)

# Assignment 5.1: WAP to find max among three numbers and input from user. Try max() function.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Maximum =", max(a, b, c))

# Assignment 5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n and n is given by the user.
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    if i % 7 == 0 and i % 9 == 0:
        total += i
print("Sum =", total)

# Assignment 5.3: WAP to add all prime numbers from 1 to n and n is given by the user.
n = int(input("Enter n: "))
total = 0
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        total += num
print("Sum of prime numbers =", total)

# Assignment 6.1: WAP using function that add all odd numbers from 1 to n, n is given by the user.
def sum_odd(n):
    return sum(range(1, n + 1, 2))

n = int(input("Enter n: "))
print("Sum of odd numbers =", sum_odd(n))

# Assignment 6.2: WAP using function that add all prime numbers from 1 to n, n given by the user.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_primes(n):
    total = 0
    for num in range(2, n + 1):
        if is_prime(num):
            total += num
    return total

n = int(input("Enter n: "))
print("Sum of prime numbers =", sum_primes(n))
