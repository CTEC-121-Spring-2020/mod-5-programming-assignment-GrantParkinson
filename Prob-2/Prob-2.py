# Module 4
#   Programming Assignment 5
#       Prob-2.py

# <Grant Parkinson>

# IPO

# function definition
# inputs: cost of items, amount tendered
# process: calculate change in terms of number of each denomination
# output: summary line, number of each denomination


def change_machine_step_1(amountTendered, costOfItem):
    print()
    print("Cost:$", amountTendered/-100, "Tendered:$",
          costOfItem/-100, "Change:$", (amountTendered - costOfItem)/100)

    ChangeDue = amountTendered - costOfItem

    # tens calculation
    tens = ChangeDue // 1000
    if tens >= 1:
        print(tens, "Tens")
    ChangeDue = ChangeDue - (tens * 1000)

    # Fives calculation
    fives = ChangeDue // 500
    if fives >= 1:
        print(fives, "Fives")
    ChangeDue = ChangeDue - (fives * 500)

    # Ones calculation
    ones = ChangeDue // 100
    if ones >= 1:
        print(ones, "Ones")
    ChangeDue = ChangeDue - (ones * 100)

    # Quarter calculation
    quarters = ChangeDue // 25
    if quarters >= 1:
        print(quarters, "Quarter")
    ChangeDue = ChangeDue - (quarters * 25)

    # Dime calculation
    dimes = ChangeDue // 10
    if dimes >= 1:
        print(dimes, "Dime")
    ChangeDue = ChangeDue - (dimes * 10)

    # nickel calculation
    nickels = ChangeDue // 5
    if nickels >= 1:
        print(nickels, "Nickel")
    ChangeDue = ChangeDue - (nickels * 5)

    # Pennie calculation
    pennies = ChangeDue // 1
    if pennies >= 1:
        print(pennies, "Pennies")

    else:
        print()


def main():
    costOfItem = int(float(input("Enter cost of item: "))*-100)
    amountTendered = int(float(input("Enter change tendered: "))*-100)
    change_machine_step_1(costOfItem, amountTendered)


main()
