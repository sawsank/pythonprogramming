try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    if denominator == 0:
        print("Error: Denominator cannot be zero.")
    else:
        percentage = (numerator / denominator) * 100
        print(f"The percentage is: {percentage:.2f}%")
except ValueError:
    print("Invalid input. Please enter numeric values.")