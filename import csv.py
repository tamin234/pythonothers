import csv 
fh=open("inventoryforfruitsitem.csv","w+",newline="")
w=csv.writer(fh)
header=['fruits name','unit price','quantity','total price']
w.writerow(header)
data=[]
while True:
    try:
        n=int(input("How many insert fruits record "))
    except ValueError:
        print("Fruits Record are number please again entered")
        continue
    else:
        break
for i in range(n):
    print(f"Enter fruits record {i+1}: ")
    fruitsname=input("Enter Fruits name: ")
    while True:
        try: 
            unitprice=float(input("Enter Unit Price: "))
        except ValueError:
            print("invalid Unit price please Entered again: ")
            continue
        else:
            break
    while True:
        try:
            quantity=int(input("Enter quantity "))
        except ValueError:
            print("invalid quantity please Entered again")
            continue
        else:
            break
    totalprice=unitprice*quantity
    res=[fruitsname,unitprice,quantity,totalprice]
    data.append(res)
w.writerows(data)
fh.close()
print("print truits items summary data from stored CSV file")
fh=open("inventoryforfruitsitem.csv","r")
r=csv.reader(fh)
for i in r:
    print(i)
fh.close()