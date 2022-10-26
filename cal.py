a=int (input("enter a value"))
b=int(input("enter second value"))
while True:
    print("\n print menu")
    print("1 addition")
    print("2 substraction")
    print("3 division")
    print("4 multiplication")
    print("5 exist")
    choice=int(input("enter you choice"))
    if choice==1:
       sum=a+b
       print("sum=",sum)
    elif choice==2:
        sub=a-b
        print("sub=",sub)
    elif choice==3:
        div=a/b
        print("div=",div)
    elif choice==4:
        mul=a*b
        print("mul=",mul)
    elif choice==5:
        break
    else:
        print("wrong choice")

