with open('input.txt', 'r') as file:
    cp = []
    for line in file:
        cp.append(line[10:].strip("\n").split("|"))
    total = 0
    for index, line in enumerate(cp):
        copy = []
        value = 0
        for element in line:
            copy.append(element.split(" "))
        for number in copy[1]:
            if number in copy[0] and number != "":
                if value == 0:
                    value += 1
                else:
                    value = value*2
        total += value
        print(total, line, index)
