# Question 2: Emirp
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary
from tabnanny import check


def check_for_prime(inp):
    for i in range(3, int(inp**(1/2))+1, 2): #check for prime
            if inp%i == 0:
                return False
    return True

def display_emirps(n):
    '''
    By calling this function, it will print the first n emirps
    It will display 10 numbers per line and align the numbers
    parameter n: int, n > 0
    reture: no
    '''
    # TODO part
    # ------- Your code start here -------
    listofemirps = []
    possibleemirps = []
    num = 13

    while len(listofemirps) < n:
        if num in possibleemirps: #if already exist as larger emirps, directly append, no need to check again
            listofemirps.append(num)
            num += 2
            continue

        if not check_for_prime(num): #skip if number not prime
            num += 2
            continue

        # the flipped number
        flipped = int(str(num)[::-1])
        if flipped%2 == 0 or flipped == num: #check for even prime and palindrome
            num += 2
            continue

        if not check_for_prime(flipped): #skip if not prime
            num += 2
            continue

        listofemirps.append(num)
        possibleemirps.append(flipped)
        num += 2

    #making alignment
    longest_num = len(str(listofemirps[-1]))
    finallist = [" "*(longest_num-len(str(x)))+str(x) for x in listofemirps]
    tempstr = ""
    for i in range(len(finallist)):
        tempstr += finallist[i] + " "
        if (i+1) % 10 == 0:
            print(tempstr.rstrip())
            tempstr = ""
    print(tempstr.rstrip())
    # ------- End of your code -----------


# Call the function to print the first n emirps
if __name__ == '__main__':
    display_emirps(10)
    display_emirps(55)