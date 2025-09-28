def print_info(**kwargs):
    if kwargs:
        print("\n --- Information ---")
        for key, value in kwargs.items():
            print(f"{key}:{value}")
        else:
            print("\n No information provided")

print_info(name="shasank", age=36, city="Bangalore")
print_info(job="Engineer", salary=75000)
print_info(country="USA", state="California", zip_code="90210")
print_info()  # Calling the function without any arguments