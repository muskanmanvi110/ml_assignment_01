str=input("entr a string=")
n=input("enter the element to check in prefix and suffix=")
if str.startswith(n)==True:
    print("Given string starts with ",n)
elif str.endswith(n)==True:
    print("Given string ends with ",n)
else:
    print("the string does not strat or end with ",n)



