# tutorial_basics.py

"""
This script introduces fundamental Python concepts for beginners.
You can run it using: python3 tutorial_basics.py
"""

def main():
    print("--- Python Basics Tutorial ---")

    # 1. Variables and Data Types
    # You don't need to declare types; Python figures it out.
    name = "Alice"          # String (str)
    age = 25                # Integer (int)
    height = 5.6            # Floating-point number (float)
    is_student = True       # Boolean (bool)

    print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

    # 2. Lists (Ordered collections)
    fruits = ["apple", "banana", "cherry"]
    print(f"First fruit: {fruits[0]}")
    fruits.append("orange")
    print(f"Fruit list: {fruits}")

    # 3. Dictionaries (Key-Value pairs)
    person = {
        "name": "Bob",
        "age": 30,
        "city": "New York"
    }
    print(f"{person['name']} lives in {person['city']}.")

    # 4. Conditionals (If/Else)
    if age >= 18:
        print(f"{name} is an adult.")
    else:
        print(f"{name} is a minor.")

    # 5. Loops
    print("Counting fruits:")
    for fruit in fruits:
        print(f"- {fruit}")

    # 6. Functions (Defined above or below)
    result = add_numbers(10, 5)
    print(f"10 + 5 = {result}")

def add_numbers(a, b):
    """A simple function that adds two numbers."""
    return a + b

if __name__ == "__main__":
    main()
