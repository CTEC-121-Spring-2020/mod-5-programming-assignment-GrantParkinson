# Module 4
#   Programming Assignment 5
#       Prob-1.py

# <Grant Parkinson>

# IPO

# function definition


def number_conversion(x):
    if x == 1:
        return 'I'
    elif x == 2:
        return 'II'
    elif x == 3:
        return 'III'
    elif x == 4:
        return 'IV'
    elif x == 5:
        return 'V'
    elif x == 6:
        return 'VI'
    elif x == 7:
        return 'VII'
    elif x == 8:
        return 'VIII'
    elif x == 9:
        return 'IX'
    elif x == 10:
        return 'X'
    else:
        return 'INVALID - Input a number between 1 and 10'

# unit test function


def unitTest():
    print("\nUnit Tests")
    print(number_conversion(1))
    print(number_conversion(2))
    print(number_conversion(3))
    print(number_conversion(4))
    print(number_conversion(5))
    print(number_conversion(6))
    print(number_conversion(7))
    print(number_conversion(8))
    print(number_conversion(9))
    print(number_conversion(10))
    print(number_conversion(-1))
    print(number_conversion(20))
    print("--------------------------\n\n")


def final_execution():
    number = int(input("Input a number between 1 and 10: "))
    if 1 <= number <= 10:
        print("Input number", number, "translates to",
              number_conversion(number), "in Roman Numerals.")
    else:
        print("INVALID - Input a number between 1 and 10")


def main():
    final_execution()


unitTest()
main()
