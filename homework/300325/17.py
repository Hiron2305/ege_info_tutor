valid_ips = set()

with open('24_17.txt', 'r') as file:
    for line in file:
        ip = line.strip()
        parts = ip.split('.')
        if len(parts) != 4:
            continue

        if (parts[0] == '195' and
                len(parts[1]) == 2 and parts[1][0] == '2' and parts[1][1].isdigit() and
                parts[2] == '125' and
                parts[3] == '14'):
            valid_ips.add(ip)

print(len(valid_ips))
