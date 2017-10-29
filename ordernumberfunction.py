
def getbillnumber():
    billnumok=0
    line=""
    
    while (billnumok==0):
        billnum=input("Enter Bill number(# to exit):\t")
        if (billnum=="#"):
            exit()
        billnumnumeric=str.isnumeric(billnum)
        billnumlen=len(billnum)
        if (billnumnumeric==False):
            print ("Invalid Bill Number")
            continue
        if (billnumlen!=5):
            print("invalid Bill Number")
            continue
        f=open('orderlist.dat','r')
        line=f.readline()
        linecheck=0
        norecord=0
        while (linecheck==0):
            line=f.readline()
##            print(line)
            if (line==""):
                norecord=1
                print("Bill Number not found")
                break
            if (norecord==0):
                ordernumber=line[0:5]
                if (ordernumber==billnum):
                    linecheck=1      
                    billnumok=1
        f.close()
    return billnum
    
##--------------------------------------------------------------

def printbill(billnum):
    itemnumlist=[]
    itemlist=[]
    ratelist=[]
    qtylist=[]
    amtlist=[]
    margin="-----------------------------------------------------------------------------"

    orderok=0
    orderfound=0
    f=open('orderlist.dat','r')
    line=f.readline()
    while (orderok==0):
        line=f.readline()
        linelen=len(line)
        ordernumber=line[0:5]
##        print(ordernumber)
##        dummy=input()
        if (ordernumber==billnum):
            orderfound=1
            date=line[6:32]
            itemnum=line[33:34]
            itemnumlist.append(itemnum)
            item=line[35:50]
            itemlist.append(item)
            rate=line[51:57]
            ratelist.append(rate) 
            qty=line[58:61]
            qtylist.append(qty)
            discount=line[62:64]
            qtyfloat=float(qty)
            ratefloat=float(rate)
            amt=qtyfloat*ratefloat
            amtlist.append(amt)
            continue
        if (orderfound==1):
            if (ordernumber!=billnum):
                break
    f.close()

    dateright=str.rjust(date, 80)
    title2="BILL"
    s2=str.center(title2, 80)
    print("\n", margin, "\n")
    print(dateright)
    print(s2, "\n")
    print("Order Number :\t", billnum)
    print(margin)
    print("Item No.\t Item \t\t  Price\t\t Qty \t\t Amount")
    print(margin)

    totalcount=0
    total=0
    listlength=len(amtlist)
    while (totalcount!=listlength):
        total=total+amtlist[totalcount]
        totalcount=totalcount+1

    billcount=0
    while (billcount!=listlength):
        rateright=str.rjust(ratelist[billcount],6)
        qtyright=str.rjust(qtylist[billcount], 3)
        amtstr=str(amtlist[billcount])
        amtright=str.rjust(amtstr,7)
        print (itemnumlist[billcount], "\t\t",itemlist[billcount], rateright, "\t",qtyright,"\t\t", amtright)
        billcount=billcount+1


    discountfloat=float(discount)
    discounttotal= total- (discountfloat/100)*total
    gst= (18/100)*discounttotal
    grandtotal=discounttotal+gst
    disctotalstr=str(discounttotal)
    disctotalright=str.rjust(disctotalstr,7)
    totalstr=str(total)
    totalright=str.rjust(totalstr,7)
    gstround=round(gst,2)
    gststr=str(gstround)
    gstright=str.rjust(gststr,7)
    grandround=round(grandtotal, 2)
    grandstr= str(grandround)
    grandtotalright=str.rjust(grandstr,7)
    print(margin)
    print("Total Amount \t\t\t\t\t\t\t", totalright)
    print("Total Amount after  \t\t",discount,"% Discount\t\t\t", disctotalright)
    print("GST \t\t\t\t 18 % \t\t\t\t", gstright)
    print(margin)
    print("Total Bill Amount \t\t\t\t\t\t", grandtotalright)
    print(margin)
##---------------------------------------------------------------------------
takeorder=0
while (takeorder==0):
    billnum=getbillnumber()
    printbill(billnum)
    orderagain=input("Do you want to display another order?(y/n)")
    if (orderagain=="y"):
        continue
    if (orderagain=="n"):
        break
