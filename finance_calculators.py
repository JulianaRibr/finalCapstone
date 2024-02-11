import math

while True:
    print("investment - to calculate the amount of interest you'll earn on your investment.")
    print("bond - to calculate the amount you'll have to pay on a home loan.")

    option = input("\nEnter either 'investment' or 'bond' from the menu above to proceed:") # Ask the option to the user

    option = option.lower() # To force the input to be lower case for the comparison

    if option == "investment": # Don't forget the colon
        try:
            money = float(input("\nEnter the amount of money you are depositing:"))
            interest_rate = float(input("Enter the interest rate:"))
            interest_rate = interest_rate / 100 # Convert the variable to calculate the total amount
            years = float(input("Enter the number of years do you plan to invest:"))
            interest_type = input("Do you want 'simple' or 'compound' interest?")
            interest_type = interest_type.lower() # To force the input to be lower case for the comparison
            
            if interest_type == "simple":
                total_amount = money * (1 + interest_rate * years) # Simple interest formula
                print(f"\nTotal Amount is {total_amount}.")
            elif interest_type == "compound":
                total_amount = money * math.pow((1 + interest_rate), years) # Compound interest formula
                print(f"\nTotal Amount is {total_amount}.")
            else:
                print("\nPlease, enter 'simple' or 'compound' to calculate the total amount:")
                # Don’t forget to show an appropriate error message, in case the user doesn’t type in a valid input.

        except ValueError:
            print("\nPlease, enter a numerical value!") 
            # Don’t forget to show an appropriate error message, in case the user doesn’t type in a valid input.
        
    elif option == "bond":
        try:
            house_value = float(input("\nEnter the present value of your house:"))
            yearly_interest_rate = float(input("Enter the interest rate:")) / 100
            monthly_interest_rate = (yearly_interest_rate / 12) # Convert the variable to calculate the repayment value
            months = float(input("Enter the number of months you plan to take to repay the bond:"))
            repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate)**(-months))
           
            print(f"\nEvery month you'll have to repay {repayment}.")

        except ValueError:
            print("\nPlease, enter a numerical value!")
            # Don’t forget to show an appropriate error message, in case the user doesn’t type in a valid input.
     
    else:
        print("\nInvalid option! Please, enter either investment or bond.")