
def SolidSquare():

    no_of_start=int(input("enter the row required for rectangle "))
    for i in range(1,no_of_start+1):


        for j in range(1,no_of_start+1):

            print('*',end="")
        print("")
    return 

def HollowSquare():
    no_of_rows=int(input("enter the row required for rectangle "))
    for i in range(1,no_of_rows+1):
        if i==1 or i==no_of_rows:
            for j in range(1,no_of_rows+1):
                print('* ',end="")
        else:
            for j in range(1,no_of_rows+1):
                if j==1 or j==no_of_rows:
                    print("*",end="")
                else:
                    print("  ",end="")
        print("")      
        print("")
    return 

def LeftangledTraingle():
    no_of_rows=int(input("enter the no of rows"))
    for i in range(1,no_of_rows+1):
        for j in range(1,i+1):
            print("*",end="")
        print("")
def HollowLeft():
    no_of_rows=int(input("enter your rows"))
    for i in range(1,no_of_rows+1):
        if i < no_of_rows:
            for j in range(1,i+1):
                if j==1 or j==i:
                    print("*",end="")
                else:
                    print(" ",end="")
            print("")
        else:
            for j in range(1,no_of_rows+1):
                print("*",end="")
            print("")

def RightalignedhollowTriangle():
    no_of_rows=int(input("enter the no of rows"))
    for i in range(1,no_of_rows+1):
        for j in range(1,no_of_rows-i+1):
            print(" ",end="")
        
        if i==1 or i==no_of_rows:
            for k in range(1,i+1):
               
                print("*",end="")
               
        else:
            for k in range(1,no_of_rows+1):
                if k==1 or k==i:

                    print("*",end="")
                else:
                    print(" ",end="")
        print("")
def fullStarPyramid():
    no_of_rows=int(input(" enter the no of rows"))
    for i in range(1,no_of_rows+1):
        blankspace=no_of_rows-i
        start=2*i-1
       
        print(" "*blankspace+"*"*start+" "*blankspace,end="")
        print(" ")
def hollowPyramid():
    no_of_row=int(input("no of rows"))
    for i in range(1,no_of_row+1):
        blankspace=no_of_row-i
        for j in range(1,i+1):
            
            if j==i or j==no_of_row:
                insideblank=2*i-1
                print(" "*blankspace+"*"+""*insideblank+""*blankspace)
        print("")
def mirrorPyramid():
    no_of_rows=int(input("enter the no of rows "))
    for i in range(1,no_of_rows+1):
        blank_space=no_of_rows-i
        print(" "*blank_space+"*"*i+" "*blank_space)
    print(" ")
def diamond():
    no_of_rows=int(input("enter the no of rows "))
    for i in range(1,no_of_rows+1):
        star=2*i-1
        blankspace=no_of_rows-i
        print(" "*blankspace+"*"*star+" "*blankspace)
  
    for i in range(no_of_rows,0,-1):
        star=2*i-1
        blankspace=no_of_rows-i
        print(" "*blankspace+"*"*star+" "*blankspace)
    print("")


   

        


          

          
    

def Printpattern():

    Options='yes'
    while Options !="no":

        
        print("---Choice---")
        print("1:for Solid Sqaure \n" 
        "2:for Hollow square\n"
        "3:for left alinged  right angled trianlge\n"
        "4:for left hollow aligned right angled triangle\n"
        "5: for hollow right aligned triangle\n"
        "6:centered star\n"
        "7:hollow centered start\n"
        "8:Mirror Pyramid")
        choice=int(input("Enter your choice "))

        if choice==1:
             
            SolidSquare()
        elif choice==2:
            HollowSquare()
        elif choice==3:
            LeftangledTraingle()
        elif choice==4:
            HollowLeft()
        elif choice==5:
            RightalignedhollowTriangle()
        elif choice==6:
            fullStarPyramid()
        elif choice==7:
            hollowPyramid()
        elif choice==8:
            mirrorPyramid()
        elif choice==9:
            diamond()



           
        
        else:
            print("invalid Choice")
        
        Options=input("Do you want to continue yes/no")


    
if __name__ == "__main__":
    Printpattern()
