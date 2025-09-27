while True:
    user_input = input("Enter a positive integer: ")
    largest_prime = 0

    if user_input == "end":
        break

    try:
        num = int(user_input)
        
        while num%2 == 0:
            largest_prime = 2
            num /= 2
        
        for i in range(3, int(num), 2):
            if num < i:
                break
            while num%i == 0:
                largest_prime = i
                num /= i
        
        if num > 2:
            largest_prime = num

        print(f"The largest prime factor of {user_input} is: {int(largest_prime)}")
    except:
        print("Invalid input")