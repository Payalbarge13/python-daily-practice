# Print a simple greeting
print("Hello, I'm Python!")

# Get input and use a variable
name = input("What is your name? \n")
print(f"Hi, {name}.")

# Print the Fibonacci sequence up to 1000
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()

fib(1000)
