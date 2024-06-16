n=input("enter C or F to convert=")
degree=float(input("enter temperature to be converted="))
if n=="c":
    result=int(round((degree - 32) * 5 / 9)) 
    print(result)
elif n=="f":
    result=int(round((9 * degree) / 5 + 32))
    print(result)
