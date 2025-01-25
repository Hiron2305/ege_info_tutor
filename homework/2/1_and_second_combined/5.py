print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((x and y) or (y and z)) == ((x <= w) and (w <= z))
                l = []
                l.extend([x,y,z,w])
                if f == 1 and ((l.count(1) == 3 and l.count(0) == 1) or (l.count(1) >= 1 and l.count(0) >= 2)):
                    print(x, y, z, w)