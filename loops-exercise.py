# Question 1
# continuously ask the user to enter a number until they provide a blank input
# output the sum of all the numbers


new_numbers = []

number = (input("Please enter a number: "))

while number:
        new_numbers.append(int(number))
        number = (input("Please enter a number: ")) 
total = sum(new_numbers)
print(total)  


# number = (input("Please enter a number: ")
# while len(number) > 1:
#     if number => 1:
#     int(number) 
#     else:
#         print

# numbers = []

# new_numbers = input("Please enter a number: ")
# while int(new_numbers) > 1:
#     numbers.append(new_numbers)
#     new_numbers = (input("Please enter a number: "))
#     result = (sum(new_numbers))
#     print(result)

# number = input("Enter a number ")
# while len(number) > 1:
#     if number > 1:
#         print ("test working")
#     else:
#         print("try again")
#     number = input("Enter a number")   

# numbers = []
# number = int(input("Enter a number: "))
# while int(number) > 0:
#     if number =>5:
#         numbers = int(input('Enter number '))
#         numbers.append(number)
#         print(sum(lst))

# Question 2

# mailing_list = [
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"], 
#     ["Biscuit", "biscuit@whippies.park"],
#     ["Rory", "rory@whippies.park"],
# ]

# print(mailing_list)

# for details in mailing_list:
#     print(f"{details[0]}: {details[1]}")


# Question 3
# use a while loop to ask the user for 3 names and append them to a list
# then use a for loop to print the list


# names = []
# count = 0
# while count < 3:
#     name = input("What is your name? ")
#     names.append(name)
#     count += 1
#     print()

# for name in names:
#     print(name)


# Question 4

# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]

# total = 0

# for item in groceries:
#     quantity = input(f"How many {item[0]} did you buy? ")
#     item[1] = item[1] * int(quantity)
#     total += item[1]

# print(f"====Izzy's Food Emporium====")
# for item in groceries:
#     print(f"{item[0]:<20} ${item[1]:.2f}")
# print(f"${total:>25.2f}")
# print(f"============================")
