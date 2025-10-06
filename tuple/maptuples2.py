#Using a loop

# 7. Map Tuples
t = (1, 2, 3, 4)
print(f"Original tuple: {t}")

# Method 2: Using a loop
squared_list_loop = []
for num in t:
  squared_list_loop.append(num ** 2)
  squared_tuple_loop = tuple(squared_list_loop)
print(f"Squared tuple (loop): {squared_tuple_loop}")