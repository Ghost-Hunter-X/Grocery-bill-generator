print("|------------------------|","| Grocery Bill Generator |","|------------------------|", sep='\n')
print("|------------|","| Store Name |","|------------|", sep='\n')
def exline(s):
    s.writelines('\n')
import datetime
print(str(datetime.datetime.now()))
z=0
e=0
x=0
a={1:"",2:"",3:"₹1 Items",4:"₹2 Items",5:"₹5 Items",6:"₹10 Items",7:"₹20 Items",8:"₹30 Items",9:"₹50 Items"}
b={}
while x in range(0,12):
    print("1:History","2:clear current","3:1₹ Items","4:2₹ Items","5:5₹ Items","6:10₹ Items","7:20₹ Items","8:30₹ Items","9:50₹ Items","10:Print Bill","0:Custom item","Or Any other key to exit..", sep = '     ')
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
                history = open('History.pickle','a+' , encoding="utf-8")
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
                        history.writelines("-------------------------")
                    xx=xx+1
                history.writelines
                history.close
                print("Saved!""\n""\n")
            elif j=="n" or j.isalnum():
                pass
        elif x in range(3,10): #Pre defined prices
            if x==3:
                c=1
            elif x==4:
                c=2
            elif x==5:
                c=5
            elif x==6:
                c=10
            elif x==7:
                c=20
            elif x==8:
                c=30
            elif x==9:
                c=50
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
            r=open("History.pickle","r+" ,encoding="utf-8")
            with open("History.pickle","r+",encoding="utf-8") as f:
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
            print("Thank you for using our software!")
            break
        else:
            x=0
