with open('aoc2/input.txt', 'r') as file:
    total = 0
    for line in file:
        line = line.replace(" ", "").replace (":", ";").replace("lue", "").replace("ed", "").replace("reen", "").replace(";", ",").strip("\n")
        line = line.split(",")
        reds = []; greens = []; blues = []
        for element in line:
            if element[-1] == "r":
                reds.append(int(element[:-1]))
            elif element [-1] == "g":
                greens.append(int(element[:-1]))
            elif element[-1] == "b":
                blues.append(int(element[:-1]))
        total += max(reds) * max(blues) * max(greens)
    print(total)