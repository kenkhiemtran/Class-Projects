#==========================================
#       IS340     PROJECT 1       KEN TRAN                          =
#==========================================
import datetime  #importing the date/time module

#Assigning differrent prices and rates
AdventurePrice  = 450 
DeluxePrice     = 675
ElephantPrice   = 150
taxRate = 0.095

loopAgain = True
while loopAgain:
    print()
#Gathering input from the user 
    number_of_people = int(input("Enter Number of People: ")) #Asking the number of people on the tour

    safariChoice = input("Which type of Safari A - Adventure or D - Deluxe: ").lower() #Asking for type of Safari
    if safariChoice not in ['a', 'd']:
        print("Oops! Please enter A or D ")
        continue                                                            
    

    while True:
        elephantChoice = input("Ride Elephants Y/N: ").lower() #Asking if they want to ride elephants or not
        if elephantChoice in ['y','n']:
            break                                              #Exit loop if choice in selection
        else:
            print ("Oops! Please enter Y or N.")               
            continue                                           #Go back to the start of the loop to ask for input again
        
    while True:
        memberChoice = input("Are you a member? Y/N: ").lower()#Asking if they are members or not
        if memberChoice in ['y' , 'n']:                        
            break                                              #Exit loop if choice in selection              
        else:
            print ("Oops! Please enter Y or N.")
            continue                                           #Go back to the start of the loop to ask for input again

#Calculations 
    if safariChoice  == ("a"):                                #Calculating price based on type of safari  
        safariTotal = number_of_people * AdventurePrice
    else:
        safariTotal = number_of_people * DeluxePrice


    if elephantChoice == "y":                                 #Calculating price based on if they choose elephant or not  
            elephantTotal = number_of_people * ElephantPrice
    else:
            elephantTotal = 0




    Subtotal = safariTotal +  elephantTotal                   
    

    if memberChoice == "y":                                   #Calculating discount price based on if they're members or not 
            Total_discount = Subtotal * 0.1
    else:
            Total_discount = 0




    taxesDue =(Subtotal - Total_discount) * (1 - taxRate)     #Calculating the taxes due

    Total =(Subtotal - Total_discount ) + taxesDue            #Total amount due at the end of the message
        

    print()                                                   #Printing all the values from the calculations.
 
    print(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S} ")
    print(f"Safari cost is: {safariTotal:.2f}")
    print(f"Elephants cost is: {elephantTotal:.2f}")
    print(f"Subtotal is: {Subtotal:.2f}")
    print(f"Discount is: {Total_discount:.2f}")
    print(f"Total due after discount is: {Subtotal - Total_discount:.2f}")
    print(f"Taxes due is: {(taxesDue):.2f}")
    print(f"Total amount due after taxes is {Total:.2f}")
 
    print("\n\n")
     
    again = input("Make another reservation? Y/N: ").lower()    #Asking if they want to continue another transaction 
   
    if again != "y":                                            #If y the loop is ran again, if not the loop ends
        loopAgain = False


print(f"Thank you,and goodbye\n\n\n")


            


            


                       
          
