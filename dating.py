#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: October 18th 2022
# This program tells the user if they are old enough to
# date their grandchild


def main():
    # Getting the Users age
    user_age = int(input("How old are you?  "))
    print("")
    # Determining whether the user can date their grandchild
    if user_age >= 25 and user_age <= 40:
        print("You can date my grandchild!")
    else:
        print("I'm sorry, but you cannot date my grandchild")


if __name__ == "__main__":
    main()
