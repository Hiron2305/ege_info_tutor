print('1:')

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((x == (not(y))) <= ((z <= (not(w)))) and (w <= y))
                first = []
                first.extend([x,y,z,w])
                if f and first.count(1) == 3:
                    print(x, y, z ,w, '= 1')
                if f == 0:
                    print(x, y, z, w, "= 0")