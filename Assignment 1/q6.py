def calculation(pair1, pair2, xy):
    h = abs(pair1[0][xy]-pair2[0][xy])
    sumOfParallel = abs(pair1[0][xy-1]-pair1[1][xy-1])+abs(pair2[0][xy-1]-pair2[1][xy-1])
    print(float(((sumOfParallel)/2)*h))


def trapezoid_area(points):
    arr = [points[0]]
    xy = 0 #parallel by what orientation, 0 vert 1 hori
    for j in points:
        if(len(arr) == 2):
            break
        if(arr[0] == j):
            continue

        if(arr[0][0] == j[0]):
            arr.append(j)
        elif(arr[0][1] == j[1]):
            arr.append(j)
            xy = 1

    restpoints = [x for x in points if x not in arr]
    if(restpoints[0][xy] == restpoints[1][xy]):
        calculation(arr, restpoints, xy)
    else:
        xy = abs(xy-1)
        arr = [points[0]] + [x for x in points if x != points[0] and x[xy] == points[0][xy]]
        restpoints = [x for x in points if x not in arr]
        calculation(arr, restpoints, xy)


trapezoid_area([(0,0), (4,0), (3,2), (1,2)])