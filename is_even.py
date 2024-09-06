class IsEven:
    def __call__(self, number):
        # Return True if the number is even and False if it is otherwise(odd number)
        return number % 2 == 0

is_even = IsEven()

result1 = is_even(10)  # Should return True since 10 is an even number 
print(f"10 is even: {result1}")

result2 = is_even(7)  # Should return False since 7 is an odd number 
print(f"7 is even: {result2}")