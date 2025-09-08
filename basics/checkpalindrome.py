def is_palindrome_while_loop(number):
    original_number = number
    reversed_number = 0

    while number>0:
        remainder = number % 10
        reversed_number = (reversed_number * 10) + remainder
        number //= 10

    return original_number ==  reversed_number

print(is_palindrome_while_loop(121))
print(is_palindrome_while_loop(123))