def is_palindrome(word):
    return word == word[::-1]

def is_palindrome_with_loop(word):
    for i in range(int(len(word) / 2)):
        if word[i] != word[-i - 1]:
            return False
    return True
