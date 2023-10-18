#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: October 17th, 2023
# this program checks if the number the user inputted is a positive, negative, or zero number.


def main():
    # the user inputs the number, including negatives
    number = int(input("Enter any number: "))
    print("")

    # the terminal will tell the user if the number is positive, negative, or zero
    if number > 0:
        print("the number is a positive number")
    elif number == 0:
        print("the number is zero")
    else:
        print("the number is a negative number")


if __name__ == "__main__":
    main()
