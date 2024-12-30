fruits = ['mango', ['fruitpulp', 'mixedpulp'], 'banana', ('apple', 'grapes')]

print(fruits[0])
print(fruits[1])
print(fruits[1][0])
print(fruits[1][1])
print(fruits[3][0])  
print(fruits[3][1])  


Menu = ['Dal', 'Paneer', 'Kofta', 'Tawa Paneer', 'Rice', 'Roti']

for i in range(len(Menu)):
    print(f"Menu item: {Menu[i]}")

author_name = ('j k rowling', 'rachel aaron', 'hans aanrud', 'verna aardema')

for i in range(len(author_name)):
    print(f"Author: {author_name[i]}")

Timing = 'It\'s 7.30am'
print(Timing)


# Taking input from the user
employee_name = input("Enter Employee Name : ")
salary = input("Enter Salary : ")


company = "ChangPond Technology"

print("\nPrinting Employee Details")
print(f"Name   Salary   Company")
print(f"{employee_name}   {salary}   {company}")


print('Hello World')
print(r'E:\ChangpondNewBatch\Python')

# Create a string list
string_list = []
size = 5  # Fixed size for the list
print('Enter 5 string values:')
for i in range(size):
    value = input(f'Enter string {i + 1}: ')
    string_list.append(value)

# # Create a float list
float_list = []
size = int(input("Enter the size: "))  # Convert input to an integer
print(f'Enter {size} float values:')

for i in range(size):
    value = float(input(f'Enter float {i + 1}: '))
    float_list.append(value)

print("The entered float values are:", float_list)


print("Float List:", float_list)
print("String List:", string_list)

