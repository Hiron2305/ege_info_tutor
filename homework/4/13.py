s = 45 * '1' + 45 * '2'

while "111" in s:
    s = s.replace("111", "2", 1)
    s = s.replace("222", "1", 1)

print(s)