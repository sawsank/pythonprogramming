first_list = [2,3,4,5,6,7,8]
print("First list ", first_list)

second_list = [4,9,16,25,36,49,64]
print("Second list ", second_list)

result = zip(first_list, second_list) #This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.
result_set = set(result)
print(result_set)

