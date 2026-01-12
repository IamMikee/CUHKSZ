# Question 1: approximate the Cube root
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary


def cbrt(n):
    '''
    This function uses Babylonian Method of Computing the Cube Root
    parameter n: an int or a float, n >= 0
    reture: an int or a float, the Cube root of n
    '''
    # TODO part
    # ------- Your code start here -------
    lastGuess = 1
    nextGuess = (1/3)*(2*lastGuess + (n/(lastGuess**2)))

    while not (abs(nextGuess-lastGuess) < 0.0001 or nextGuess == lastGuess):
        lastGuess = nextGuess
        nextGuess = (1/3)*(2*lastGuess + (n/(lastGuess**2)))

    print(round(nextGuess, 5))
    # ------- End of your code -----------


# Call the function to approximate the Cube root
if __name__ == '__main__':
    cbrt(3)
    cbrt(3.3333)