def outer_func(a,b):
    square = a ** 2

    def addition(a,b): # inner function
        return a + b
    
    add = addition(a,b) # call inner function from outer function
    return add+5

result = outer_func(5,10)
print(result)