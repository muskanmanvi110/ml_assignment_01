from datetime import datetime
Birth_year=int(input("enter birth year="))
current_year = datetime.now().year
a=int((current_year)-(Birth_year))
print("your age is = ",a)
