print("x y z w")
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (w <= (y == z)) and (y == (z <= x))
                if f == 1 or (f == 0 and sorted([x,y,z,w]) == [0,0,0,1]):
                    print(x, y, z, w, "=", int(f))
