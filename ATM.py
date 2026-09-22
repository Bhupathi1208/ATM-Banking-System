import time
password=1208
acc_bal=30000
print("WELCOME TO THE SBI ATM")
print("Insert the card")
print("select the option\n 1.yes \n 2.No")
card=int(input())
if card==1:
    print("Select the language\n 1.English\n 2.Teugu\n 3.kannada")
    lang=int(input())
    if lang==1 or lang==2 or lang==3:
        pin=int(input("Enter the pin:"))
        if pin==password:
            print("Choose the option\n 1.Balance Enquiry\n 2.Withdraw")
            choice=int(input())
            if choice==1:
                print("Balance in your account:",acc_bal)
            elif choice==2:
                withdraw_amt=int(input("Enter the amount to withdraw:"))
                if withdraw_amt<=acc_bal:
                    if withdraw_amt%100==0:
                        print("Transaction is processing.....!")
                        time.sleep(5)
                        print("Amount debited in your account=",withdraw_amt)
                        time.sleep(3)
                        print("Do you want to check the balance\n 1.yes\n 2.No")
                        option=input()
                        if option=="1":
                            print("Available balance :",acc_bal-withdraw_amt)
                        elif option==("2"):
                            print("Thank you visit again")
                    else:
                        print("Enter withdraw amount properly")
                else:
                    print("Insufficient balance")
            else:
                print("choose the correct option")
        else:
            print("Incorrect pin")
    else:
        print("Select language properly")
else:
    print("Insert the card properly")