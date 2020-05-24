# Module 4
#   Programming Assignment 5
#       Prob-3.py

# <Grant Parkinson>

# input: job size in square feet, cost of paint per gallon
# process: calculate estimate
# output: print estimate

# function definition


# main function definition


def job_price(Squarefeet, gallon_price):

    multiplyer = round(Squarefeet / 112)

    labor_cost = multiplyer * 8 * 35

    paint_cost = multiplyer * gallon_price

    total_cost = paint_cost + labor_cost + 99

    print("\nGallons required:", multiplyer)
    print("Labor hours required:", (multiplyer*8))
    print("Paint cost: $", paint_cost)
    print("Labor cost: $", labor_cost)
    print("Total cost: $", total_cost)


def main():
    Squarefeet = float(input("Enter square feet:"))
    gallon_price = float(input("Enter price per gallon:"))
    job_price(Squarefeet, gallon_price)


main()
