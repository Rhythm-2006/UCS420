import random

#QUESTION 1
roll_no = input("Enter your roll number: ")
L = [int(digit) * 10 for digit in roll_no]
print("L =", L)
L.append(50)
print("L after appending 50 =", L)
L.insert(2, 70)
print("After insert:", L)
L.remove(50)
print("After remove:", L)
L.pop()
print("After pop:", L)
L.sort()
print("Ascending order:", L)
L.sort(reverse=True)
print("Descending order:", L)
print(L[:3:1],L[7::1])
average = sum(L) / len(L)
L1 = [x for x in L if x > average]
print(average)
print(L1)



#QUESTION 2
scores = tuple(L[:8])
print("scores =", scores)

highest = max(scores)
highest_idx = scores.index(highest)
lowest = min(scores)
lowest_count = scores.count(lowest)
print("Highest score is", highest, "at index", highest_idx)
print("Lowest score is", lowest, "which appears", lowest_count, "times")

# Tuples are immutable and cannot be changed in place, so we reverse it by casting to list after slicing
reversed_list = list(scores[::-1])
print("Reversed as list:", reversed_list)

search_score = int(input("Enter a score to search: "))
if search_score in scores:
    print("First occurrence index:", scores.index(search_score))
else:
    print("Score is not present in the tuple")

try:
    scores[0] = 100
except TypeError as e:
    print("Captured Error:", e)
    # Tuples are immutable so we cannot reassign values, unlike lists which are mutable and allow direct changes

first, second, *remaining = scores
print("First score:", first)
print("Second score:", second)
print("Remaining scores:", remaining)



#QUESTION 3
random.seed(int(roll_no))

random_nums = [random.randint(100, 900) for _ in range(100)]
print("Generated list:", random_nums)

odds = [x for x in random_nums if x % 2 != 0]
print("Total odd numbers:", len(odds))
print("Odd numbers:", odds)

evens = [x for x in random_nums if x % 2 == 0]
print("Total even numbers:", len(evens))
print("Even numbers:", evens)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in random_nums if is_prime(x)]
print("Total prime numbers:", len(primes))
print("Prime numbers list:", primes)

most_frequent_num = max(set(random_nums), key=random_nums.count)
frequency = random_nums.count(most_frequent_num)
print("Most frequent number:", most_frequent_num, "which occurs", frequency, "times")



#QUESTION 4
first_8_digits = [int(digit) for digit in roll_no[:8]]
A = {digit * 7 for digit in first_8_digits}
B = {digit * 9 for digit in first_8_digits}
print("Set A =", A)
print("Set B =", B)

union_set = A.union(B)
print("Union:", union_set)

intersection_set = A.intersection(B)
print("Intersection:", intersection_set)

diff_AB = A.difference(B)
diff_BA = B.difference(A)
print("A - B:", diff_AB)
print("B - A:", diff_BA)
# difference finds elements in one set but not the other, while symmetric_difference finds elements in either set but not both

sym_diff = A.symmetric_difference(B)
print("Symmetric difference:", sym_diff)

print("Is A subset of B:", A.issubset(B))
print("Is B superset of A:", B.issuperset(A))

x = int(input("Enter value to remove from A: "))
A.discard(x)
print("Set A after discard:", A)
# discard does not raise an error if the element is missing, whereas remove raises a KeyError



#QUESTION 5
name = input("Enter your name: ")
branch = input("Enter your branch: ")
age = int(input("Enter your age: "))
city = input("Enter your home city: ")

my_dict = {
    "name": name,
    "roll_no": roll_no,
    "branch": branch,
    "age": age,
    "city": city
}
print("Original dictionary:", my_dict)

my_dict["location"] = my_dict.pop("city")
print("After renaming city:", my_dict)

cgpa = float(input("Enter your CGPA: "))
my_dict["cgpa"] = cgpa
print("After adding cgpa:", my_dict)

my_dict["age"] += 1
print("After updating age:", my_dict)

dict_copy1 = my_dict.copy()
dict_copy2 = my_dict.copy()

popped_val = dict_copy1.pop("branch")
print("After pop:", dict_copy1)
del dict_copy2["branch"]
print("After del:", dict_copy2)
# pop removes the key and returns its value, while del simply removes the key-value pair without returning anything

for key, value in my_dict.items():
    print(key, "->", value)

if "email" in my_dict:
    print("Email is:", my_dict["email"])
else:
    print("Fallback message: email does not exist in dictionary")

friend_dict = {
    "name": "Amit Sharma",
    "roll_no": "1022034588",
    "branch": "Information Technology",
    "age": 21,
    "city": "Delhi"
}
merged_dict = {**my_dict, **friend_dict}
print("Merged dictionary:", merged_dict)
# When merging dictionaries, values from the second dictionary override those from the first dictionary for common keys

string_dict = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print("String only dictionary:", string_dict)
