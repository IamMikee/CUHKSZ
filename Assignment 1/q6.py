def trapezoid_area(points):
    y1 = points[0][1]
    p1 = [x for x in points if x[1] == y1]
    p2 = [x for x in points if x[1] != y1]

    p1.sort()
    p2.sort()

    area = ((p1[0][0]-p1[1][0])+(p2[0][0]-p2[1][0]))*(p1[0][1]-p2[0][1])/2

    if area < 0:
        area*=-1

    print(area)


trapezoid_area([(0,0), (4,0), (3,2), (1,2)])