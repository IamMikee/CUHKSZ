while True:
    user_input = input("Enter a positive integer: ")
    if user_input == "end":
        break
    try:
        print(f"The sum of the digits of {user_input} is: {sum([int(x) for x in user_input])}")
    except:
        print("Invalid input")