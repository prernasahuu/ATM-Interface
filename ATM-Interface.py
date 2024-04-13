user_id = "user ID"
pin= 9294 #user pin
user = str(input("Enter your user ID: \n"))
user_pin = int(input("Enter the four digit pin: \n"))
balance = 500000
transcation_history= {'11-4-2024' : 2000,
                      '10-4-2024' : 100000,
                      '09-4-2024': 200,
                      '08-4-2024': 45000,
                      '07-4-2024': 499,
                      '06-4-2024': 10,
                      '04-4-2024' : 849 }
if user == user_id && pin == user_pin:
    while True:
        print("WELCOME TO SWISS BANK")
        print("============================================================================================================================================")

        print("""
            1 == Transaction History
            2 == Withdraw
            3 == Deposit
            4 == Transfer
            5 == Quit
            """)
        print("============================================================================================================================================")
        try:
            option = int(input("Choose the service number: \n"))
        except:
            print(" Enter a valid service number: \n")
        if option == 1:
            print("Your Transcation History for 7 days: \n", transcation_history)
            print("============================================================================================================================================")
            print("============================================================================================================================================")
            print("============================================================================================================================================")
        if option ==2:
            amt= int(input("Enter the withdrawal amount: \n"))
            amt_balance = (balance - amt)
            print(f"{amt} is debited from your account")
            add = (input("Display the current balance Y/N: \n"))
            if add == "Y":
                print("The current balance is : \n",dt_balance)
                
            elif add == "N":
                print("Thank You Visit again")
            print("============================================================================================================================================")
            print("============================================================================================================================================")
            print("============================================================================================================================================") 
        if option == 3:
            dpt= int(input("Enter the amount to be deposited: \n"))
            dpt_balance= (balance + dt)
            print(f"{dpt} has been cerdited successfully to your account")
            add = (input("Display the current balance Y/N: \n"))
            if add == "y":
                print("The current balance is : \n",dpt_balance)
                
            elif add == "n":
                print("Thank You Visit again")
            print("============================================================================================================================================")
            print("============================================================================================================================================")
            print("============================================================================================================================================") 

            
        if option == 4:
            print("""
                1 == Self Transfer
                2 == Account Transfer """)
            try:
                opt = int(input("Choose the tranfer mode number: \n"))
            except:
                print(" Enter a valid transfer mode number: \n")
            if opt == 1:
                    tf= int(input("Enter the amount to be tranferred: \n"))
                    tf_balance= (balance+ f)
                    print(f"{tf} has been successfully tranferred to your account")
                    add = (input("Display the current balance Y/N: \n"))
                    if add == "y":
                        print("The current balance is : \n",tf_balance)
                
                    elif add == "n":
                        print("Thank You Visit again")
                    print("============================================================================================================================================")
                    print("============================================================================================================================================")
            elif opt == 2:
                    user2 = str(input("Enter the User ID number: \n"))
                    tf= int(input("Enter the amount to be tranferred: \n"))
                    user_pin = int(input("Enter the four digit pin: \n"))
                    if user_pin == pin:
                            print(f"You have successfully transferred the{tf} to {user2}")
                            at_balance = (balance -f)
                            add = (input("Display the current balance Y/N: \n"))
                            if add == "Y":
                                print("The current balance is : \n",at_balance)
                            elif add == "N":
                                print("Thank You Visit again")
                    else:
                            print("Please enter the valid pin")
                    
            print("============================================================================================================================================")
            print("============================================================================================================================================")
            print("============================================================================================================================================") 

            
        if option == 5:
            break
        print("THANK YOU, VISIT AGAIN")
        print("============================================================================================================================================")
        print("============================================================================================================================================")

else:
    print("invalid user ID or user pin, try again")
