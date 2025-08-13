# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount.
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
# If the discount is 20% or higher, apply the discount; 
# otherwise, return the original price.
# Using the calculate_discount function, 
# prompt the user to enter the original price of an item and the discount percentage.
# Print the final price after applying the discount, or if no discount was applied, print the original price.

def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or more
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract the discount from the original price
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Ask the user to enter the original price
price_input = float(input("Enter the original price of the item: "))

# Ask the user to enter the discount percentage
discount_input = float(input("Enter the discount percentage: "))

# Use the function to calculate the final price
final_price = calculate_discount(price_input, discount_input)

# Print the result
print("The final price is:", final_price)