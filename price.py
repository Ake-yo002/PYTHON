#We define the function that calculates the final price after after applying the discount
#The parameters are price and discount percent
def calculate_discount(price,discount_percent):
    #Calculate and return the final price after discount
    if discount_percent >= 20:
        discount_amount = price*(discount_percent/100)
        final_price= price - discount_amount
        return final_price
    else:
        return price
#Prompt the user to enter the original price and discount percentage outside of the function
try:
    price=float(input("Enter the price:"))
    discount_percent=int(input("Enter the discount percentage:"))
    #Call the the function with the user's input
    final_price = calculate_discount(price,discount_percent)

    #The final step is printing the results
    if discount_percent>=20:
        print(f"The final price after the {discount_percent}% discount is {final_price}")
    else:
        print(f"The final price is {price} .No discount allowed.")
except ValueError:
    print("Invalid input.PLEASE ENTER NUMERIC VALUES FOR THE ORIGINAL PRICE AND DISCOUNT PERCENTAGES!")