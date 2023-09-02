#Variable that can be changed
store_name="Store Namefkcyhuifwfihkjjj"
#Make item and cost var here
name_3,cost_3="₹1 Items",1
name_4,cost_4="₹2 Items",2
name_5,cost_5="₹5 Items",5
name_6,cost_6="₹10 Items",10
name_7,cost_7="₹20 Items",20
name_8,cost_8="₹30 Items",30
name_9,cost_9="₹50 Items",50


import json
import os
print('|','-'*22,'|')
print("| Grocery Bill Generator |")
print("|","-"*22,"|")
print()
print("|","-"*len(store_name),"|")
print("|",store_name,"|")
print("|","-"*len(store_name),"|")
print()
def exline(s):
    s.writelines('\n')
import datetime
print(str(datetime.datetime.now()))
z=0
e=0
x=0
a={1:"",2:"",3:name_3,4:name_4,5:name_5,6:name_6,
   7:name_7,8:name_8,9:name_9}
b={}
while x in range(0,12):
    print_list=("Custom item","History","clear current",name_3,name_4,name_5,name_6,name_7,name_8
                ,name_9,"Print Bill")
    for index, com in enumerate(print_list):
        print(index,com)
    print("Or Any other key to exit..")
    x=(input("Select item number you want to add to bill:-"))
    if x.isnumeric():
        x=int(x)
        if x==10:
            for key,value in b.items():
                if value<=0:
                    pass
                else:
                    print(key ,":" ,value)
            print("Total :",z)
            j=input("Do you want to save bill?   y=Yes , any other key=no")
            j=j.lower()
            if j=="y":
                nam=str(input("Name of customer: "))
                print("Saving...")
                history = open('History.txt','a' , encoding="utf-8")
                history.writelines(nam)
                exline(history)
                now = datetime.datetime.now()
                history.writelines(str(now))
                exline(history)
                exline(history)
                for key,value in b.items():
                    if value<=0:
                        pass
                    else:
                        k=str(value)
                        history.writelines((key ," = ₹" ,k))
                        exline(history)
                history.writelines(("Total = ₹",str(z)))
                xx=0
                for xx in range(0,4):
                    exline(history)
                    if xx==1:
                        history.writelines("-"*24)
                    xx=xx+1
                history.writelines
                history.close()
                print("Saved!""\n""\n")
            elif j=="n" or j.isalnum():
                pass
        elif x in range(3,10): #Pre defined prices
            if x==3:
                c=cost_3
            elif x==4:
                c=cost_4
            elif x==5:
                c=cost_5
            elif x==6:
                c=cost_6
            elif x==7:
                c=cost_7
            elif x==8:
                c=cost_8
            elif x==9:
                c=cost_9
            y=float(input("Enter quantity of selected item or Weight(in KG):-"))
            d=(c*y)
            z=(z)+(d)
            e=b.get(a.get(x),None)
            if e is None:
               e=0
            else:
                e=int(e)
            b[a.get(x)]=e+d
        elif x==0: # Custom item
            fl=str(input("Enter Name of item = "))
            g=float(input("Price per item or per KG = "))
            h=float(input("Number of items or weight(In KG) = "))
            f=fl.title()
            i=g*h
            e=b.get(f)
            if e is None:
               e=0
            else:
                e=int(e)
            z=(z)+(i)
            b[f]=e+i
        elif x==1: #Read history
            print()
            print("-------------------------")
            print()
            print(os.path.abspath("History.txt"))
            r=open("History.txt","r+" ,encoding="utf-8", errors='ignore')
            with open("History.txt","r+",encoding="utf-8", errors='ignore') as f:
                for i in r:
                    print(i.strip('\n'))
        elif x==2: #Clear current bill
            for key1,value1 in b.items():
                key1=str(key1)
                key1.isalnum()
                del b
                b={}
                z=0
            print("Bill Cleared!")
        else:
            print("\n""\t""Invalid Option!""\n")
        e=0
        x=0
    else:
        w=input("Are you sure you want to exit?  y=yes OR n=no : ")
        w=w.lower()
        if w=="y":
            print()
            print('Thank you for using our software!')
            break
        else:
            x=0
