def is_palindrome(number):
    if number < 0:
        return False
    
    original_string = str(number)
    reversed_string = original_string[::-1]

    if original_string == reversed_string:
        return True
    else:
        return False

print(is_palindrome(121))
print(is_palindrome(123))