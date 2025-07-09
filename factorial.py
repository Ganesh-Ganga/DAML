def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci_series(n):
    """Return a list containing the Fibonacci series up to n terms."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {factorial(num)}")
    print(f"Fibonacci series up to {num} terms is {fibonacci_series(num)}")