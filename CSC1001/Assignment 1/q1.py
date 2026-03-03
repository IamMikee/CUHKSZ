while True:
    binary_num = input("Enter a binary number: ")
    if binary_num == "end":
        break
    try:
        print(hex(int(binary_num, 2))[2:])
    except:
        print("Invalid input")