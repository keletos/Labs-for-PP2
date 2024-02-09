def reverse_sentence(input_str):
    return ' '.join(input_str.split()[::-1])

def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]
