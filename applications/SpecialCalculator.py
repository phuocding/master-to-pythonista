#Calculator Description This mini project Calculator is the implementation of Calculator which can perform different arithematic operations. Few of the most required arithematic operations that must be present in this mini-projects are

#Result after each operation should be stored for future operations Addition of 2 numbers Subtraction of 2 numbers Multiplication of 2 numbers Division of 2 numbers, handle DivisionByZero error Calculating Values of Trignometric Ratio, sin, cos, tan, cot, sec, cosine
print("This Is A Calculator")
print("The Following Task Can Be Done:")
print("--------------------------------")
print("Press 1 For Addition")
print("Press 2 For Substraction")
print("Press 3 For Muliplication")
print("Press 4 For Divison")
print("Press 5 For Calculating Trignometric Ratioes")
print("---------------------------------------------")
print("Please Choose Any")
#Here We are Calling Functions
def statment():
    print("Do You want To Save The result")
    print("Press Y for Yes")
    print("Press N For No")
def call():
    print("Please Enter The Operation To Be Done// For Exit Press N")
    print("---------------------------------------------------------")
    print("Press 1 For Addition")
    print("Press 2 for Substraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
def calling():
    print("Press 1 For Addition")
    print("Press 2 For Substraction")
    print("Press 3 For Muliplication")
    print("Press 4 For Divison")
    print("Press 5 For Calculating Trignometric Ratioes")
    print("---------------------------------------------")
    print("Please Choose Any")
while(True):
    press=int(input())
    if press==1:
        print("You Have Choosed Addition")
        print("--------------------------")
        a = int(input("Please Enter The First No"))
        b = int(input("Please Enter The Secound No"))
        sum = a + b
        print("The result is",sum)
        print("--------------------------------------")
        statment()
        while(True):
            key=input()
            if key=='Y':
                call()
                stroke=int(input())
                if stroke==1:
                    a=int(input("Please Enter The No"))
                    sum=sum+a
                    print("The result is",sum)
                    call()
                if stroke==2:
                    a=int(input("Please Enter The No"))
                    sum=sum-a
                    print("The result is",sum)
                    call()
                if stroke==3:
                    a=int(input("Please Enter The No"))
                    sum=sum*a
                    print("The result is",sum)
                    call()
                if stroke==4:
                    a=int(input("Please Enter The No"))
                    sum=sum/a
                    print("The result is",sum)
                    call()
            if key=='N':
                print("Quitting Now")
                calling()
                break
    if press==2:
        print("You Have Choosed Substraction")
        print("--------------------------")
        a = int(input("Please Enter The First No"))
        b = int(input("Please Enter The Secound No"))
        sum = a-b
        print("The result is",sum)
        print("--------------------------------------")
        statment()
        while(True):
            key=input()
            if key=='Y':
                call()
                stroke=int(input())
                if stroke==1:
                    a=int(input("Please Enter The No"))
                    sum=sum+a
                    print("The result is",sum)
                    call()
                if stroke==2:
                    a=int(input("Please Enter The No"))
                    sum=sum-a
                    print("The result is",sum)
                    call()
                if stroke==3:
                    a=int(input("Please Enter The No"))
                    sum=sum*a
                    print("The result is",sum)
                    call()
                if stroke==4:
                    a=int(input("Please Enter The No"))
                    sum=sum/a
                    print("The result is",sum)
                    call()
            if key=='N':
                print("Quitting Now")
                calling()
                break
    if press==3:
        print("You Have Choosed Multiplication")
        print("--------------------------")
        a = int(input("Please Enter The First No"))
        b = int(input("Please Enter The Secound No"))
        sum = a*b
        print("The result is",sum)
        print("--------------------------------------")
        statment()
        while(True):
            key=input()
            if key=='Y':
                call()
                stroke=int(input())
                if stroke==1:
                    a=int(input("Please Enter The No"))
                    sum=sum+a
                    print("The result is",sum)
                    call()
                if stroke==2:
                    a=int(input("Please Enter The No"))
                    sum=sum-a
                    print("The result is",sum)
                    call()
                if stroke==3:
                    a=int(input("Please Enter The No"))
                    sum=sum*a
                    print("The result is",sum)
                    call()
                if stroke==4:
                    a=int(input("Please Enter The No"))
                    sum=sum/a
                    print("The result is",sum)
                    call()
            if key=='N':
                print("Quitting Now")
                calling()
                break

    if press==4:
        print("You Have Choosed Divison")
        print("--------------------------")
        a = int(input("Please Enter The First No"))
        b = int(input("Please Enter The Secound No"))
        sum = a/b
        print("The result is",sum)
        print("--------------------------------------")
        statment()
        while(True):
            key=input()
            if key=='Y':
                call()
                stroke=int(input())
                if stroke==1:
                    a=int(input("Please Enter The No"))
                    sum=sum+a
                    print("The result is",sum)
                    call()
                if stroke==2:
                    a=int(input("Please Enter The No"))
                    sum=sum-a
                    print("The result is",sum)
                    call()
                if stroke==3:
                    a=int(input("Please Enter The No"))
                    sum=sum*a
                    print("The result is",sum)
                    call()
                if stroke==4:
                    a=int(input("Please Enter The No"))
                    sum=sum/a
                    print("The result is",sum)
                    call()
            if key=='N':
                print("Quitting Now")
                calling()
                break
    if press==5:
        print("You Have Choosed Calculation For Trignomertric Finction")
        print("--------------------------")
        a = int(input("Please Enter A Number"))
        import math
        print("The Cos of",a,"is:",math.cos(a))
        print("The Sine of",a,"is:",math.sin(a))
        print("--------------------------------------")
        statment()
        while(True):
            key=input()
            if key=='Y':
                call()
                stroke=int(input())
                if stroke==1:
                    a=int(input("Please Enter The No"))
                    sum=sum+a
                    print("The result is",sum)
                    call()
                if stroke==2:
                    a=int(input("Please Enter The No"))
                    sum=sum-a
                    print("The result is",sum)
                    call()
                if stroke==3:
                    a=int(input("Please Enter The No"))
                    sum=sum*a
                    print("The result is",sum)
                    call()
                if stroke==4:
                    a=int(input("Please Enter The No"))
                    sum=sum/a
                    print("The result is",sum)
                    call()
            if key=='N':
                print("Quitting Now")
                calling()
                break


