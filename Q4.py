def remove_vowels(s):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    return ''.join([char for char in s if char not in vowels])


original_string = input("Original string:")
no_vowels_string = remove_vowels(original_string)
print("String without vowels:", no_vowels_string)
