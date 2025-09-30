data = [('apple',5),('banana',2),('orange',8),('grape',3)]
sorted_data = sorted(data, key=lambda item: item[1])
print(f"The sorted list of tuples based on the second element is :{sorted_data}")