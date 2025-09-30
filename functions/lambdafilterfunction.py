number = [1,2,3,4,5,6,7,8,9,10]

even_number = list(filter(lambda x: x% 2 == 0, number))
print(f"The even number in the list are: {even_number}")