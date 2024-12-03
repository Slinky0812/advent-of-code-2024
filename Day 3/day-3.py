import re

def mul(a, b):
    return a * b

def findTotal(mulList):
    total = 0
    for call in mulList:
        nums = re.findall(r"\d{1,3}", call)
        total = total + mul(int(nums[0]), int(nums[1]))
    return total

total = 0

with open('memory.txt') as file:
    text = file.read()

mulList = []

findMul = True
splitText = re.split(r"(do\(\)|don't\(\))|(mul\((\d{1,3}),(\d{1,3})\))", text)
for string in splitText:
    if string is None:
        continue;

    if string == "do()":
        findMul = True
    
    if string == "don't()":
        findMul = False
    
    if findMul:
        mulMatch = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", string)
        if mulMatch:
            mulList.append(f"{str(mulMatch.group(1))}, {str(mulMatch.group(2))}")

total = total + findTotal(mulList)
print(total)