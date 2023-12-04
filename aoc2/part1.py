with open('aoc2/input.txt', 'r') as file:
    total = 0
    for index, line in enumerate(file):
        line = line.replace(" ", "").replace (":", ";").replace("lue", "").replace("ed", "").replace("reen", "").strip("\n")
        line = line.split(";")
        del line[0]
        copy = []
        for element in line:
            copy.append(element.split(","))
        lineScore = 0
        for element in copy:
            red = 12; green = 13; blue = 14
            for amount in element:
                if amount[-1] == "r":
                    red -= int(amount[:-1])
                elif amount [-1] == "g":
                    green -= int(amount[:-1])
                elif amount[-1] == "b":
                    blue -= int(amount[:-1])
            if red >= 0 and blue >= 0 and green >= 0:
                lineScore += 1
        if lineScore == len(copy):
            total += index + 1
    print(total)