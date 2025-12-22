# Question 4: credit card number validation
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary


def isValid(number):
    ''' 
    Return True if the card number is valid
    parameter number: card number (int), number >= 0
    return: bools (True/False), the validity
    '''
    # TODO part
    # ------- Your code start here -------
    number = str(number)[::-1]
    if len(number) < 13 or len(number) > 16 or not(number.endswith("4") or number.endswith("5") or number.endswith("73") or number.endswith("6")):
        return False
    sum = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    return sum%10 == 0
    # ------- End of your code -----------


def sumOfDoubleEvenPlace(number):
    '''
    Get the result from step 2.
    '''
    # TODO part
    # ------- Your code start here -------
    sum = 0
    for i in range(1, len(number), 2):
        sum += getDigit(int(number[i]))
    return sum
    # ------- End of your code -----------


def getDigit(number):
    '''
    Return this number if it is a single digit, otherwise, return the sum of the two digits
    '''
    # TODO part
    # ------- Your code start here -------
    number*=2
    if number > 9:
        return sum([int(x) for x in str(number)])
    return number
    # ------- End of your code -----------


def sumOfOddPlace(number):
    ''' 
    Return the sum of odd place digits in number
    '''
    # TODO part
    # ------- Your code start here -------
    sum = 0
    for i in range(0, len(number), 2):
        sum += int(number[i])
    return sum
    # ------- End of your code -----------


if __name__ == '__main__':
    # Sample test cases
    # isValid(4388576018410707) # valid test case
    # isValid(4388576018402626) # invalid test case

    # Prompts the user to enter a credit card number as an integer
    # Display whether the number is valid or invalid
    try:
        number = int(input("Please input your credit card number: "))
    except:
        print("Invalid")
        exit()
    if isValid(number):
        print("Valid")
    else:
        print("Invalid")
