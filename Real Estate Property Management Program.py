#PROJECT 2
loopAgain = True
import math
#Dictionaries to rental and sale properties 
forrent = { "1542 Bartlett #199D"    :2183,
            "1026 17th St #124A"     :1900,
            "728 16th St #18M"       :2633,
            "1010 11th #2D"          :3406}

forsale = {"4220 Edison Ave"    :325000,
           "2209 Gila Way"      :650000,
           "4640 Sagar Ave"     :875000,
           "3780 Las Pasas Way" :1740000}
#Function to display main menu 
def displayMenu():
    print("\n1.Show Available Properties")
    print("2.Add Properties")
    print("3.Calculate Monthly Loan Payments")
    print("Q.Quit")
    choice = input("\nEnter your choice: ").upper()
    #Code to validate the user's choice.
    if choice not in ('1', '2', '3', 'Q'):
        print("Oops! Please Select A Valid Input!")
    return choice
   
#Function to show available properties 
def showProperties():
    while True: #Display options for property type
        print("\nWhich type of property are you looking for?")
        print("S Home for Sale")
        print("R Rentals")
        print("B Both")
        #Get the user's choice of property type
        property_choice = input("Select (S,R,B):").upper()
        #Display property based on user's selection
        if property_choice == 'S':
                showForSale()
                break
        elif property_choice == 'R':
                showForRent()
                break
        elif property_choice == 'B':
                showForSale()
                showForRent()
                break
        else:
            print("\nInvalid Input! Please Select Again!")
            continue

#Function to display rental properties
def showForRent():
   print(f'\n{"RENTALS":<16}{"PRICE":>14}')
   for theKey in forrent.keys():
        print(f"{theKey:<21} {forrent[theKey]:>12,} monthly")

#Function to display properties for sale
def showForSale():
    print(f'\n{"FOR SALE":<16}{"PRICE":>14}')
    for theKey in forsale.keys():
        print(f'{theKey:<21} {forsale[theKey]:>12,}')

#Function to add rental or sale properties   
def addProperties():
    while True:#Display options for property type
        print(f'\nWhat type of property do you want to add?')
        print("R Rentals")
        print("S Homes for Sale")
        #Get the user's choice of property type
        addChoice = input("Enter your choice (R,S):").upper()
        if addChoice == "R":
            addForRent()
            break
        elif addChoice== "S":
            addForSale()
            break
        else:
            print("\nInvalid Input! Please Select Again!")
            continue
            
        
#Function to add a rental property
def addForRent():
    while True:
        #Get property address and value from user
        address = input("\nEnter the address of the property:")
        value_input = input("Enter the value of the property:")
        #Validate the value inputed is a number
        if value_input.isdigit(): 
            value = int(value_input)
            break
        else:
            print("\nPlease enter an numeric value for property.")
            continue
    #Add the property to the global dictionary
    forrent[address]= value
    showForRent()

#Function to add a property for sale
def addForSale():
    while True:
        #Get property address and value from user
        address = input("\nEnter the address of the property:")
        value_input = input("Enter the value of the property:")
        #Validate the value inputed is a number
        if value_input.isdigit():
            value = int(value_input)
            break
        else:
            print("\nPlease enter an numeric value for property.")
            continue
    #Add the property to the global dictionary
    forsale[address]= value
    showForSale()

#Funcion to calculate monthly loan payment base on user's input
def calcMonthlyLoanPayment(LoanAmount,InterestRate,YearsTilMaturity):
    #Calculate the monthly interest rate
    monthlyRate = InterestRate / 100 / 12
    #Calculate the monthly payment
    monthly_payment =(LoanAmount * monthlyRate)/(1 - math.pow((1+monthlyRate),(-12*YearsTilMaturity)))
    #Calculate total payments and interest paid 
    total_payments = monthly_payment * 12 * YearsTilMaturity
    total_interest = total_payments - LoanAmount
    
    return monthly_payment,total_payments,total_interest

#Function to get loan information from the user 
def getMonthlyLoanPayment():
    while True:
        #Get years until loan maturity and validate the input (30 if left blank) 
        years_input = input("\nYears until loan maturity (leave blank for 30):")
        if years_input == "":
            N = 30
            break
        elif years_input.isdigit():
            N = int(years_input)
            if N > 0:
                break
            else:
                print("\nYears until loan maturity must be greater than zero.")
        else:
            print("\nInvalid Input! Please Enter an Integer!")
    #Get the loan amount and validate the input
    while True:
        loan_amount = input("Enter the loan amount(Pricipal): ")
        if loan_amount.replace(".", "").isnumeric():
            P = float(loan_amount)
            if P > 0:
                break
            else:
               print("\nPrincipal must be greater than zero.")
        else:
            print("\nInvalid Input! Please Enter a Integer or Float!")
    #Get the interest rate and validate the input
    while True:    
        interest_input = input("Enter the Annual Interest Rate: ")
        if interest_input.replace(".", "").isnumeric():
            R = float(interest_input)
            if R <= 0:
                print("\nAnnual interest rate must be greater than zero.")
            elif R > 18.5:
                print("\n18.5% is the maximum interest rate by state law.")
            else:
                break
        else:
            print("\nInvalid Input! Please Enter an Integer or Float!")
    #Call the loan payment calculation with the user's inputs 
    monthly_payment,total_payments,total_interest = calcMonthlyLoanPayment(P, R, N)
    return monthly_payment,total_payments,total_interest

#Main function to run the program
def main():
    while True:
        #Display the main menu and get the user's choice
        choice = displayMenu()
        #Call on appropriate funtions depending on the user's choice

        if choice == '1':
           showProperties() #Show properties

        elif choice == '2':
            addProperties() #Add property

        elif choice == '3':
           #Calculate and display loan payments
           monthly_payment,total_payments,total_interest = getMonthlyLoanPayment()
           print(f"\nThe monthly payment is: ${monthly_payment:,.2f}")
           print(f"The total interest paid is: ${total_interest:,.2f}")
           print(f"The total amount paid is: ${total_payments:,.2f}")

        elif choice == 'Q':
            #Exit the program when user wants to quit
            print("\nGoodbye, Thank you")
            break


#Calling function to run the program
main()
