from datetime import datetime


##password= "1234"
##passwordinput=input("Enter Password: \t")
##if (passwordinput!=password):
##    exit()
    
d=datetime.now()
longdate=d.strftime("%d %B %Y %I:%M:%S")
longdateright=str.rjust(longdate, 80)
print(longdateright)

itemnumber=['1','2', '3', '4', '5']
beveragelist=["Tea", "Coffee", "Ice Tea", "Cold Coffee", "Juices"]
beverage=[]
rate=[50.00, 80.00, 100.00, 150.00, 50.00]
qty=[0,0,0,0,0]
amt=[0.0,0.0,0.0,0.0,0.0]
w=[0,0,0,0,0]
bevdone=0
bevindex=0
bevlen=len(beveragelist)
while (bevdone==0):
    buffer=list("               ")
    itemlen=len(beveragelist[bevindex])
    icount=0
    while (icount!=itemlen):
        buffer[icount]=beveragelist[bevindex][icount]
        icount=icount+1
    addall=0
    bufferitem=""
    bufferlen=len(buffer)
    while (addall!=bufferlen):
        bufferitem=bufferitem+buffer[addall]
        addall=addall+1
    
    beverage.append(bufferitem)
    bevindex=bevindex+1
    if (bevindex==bevlen):
        bevdone=1
        

line="-----------------------------------------------------------------------------"

title="MENU"
s=str.center(title,80)
print (s,"\n")
print(line)
print ("ITEM NO. \t\t BEVERAGES \t\t\t PRICE YOU PAY\n")
print(line)
i=0
while (i!=5):
    print (itemnumber[i], "\t\t\t", beverage[i], "\t\t\t",  rate[i], "\n")
    i=i+1
print(line)


runningtotal=0
xok=0
while (xok==0):
    y=input("Item number: \t")
    numericy=str.isnumeric(y)
    if (numericy==False):
        print("give me a number")
        continue
    if (numericy==True):
        x=int(y)

        if (x==0):
            print("Invalid item number")
            continue
        if (x>5):
            print("invalid item number")
            continue
    x=x-1
        
    qint=0
    qok=0
    while (qok==0):
        q=input("Quantity :")
        
        numericq=str.isnumeric(q)
        if (numericq==False):
            print("give me a number")
            continue
        qint=int(q)
        if (qint>99):
            print("Invalid Quantity(too high)")
            continue
        if (qint<1):
            print("Invalid Quantity")
            continue
    
        qty[x]=qint
        if (w[x]!=0):
            prevorder=w[x]
            w[x]=qty[x]
            w[x]=prevorder+w[x]
        if (w[x]==0):
            w[x]=int(qty[x])
        if (amt[x]==0):
            amt[x]= (rate[x]*w[x])
            runningtotal=runningtotal+amt[x]
        if (amt[x]!=0):
            runningtotal=runningtotal-amt[x]
            amt[x]=0
            amt[x]= (rate[x]*w[x])
            runningtotal=runningtotal+amt[x]
        print(beverage[x], "\t\t", rate[x])
        print("Total Billing Amount is: \t", runningtotal)
        break
    proceed=input("Proceed to next item?(y/n) \t")
    if (proceed!="y"):
        break

b=open('billnumber.dat','r')
billnum=b.readline()
billnumint=int(billnum)
billnumber=billnumint+1
on=str(billnumber)
##on=billnumberstr.zfill(5)
b.close()
print("Order Number :\t", on)

b=open('billnumber.dat','w')
b.write(on)
b.close()

discount=input("Discount percentage: \t")
discountfloat=float(discount)


title2="BILL"
s2=str.center(title2, 80)
ordernumber=str.ljust(on,80)
print("\n", line, "\n")
print(longdateright)
print(s2, "\n")
print("Order Number :\t", ordernumber)
print(line)
print("Item No.\t Item \t\t  Price\t\t Qty \t\t Amount")
print(line)


billcount=0
listlength=len(amt)
while (billcount!=listlength):
    if (amt[billcount]!=0):
        ratestr=str(rate[billcount])
        rateright=str.rjust(ratestr,6)
        qtystr=str(qty[billcount])
        qtyright=str.rjust(qtystr, 3)
        amtstr=str(amt[billcount])
        amtright=str.rjust(amtstr,7)
        print (itemnumber[billcount], "\t\t",beverage[billcount], rateright, "\t",qtyright,"\t\t", amtright)
    billcount=billcount+1


discounttotal= runningtotal- (discountfloat/100)*runningtotal
gst= (18/100)*discounttotal
grandtotal=discounttotal+gst

disctotalstr=str(discounttotal)
disctotalright=str.rjust(disctotalstr,7)
totalstr=str(runningtotal)
totalright=str.rjust(totalstr,7)
gstround=round(gst,2)
gststr=str(gstround)
gstright=str.rjust(gststr,7)
grandround=round(grandtotal, 2)
grandstr= str(grandround)
grandtotalright=str.rjust(grandstr,7)
print(line)
print("Total Amount \t\t\t\t\t\t\t", totalright)
print("Total Amount after  \t\t",discount,"% Discount\t\t\t", disctotalright)
print("GST \t\t\t\t 18 % \t\t\t\t", gstright)
print(line)
print("Total Bill Amount \t\t\t\t\t\t", grandtotalright)
print(line)

confirm=input("Confirm Order?(y/n):\t")
if (confirm == 'n'):
    b=open('billnumber.dat','r')
    billnum=b.readline()
    billnumint=int(billnum)
    billnumber=billnumint-1
    on=str(billnumber)
    b.close()
    b=open('billnumber.dat','w')
    b.write(on)
    b.close()
    exit()

orders=open('orderlist.dat','a')
billcount=0
listlength=len(amt)
while (billcount!=listlength):
    if (amt[billcount]!=0):
        orders.write(on)
        orders.write(',')
        orders.write(longdate)
        orders.write(',')
        ratestr=str(rate[billcount])
        rateright=str.rjust(ratestr,6)
        qtystr=str(qty[billcount])
        qtyright=str.rjust(qtystr, 3)
        amtstr=str(amt[billcount])
        amtright=str.rjust(amtstr,7)
        orders.write(itemnumber[billcount])
        orders.write(",")
        orders.write(beverage[billcount])
        orders.write(",")
        orders.write(rateright)
        orders.write(",")
        orders.write(qtyright)
        orders.write(",")
        orders.write(discount)
        orders.write("\n")
    billcount=billcount+1
orders.close()




























    
