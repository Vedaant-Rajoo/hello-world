#INPUT
namt,bal=raw_input("").split()
fbal=float(bal)
amt=int(namt)
nbal=("%.f" %round(fbal,2))
ibal=int(round(fbal))
tax=0.50
temp=float(nbal)
if amt in range(1,2001) and ibal in range(0,2001):
    if amt%5==0:
        if amt<=ibal:
            temp=(temp-amt)-0.50
            print ("%.2f" %temp)
        else:
            print bal
    else:
        print bal

  
