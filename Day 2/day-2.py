def generateReportArray(report):
    reportArray = []
    num = ''
    for char in report:
        if char.isspace():
            reportArray.append(num)
            num = ''
        elif char == '':
            reportArray.append(num)
            num = ''
        else:
            num += char

    return reportArray


def checkGradualIncrease(reportArray):
    for i in range(0, len(reportArray)-1):
        if int(reportArray[i+1]) > int(reportArray[i]):
            if int(reportArray[i+1]) - int(reportArray[i]) > 3:
                return False
        else:
            return False
        
    return True


def checkGradualDecrease(reportArray):
    for i in range(0, len(reportArray)-1):
        if int(reportArray[i+1]) < int(reportArray[i]):
            if int(reportArray[i]) - int(reportArray[i+1]) > 3:
                return False
        else:
            return False
        
    return True


def canBeMadeSafe(reportArray):
    for i in range(0, len(reportArray)):
       # Create a new list with the element at index i removed
        tempArray = reportArray[:i] + reportArray[i + 1:]
        
        # check if the array is gradually increasing or decreasing
        if (checkGradualIncrease(tempArray)) or (checkGradualDecrease(tempArray)):
            return True
    
    return False


safeReports = 0

reports = open('reports.txt')

for report in reports:
    reportArray = generateReportArray(report)

    # check if the array is gradually increasing
    if (checkGradualIncrease(reportArray)):
        safeReports += 1
    # check if the array is gradually increasing
    elif (checkGradualDecrease(reportArray)):
        safeReports += 1
    # report is unsafe
    else:
        if (canBeMadeSafe(reportArray)):
            safeReports += 1
    
print(safeReports)

reports.close()