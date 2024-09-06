class AddNumbers:
    def __call__(self, num1, num2):
        return num1 + num2
    
add_numbers = AddNumbers()        # Creating an instance of AddNumbers
result = add_numbers(100, 120) 
print(result)