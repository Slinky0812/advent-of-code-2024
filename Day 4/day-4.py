import re


def searchHorizontal(wordSearch):
    totalCount = 0
    for line in wordSearch:
        # search forward
        forwardList = re.findall("XMAS", line)
        # search backward
        backwardList = re.findall("SAMX", line)
        count = len(forwardList) + len(backwardList)
        totalCount += count

    return totalCount

def searchVertical(wordSearch):
    totalCount = 0
    for line in range(0, len(wordSearch) - 3):
        for i in range(0, len(wordSearch[line])):
            if wordSearch[line][i] == 'X' and wordSearch[line+1][i] == 'M' and wordSearch[line+2][i] == 'A' and wordSearch[line+3][i] == 'S':
                totalCount+=1
            if wordSearch[line][i] == 'S' and wordSearch[line+1][i] == 'A' and wordSearch[line+2][i] == 'M' and wordSearch[line+3][i] == 'X':
                totalCount+=1

    return totalCount

def searcForwardhDiagonal(wordSearch):
    # \ direction
    totalCount = 0
    for line in range(0, len(wordSearch) - 3):
        for i in range(0, len(wordSearch[line]) - 3):
            if wordSearch[line][i] == 'X' and wordSearch[line+1][i+1] == 'M' and wordSearch[line+2][i+2] == 'A' and wordSearch[line+3][i+3] == 'S':
                totalCount+=1
            if wordSearch[line][i] == 'S' and wordSearch[line+1][i+1] == 'A' and wordSearch[line+2][i+2] == 'M' and wordSearch[line+3][i+3] == 'X':
                totalCount+=1

    return totalCount

def searchBackwardDiagonal(wordSearch):
    # / direction
    totalCount = 0
    for line in range(0, len(wordSearch) - 3):
        for i in range(3, len(wordSearch[line])):
            if wordSearch[line][i] == 'X' and wordSearch[line+1][i-1] == 'M' and wordSearch[line+2][i-2] == 'A' and wordSearch[line+3][i-3] == 'S':
                totalCount+=1
            if wordSearch[line][i] == 'S' and wordSearch[line+1][i-1] == 'A' and wordSearch[line+2][i-2] == 'M' and wordSearch[line+3][i-3] == 'X':
                totalCount+=1

    return totalCount

def countXShapes(wordSearch):
    totalCount = 0
    for line in range(1, len(wordSearch)-1):
        for i in range(1, len(wordSearch[line])-1):
            if wordSearch[line][i] == "A":
                if wordSearch[line-1][i-1] == "S" and wordSearch[line+1][i+1] == "M" and wordSearch[line-1][i+1] == "M" and wordSearch[line+1][i-1] == "S":
                    totalCount += 1

                if wordSearch[line-1][i-1] == "S" and wordSearch[line+1][i+1] == "M" and wordSearch[line-1][i+1] == "S" and wordSearch[line+1][i-1] == "M":
                    totalCount += 1

                if wordSearch[line-1][i-1] == "M" and wordSearch[line+1][i+1] == "S" and wordSearch[line-1][i+1] == "S" and wordSearch[line+1][i-1] == "M":
                    totalCount += 1

                if wordSearch[line-1][i-1] == "M" and wordSearch[line+1][i+1] == "S" and wordSearch[line-1][i+1] == "M" and wordSearch[line+1][i-1] == "S":
                    totalCount += 1

    return totalCount


xmasCount = 0

with open("word-search.txt") as file:
    wordSearch = [line.strip() for line in file]

xmasCount = xmasCount + searchHorizontal(wordSearch)
xmasCount = xmasCount + searchVertical(wordSearch)
xmasCount = xmasCount + searcForwardhDiagonal(wordSearch)
xmasCount = xmasCount + searchBackwardDiagonal(wordSearch)

# print(xmasCount)

# PART TWO
xShapedMAS = countXShapes(wordSearch)
print(xShapedMAS)