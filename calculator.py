x=int(input("Enter the number="));
y=int(input("Enter the second number="));
z=int(input("Enter the operator,1=(+),2=(-),3=(*),4=(/)="));
if z==1:
    a=x+y
    print("the addition is",a);
elif z==2:
    a=x-y
    print("the subtraction is",a);
elif z==3:
    a=x*y
    print("the multiplication is",a);
elif z==4:
    a=x/y
    print("the division is",a);
else:
    print("no command");
