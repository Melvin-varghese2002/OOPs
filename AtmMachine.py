class Atm_machine :
    def __init__ (self,name,acc_number) :
        self.name = name
        self.acc_number = acc_number
        print("Account Details\n_______________")
        print("Account Holder :",self.name)
        print("Account Number :",self.acc_number)
        print("1. Deposit Money \n2. Withdraw Money\n3.View Balance\n4. EXIT")

    def operation (self,choice) :
        self.choice = choice
        balance = 0
        while choice != 4 :
            if choice == 1 :
                deposit_amount = int(input("Enter the amount to be deposited :"))
                balance = balance + deposit_amount
                print("Amount deposited succesfully!!")

            elif choice == 2 :
                withdraw_amount = int(input("Enter the amount to be withdrawn :"))
                balance = balance - withdraw_amount
                print("Amount withdrawn successfully!!")

            elif choice == 3 :
                print("Account balance :",balance)

            else:
                print("invalid choice")
            choice = int(input("Enter your choice :"))


details = Atm_machine(input("Enter the account holder name :"),int(input("Enter the account number :")))
details.operation(int(input("Enter your choice :")))