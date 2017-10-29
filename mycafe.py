from datetime import datetime

cashcode=["QWE","ASD","ZXC","RTY","FGH"]
cashier=input("Password:\t")
if (cashier not in cashcode):
    print("INVALID PASSWORD")
    dummy=input()
    exit()
d=datetime.now()
longdate=d.strftime("%d %B %Y %I:%M:%S")
longdateright=str.rjust(longdate,80)


print(longdateright)
title="Cafe Azzure"
line="---------------------------------------------------------------------------------"
titlecen=str.center(title,80)
print(titlecen)
print(line)
option1="1.\tEnter Bill"
option2="2.\tDisplay Bill"
option1cen=str.center(option1,80)
option2cen=str.center(option2,80)
print(option1cen)
print(option2cen)
print(line)
opdone=0
while (opdone==0):
    option=input("Enter Option Number(0 to exit):\t")
    optionint=int(option)
    if (optionint>2):
        print("Invalid selection")
        continue
    if (optionint==1):
        import generatebill
    if (optionint==2):
        import ordernumberfunction
    if (optionint==0):
        opdone=1
