row=int(input("enter the number row:"))
for i in range(1,row+1):
    for i in range(1,row+1):
        for j in range(1,i+1):
            print(i*j,end=' ')
        print()
