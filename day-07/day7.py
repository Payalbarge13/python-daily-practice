#code1
numbers = [1, 2, 3, 4]
squares = {n: n ** 2 for n in numbers}
# Result: {1: 1, 2: 4, 3: 9, 4: 16}

#code2
users = {
    "user_1": {"name": "Alex", "role": "Admin"},
    "user_2": {"name": "Maya", "role": "Editor"}
}
print(users["user_2"]["role"])  # Output: Editor
