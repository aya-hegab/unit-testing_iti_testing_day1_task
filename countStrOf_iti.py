myStr = "itiititi"

def countITI(myStr):
    myStrLower = myStr.lower()
    count = 0

    for i in range(len(myStrLower)-2):
        if myStrLower[i:i+3]=="iti":
                count = count + 1 
    return count

print(countITI(myStr))


