# num3 = 5
# num4 = 10

# # Swapping values using arithmetic operations
# num3 = num3 + num4
# num4 = num3 - num4
# num3 = num3 - num4

# print("After swapping:")
# print("num3 = ",num3)
# print("num4 = ",num4)


# print("After swapping: num3 =", num3, ", num4 =", num4)


# d = int(input("num1 "))
# e = int(input("num2 "))

# temp=d
# d=e
# e=temp

# print(d,e)


# # Input from user
# bill_amount = float(input("Enter the bill amount: "))
# tip_percentage = float(input("Enter the tip percentage: "))
# num_people = int(input("Enter the number of people to divide the bill: "))

# # Calculate the tip and total bill
# tip = (tip_percentage / 100) * bill_amount
# total_amount = bill_amount + tip

# # Calculate amount per person
# amount_per_person = total_amount / num_people

# # Output results
# print("Total bill (including tip):",total_amount)
# print("Amount per person: ",amount_per_person)


name = "shreya"
print(name,type(name))

inte = 23
print(inte,type(inte))

flo = 23.54
print(flo,type(flo))


# Food items available at the restaurant
food_available = ['burger', 'veg pizza', 'momos', 'chinese', 'garlic bread', 'french fries', 'non-veg pizza']

# Displaying food list and its type
print("Food available at restaurant:", food_available)
print("Data type of food:", type(food_available))

# Displaying total food items
print("Total food items:", len(food_available))

# Food items not available
food_not_available = ['momos', 'chinese', 'garlic bread']
print("Food at present not available:", food_not_available)

# Adding one more item
food_available.append('kabab')
print("Updated food list:", food_available)
