#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: October 18th 2022
# This program tells the user if they are old enough to
# date their grandchild


def main():

    # Determining whether the user can date their grandchild
    try:
        # Getting the Users age
        user_age_as_string = input("How old are you?  ")
        user_age_as_int = int(user_age_as_string)
    except Exception:
        print(user_age_as_string, "is not valid")

    # Determine whether the user is the right age to date the grandchild
    else:
        if user_age_as_int >= 25 and user_age_as_int <= 40:
            print("You can date my grandchild!")
        else:
            print("I'm sorry, but you cannot date my grandchild")

    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
