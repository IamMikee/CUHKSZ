def largest_k_evens(x, k):
    x = [int(a) for a in x if type(a) == int and a%2 == 0] #filter x
    x.sort()
    print(x[-k:])

largest_k_evens([12, 12, 11, 10, 14], 3)
largest_k_evens([10, 23, 5, 4, 11, 8], 3)
largest_k_evens([3.5, 2, 2.0, 6, "8", True], 2)