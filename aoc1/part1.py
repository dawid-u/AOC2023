from numpy import sum

with open('aoc1/input.txt', 'r') as file:
    numbers = "0123456789"
    values = []
    for line in file:
        temp = ""
        for letter in line:
            if letter in numbers:
                temp += letter
                break
        for letter in line[::-1]:
            if letter in numbers:
                temp += letter
                break
        values.append(int(temp))
    print(sum(values))