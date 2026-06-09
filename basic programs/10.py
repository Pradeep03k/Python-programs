Account_Balance = 500000
Withdraw_Ammount = int(input("Enter the withdraw amount: "))

if Withdraw_Ammount > 1000 and Withdraw_Ammount<=Account_Balance:
    if Withdraw_Ammount % 100 == 0:
        Account_Balance -= Withdraw_Ammount
        print("-----------------Account Balance------------------")
        print("Account Balance:", Account_Balance)
        print("Withdraw Amount:", Withdraw_Ammount)
        print("Withdraw Amount Successful")
    else:
        print("Amount must be a multiple of 100")       
else:
    print("Invalid amount")

