while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Calculate Square")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        print("Hello there!")
    elif choice == '2':
        try:
            number = int(input("Enter a number: "))
            square = number ** 2
            print(f"The square of {number} is {square}")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")