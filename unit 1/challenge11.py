def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: factorial of n is n times factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Test the factorial function
num = 5  # Change this to any non-negative integer you want to calculate the factorial for
result = factorial(num)
print(f"The factorial of {num} is {result}")
