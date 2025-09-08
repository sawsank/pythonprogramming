def contains_digit(text):
    for char in text:
        if '0' <= char <= '9':
            return True
    return False
    
user_string = input("Enter a string:")

if contains_digit(user_string):
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")