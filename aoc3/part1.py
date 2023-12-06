with open('input.txt', 'r') as file:
    total = 0
    copy = ['!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!']
    nums = []
    with open('input.txt', 'r') as file2:
        for line in file2:
            copy.append("!" + line.strip("\n") + "!")
    copy.append('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    numbers = "0123456789"
    symbols = "@#$%^&*()_+=-~`/?><,:"
    for index, line in enumerate(copy):
        for i, letter in enumerate(line):
            if letter in numbers and line[i - 1] not in numbers:
                stIndex = i - 1
                temp = letter
            elif letter in numbers:
                temp += letter
            elif letter not in numbers and line[i - 1] in numbers and temp != "":
                endIndex = i
                adjacent = ""
                for j in range(index - 1, index + 2):
                    for k in range(stIndex, endIndex + 1):
                        adjacent += copy[j][k]
                for l in adjacent:
                    if l in symbols:
                        total += int(temp)
                temp = ""
    print(total)