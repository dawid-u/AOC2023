from numpy import sum

with open('aoc1/input.txt', 'r') as file:
    change = {
        "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6",
        "seven": "7", "eight": "8", "nine": "9"
    }
    numbers = "0123456789"
    values = []
    for line in file:
        t = line.strip("\n")
        temp = ""
        line = line.strip("\n")
        for value in change:
            line = line.replace(value, change[value])
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