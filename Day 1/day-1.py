def generateLists(path):
    word = ''
    leftWords = []
    rightWords = []
    with open(path) as file:
        left = True
        while True:
            char = file.read(1)
            if char.isspace():
                if word:
                    if left:
                        leftWords.append(word)
                        left = False
                    else:
                        rightWords.append(word)
                        left = True
                    word = ''
            elif char == '':
                if word:
                    if left:
                        leftWords.append(word)
                        left = False
                    else:
                        rightWords.append(word)
                        left = True
                break
            else:
                word += char

    return leftWords, rightWords

# Find the Left list and right list
left, right = generateLists('location-id-list.txt')

# Sort out lists from smallest to largest
left.sort()
right.sort()

distance = 0
# len(left) == len(right)
for id in range(0, len(left)):
    if int(right[id]) > int(left[id]):
        currentDistance = int(right[id]) - int(left[id])
    else:
        currentDistance = int(left[id]) - int(right[id])
    distance = distance + currentDistance

print(distance)

# PART TWO
similarityScore = 0
for i in range(0, len(left)):
    count = 0
    for j in range(0, len(right)):
        if left[i] == right[j]:
            count += 1
        
    score = int(left[i]) * count
    similarityScore = similarityScore + score

print(similarityScore)