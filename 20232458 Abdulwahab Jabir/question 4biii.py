while True:
    age = input("Please enter your age (enter 'quit' to exit): ")

    if age.lower() == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket is N5,000.")
    else:
        print("Your ticket is N10,000.")