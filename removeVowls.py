myStr = "ahmed mohammed"

def removeV(myStr):
    newmyStr = myStr

    for i in myStr.lower():
        if i in ('a', 'e', 'i', 'o', 'u'):
            newmyStr = newmyStr.replace(i, "")
    return newmyStr

print(removeV(myStr))