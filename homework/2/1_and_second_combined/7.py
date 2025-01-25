print("x y z w")
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (z == (x <= w)) and (x == (not(w <= y)))
                l = []
                l.extend([x,y,z,w])
                if (f == 1 and l.count(0) >= 2) or (f == 0 and l.count(0) >= 1 and l.count(1) >= 2):
                    print(x, y, z, w, "=", int(f))