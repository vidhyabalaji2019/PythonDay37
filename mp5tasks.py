# ===============================
# PYTHON SETS & DICTIONARIES TASKS
# ===============================

# ---------- Task 1 ----------
print("\nTask 1: Create and Access a Set")
colors = {"Red", "Blue", "Green", "Yellow", "Purple"}
for color in colors:
    print(color)

# ---------- Task 2 ----------
print("\nTask 2: Add Items to a Set")
movies = set()
movies.update(["Inception", "Avatar", "Titanic", "Interstellar", "Joker"])
print(movies)

# ---------- Task 3 ----------
print("\nTask 3: Remove Items from a Set")
fruits = {"Apple", "Banana", "Mango", "Orange", "Pineapple", "Grapes"}
fruits.remove("Banana")
fruits.discard("Cherry")  # No error even if missing
print(fruits)

# ---------- Task 4 ----------
print("\nTask 4: Check if an Item Exists in a Set")
languages = {"Python", "Java", "C++", "JavaScript"}
user_input = "Python"  # Replace with input("Enter a language: ")
if user_input in languages:
    print(f"{user_input} exists in the set!")
else:
    print(f"{user_input} not found!")

# ---------- Task 5 ----------
print("\nTask 5: Join Two Sets")
even = {2, 4, 6, 8, 10}
odd = {1, 3, 5, 7, 9}
combined = even.union(odd)
print(combined)

# ---------- Task 6 ----------
print("\nTask 6: Common Elements in Two Sets")
set1 = {2, 4, 6, 8, 10}
set2 = {4, 8, 12, 16}
print(set1.intersection(set2))

# ---------- Task 7 ----------
print("\nTask 7: Difference Between Two Sets")
A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8, 9}
print(A.difference(B))

# ---------- Task 8 ----------
print("\nTask 8: Symmetric Difference Between Two Sets")
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(setA.symmetric_difference(setB))

# ---------- Task 9 ----------
print("\nTask 9: Loop Through a Set")
cars = {"BMW", "Audi", "Tesla", "Ford"}
for car in cars:
    print(car)

# ---------- Task 10 ----------
print("\nTask 10: Convert a List to a Set")
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)

# ---------- Task 11 ----------
print("\nTask 11: Frozen Set Example")
vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
print(vowels)
# vowels.add('x')  # ❌ Will cause an error (immutable)

# ---------- Task 12 ----------
print("\nTask 12: Set Operations on Frozen Set")
primes = frozenset({2, 3, 5, 7})
evens = {2, 4, 6, 8, 10}
print("Intersection:", primes.intersection(evens))
print("Union:", primes.union(evens))

# ---------- Task 13 ----------
print("\nTask 13: Find Length of a Set")
words = {"apple", "banana", "grape", "orange", "kiwi", "pear", "mango", "papaya", "plum", "berry"}
print("Number of items:", len(words))

# ---------- Task 14 ----------
print("\nTask 14: Create a Dictionary and Access Elements")
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"], person["age"])
print(person.get("name"), person.get("age"))

# ---------- Task 15 ----------
print("\nTask 15: Handle Missing Keys")
print(person.get("country", "Key not found"))

# ---------- Task 16 ----------
print("\nTask 16: Add New Key-Value Pairs")
data = {}
data["name"] = "Bob"
print(data)
data["age"] = 30
print(data)
data["city"] = "London"
print(data)

# ---------- Task 17 ----------
print("\nTask 17: Update Dictionary Entry")
product = {"name": "Laptop", "price": 50000, "stock": 10}
print("Before:", product)
product["price"] = 45000
product["stock"] = 15
print("After:", product)

# ---------- Task 18 ----------
print("\nTask 18: Merge Two Dictionaries")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)

# ---------- Task 19 ----------
print("\nTask 19: Remove a Specific Key")
sample = {"x": 10, "y": 20, "z": 30, "w": 40, "v": 50}
del sample["y"]
print(sample)
if "k" in sample:
    del sample["k"]
else:
    print("Key not found, cannot delete.")

# ---------- Task 20 ----------
print("\nTask 20: Remove Using pop()")
sample2 = {"id": 1, "name": "John", "age": 28}
removed_value = sample2.pop("age")
print("Removed Value:", removed_value)
print("Updated Dictionary:", sample2)

# ---------- Task 21 ----------
print("\nTask 21: Remove and Return Last Item")
sample3 = {"A": 100, "B": 200, "C": 300}
last_item = sample3.popitem()
print("Removed Item:", last_item)
print("Updated Dictionary:", sample3)

# ---------- Task 22 ----------
print("\nTask 22: Iterate Through Dictionary (Keys & Values)")
info = {"name": "David", "age": 32, "city": "Paris"}
for key, value in info.items():
    print(f"{key} → {value}")

# ---------- Task 23 ----------
print("\nTask 23: Iterate Through Dictionary (Keys Only)")
for key in info.keys():
    print(key)

# ---------- Task 24 ----------
print("\nTask 24: Iterate Through Dictionary (Values Only)")
for value in info.values():
    print(value)

# ---------- Task 25 ----------
print("\nTask 25: Iterate Through a Nested Dictionary")
students = {
    "student1": {"name": "Alice", "age": 20, "subjects": ["Math", "Science"]},
    "student2": {"name": "Bob", "age": 22, "subjects": ["English", "History"]}
}
for student, details in students.items():
    print(f"\n{student}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

# ---------- Task 26 ----------
print("\nTask 26: Access Specific Value from Nested Dictionary")
print("Student2's subject (direct):", students["student2"]["subjects"])
print("Student2's subject (using get):", students.get("student2").get("subjects"))
