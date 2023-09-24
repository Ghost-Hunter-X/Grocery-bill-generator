

#Variable that can be changed
store_name="Store Name blahblahblah"
#Make item and cost var here
name_0,cost_0="",0
name_1,cost_1="",0
name_2,cost_2="",0
name_3,cost_3="₹1 Items",1
name_4,cost_4="₹2 Items",2
name_5,cost_5="₹5 Items",5
name_6,cost_6="₹10 Items",10
name_7,cost_7="₹20 Items",20
name_8,cost_8="₹30 Items",30
name_9,cost_9="₹50 Items",50

### Program Starts here
import json
import os
import datetime
import re


def header():
    print('|','-'*22,'|')
    print("|","Grocery Bill Generator","|")
    print("|","-"*22,"|")
    print()
    print("|","-"*len(store_name),"|")
    print("|",store_name,"|")
    print("|","-"*len(store_name),"|")
    print()
    print(str(datetime.datetime.now()))
    return

def strip_char(a): # a-Variable, removes char from input
    x = "".join(re.findall("[0-9]|\.",a))
    return x

def clear():
    print("\033c", end='')
    return

def exline(s):
    s.writelines('\n')
    return

def pause():
    input("Press Enter to continue...")
    return


z=0  # Total Price of bill
e=0  # Price of current item being added
x=0  # Input value from user
ender="-"*24 # make lines
a={1:"",2:"",3:name_3,4:name_4,5:name_5,6:name_6,
   7:name_7,8:name_8,9:name_9} # Default price extractor
b={} # Bill counter


clear()
while 1:
    header()
    print_list=(name_0,name_1,name_2,name_3,name_4,name_5,name_6,name_7,name_8
                ,name_9)
    for index, com in enumerate(print_list):
        print(index,com)
    print("c Add custom item")
    print("s To show or save current bill")
    print("h To read history")
    print("f To search name in history")
    print("z To clear Bill")
    print("OR")
    print("e To exit..")
    x=(input("Select item number you want to add to bill:-"))

    
    if x.isnumeric(): # Pre defined prices
        x=int(x)
        if x in range(0,10): 
            if x==0:
                c=cost_0
            elif x==1:
                c=cost_1
            elif x==2:
                c=cost_2
            elif x==3:
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
            y=float(strip_char((input("Enter quantity of selected item or Weight(in KG):-"))))
            d=(c*y)   # cost x quantity
            z=(z)+(d)
            e=b.get(a.get(x),None)   # Checking if selected item is already present in bill
            if e is None:   # If not present
               e=0
            else:   # If present
                e=int(e)
            b[a.get(x)]=e+d    #Adding to bill
            clear()
            print("Item added")
        else:
            pass
        e=0
        
    elif x.isalpha():
        x=x.lower()

        if x=="z": # Clear current bill
            b={}
            z=0
            clear()
            print("Bill Cleared!")


        elif x=="h": # Read history
            print()
            print("-------------------------")
            print()
            print(os.path.abspath("History.txt"))
            r=open("History.txt","r+" ,encoding="utf-8", errors='ignore')
            with open("History.txt","r+",encoding="utf-8", errors='ignore') as f:
                for i in r:
                    print(i.strip('\n'))
            pause()
            clear()


        elif x=="c": # Custom item
            fl=str(input("Enter Name of item = "))
            g=float(strip_char(input("Price per item or per KG = ")))
            h=float(strip_char(input("Number of items or weight(In KG) = ")))
            f=fl.title()
            i=g*h
            e=b.get(f)
            if e is None:
                e=0
            else:
                e=int(e)
            z=(z)+(i)
            b[f]=e+i
            clear()
            print("Item added")

        
        elif x=="s": #Saving bill to file
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
                        history.writelines(ender)
                    xx=xx+1
                history.writelines
                history.close()
                clear()
                print("Bill Saved!""\n""\n")
            elif j=="n" or j.isalnum():
                pass
            clear()


        elif x=="f": #Check this and make it searchable with f
            search=input("Name of customer - ")
            with open("History.txt","r+",encoding="utf-8", errors='ignore') as f:
                for i in f:
                    i=i.strip('\n')
                    if i==ender:
                        #print(ender)
                        end_var=1
                    elif i==search:
                        print(ender)
                        end_var=0
                    else:
                        pass
                    if end_var==0:
                        print(i)
                    else:
                        pass
            print(ender)
            pause()
            clear()


        elif x=="e":
            clear()
            w=input("Are you sure you want to exit?  y=yes OR n=no : ")
            w=w.lower()
            if w=="y":
                print()
                print('Thank you for using our software!')
                pause()
                break
            else:
                pass


    else:
        clear()
        print("\n""\t""Invalid Option!""\n")
