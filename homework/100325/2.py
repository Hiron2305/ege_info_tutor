print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x == (y <= z)) and (y == (not(z <= w)))
                if f == 1 and [x,y,z,w].count(0) >= 2:
                    print("equals 1:", x, y, z, w)
                if f == 0 and [x, y, z, w].count(1) >= 2 and [x, y, z, w].count(0) >= 1:
                    print("equals 0:", x, y, z, w)