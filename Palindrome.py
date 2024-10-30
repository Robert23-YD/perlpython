# Create a function is_palindrome(word) that returns True if a given word is a palindrome (reads the same backward) and False otherwise.

def is_palindrome(word):
    # Remove any spaces and convert the string to lowercase for uniformity
    cleaned_word = word.replace(" ", "").lower()
    # Check if the word reads the same backward
    return cleaned_word == cleaned_word[::-1]

# Example usage
print(is_palindrome("rotator"))  # Output: True
print(is_palindrome("hello"))    # Output: False
print(is_palindrome("madam"))  # Output: True
