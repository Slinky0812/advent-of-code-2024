import re

def mul(a, b):
    return a * b

def findTotal(mulList):
    total = 0
    for call in mulList:
        total = total + mul(int(call[0]), int(call[1]))
    return total

total = 0

memory = open('memory.txt')

for line in memory:
    # find instance of mul(a, b)
    mulList = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
    total = total + findTotal(mulList)

print(total)

memory.close()