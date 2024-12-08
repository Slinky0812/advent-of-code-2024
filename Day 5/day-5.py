import re


def findPageRulesAndUpdates(pages):
    pageRules = []
    updates = []
    for line in pages:
        tempPage = re.search(r"\d{2}\|\d{2}", line)
        if tempPage != None:
            pageRules.append(tempPage.string)
        else:
            if line != "":
                updates.append(line)
    return pageRules, updates


def findCorrectUpdates(pageRules, updates):
    correctUpdates = []
    for update in updates:
        numsList = update.split(",")
        wrongRule = 0
        # loop through each rule
        for rule in pageRules:
            # check if we need to check for a rule
            if rule[:2] in numsList:
                # look beyond this point to see if the second number exists
                if rule[3:] in numsList:
                    if numsList.index(rule[:2]) > numsList.index(rule[3:]):
                        wrongRule += 1
                        break;

        if wrongRule == 0:
            correctUpdates.append(update)
            print(update + " - ADDED")
            print("")

    return correctUpdates


def findMiddleNumSum(updates):
    total = 0
    for update in updates:
        numsList = update.split(",")
        middleIndex = (len(numsList)) // 2
        total += int(numsList[middleIndex])

    return total


with open("pages.txt") as file:
    pages = [line.strip() for line in file]

pageRules, updates = findPageRulesAndUpdates(pages)
correctUpdates = findCorrectUpdates(pageRules, updates)
total = findMiddleNumSum(correctUpdates)
print(total)

