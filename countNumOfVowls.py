myStr = "ahmed Hegab"
# myStr = input("Enter myString: ")
def countV(myStr):
      count = 0
      for i in myStr.lower():
            if(i in ('a', 'e', 'i', 'o', 'u')):
                  count = count + 1
      return count

print(countV(myStr))