class BankAccount:
    def __init__(self,accno,name,type,bal):
        self.accountnumber=accno
        self.Name=name
        self.AccountType=type
        self.Balance=bal
    def deposits(self,amt):
        self.Balance=self.Balance+amt
        print("the deposited amount is:",self.Balance)
    def withdraw(self,amt):
        if self.Balance==0:
            print("balance is zero")
        else:
            self.Balance=self.Balance-amt
            print(self.Balance)
a1=BankAccount(1000000,"ansar","saving",5000)
while (True):
    print("\n 1:deposit \n 2:withdraw \n 3:exit")
    op=int(input("enter your choice: "))
    if (op==1):
        a1.deposits(1000)
    elif (op==2):
        a1.withdraw(200)
    else:
        exit(0)                