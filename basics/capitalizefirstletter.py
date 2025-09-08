def capitalize_words(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

str1 = "snake is for python lovers"

capitalized_string = capitalize_words(str1)
print("Capitalized string:", capitalized_string)