class ReverseString:
    def __call__(self, text):
        # Return the reversed version of the string which will be inputed 
        return text[::-1]
    
reverse_string = ReverseString() 

result  = reverse_string("Joshua Ndegwa")  
print(f"Reversed 'hello': {result}")