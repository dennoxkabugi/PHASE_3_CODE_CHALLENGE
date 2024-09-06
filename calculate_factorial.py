class CalculateFactorial:
    def __call__(self, n):
        if n == 0:              # Calculating the factorial of a non-negative integer n
            return 1            # Factorial of 0 is 1
        return n * self(n - 1)  
    
calculate_factorial = CalculateFactorial()

result = calculate_factorial(10)  
print(f"Factorial of 10 : {result}")