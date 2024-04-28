# myStr = input("Enter myString: ")
myStr = "heillo woirld"

def locateI(myStr):

    myStrLower = myStr.lower()
    locations = []

    for i in range(len(myStrLower)):
        if myStrLower[i] == 'i':
            locations.append(i)
    return locations


print(locateI(myStr))