class CountVowels:
    def __call__(self, text):
        vowels = 'aeiou'          # defining the vowels 
        return sum(1 for char in text.lower() if char in vowels)

count_vowels = CountVowels()

result = count_vowels("My Name is Joshua Ndegwa. I am Learning Python")  
print(f"Number of vowels : {result}")