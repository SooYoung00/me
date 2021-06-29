"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        try:
            value = int(input(message))
            print("Thanks {} looks right".format(value))
            return value
        except Exception as e:
            print("Please enter a number ({})".format(e))


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    while True:
        try:
            value = int(input("Please enter a number: "))
            if low <= value <= high:
                print("That is correct")
                return value
            else:
                print("please try again")
        except Exception as e:
            print(f"pleaes try again {e}")


import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("n/Welcome to the guessing game!")
    print("Enter the lower bound and higher bound of your choice.")
    lower_bound = not_number_rejector("Enter a number: ")
    higher_bound = super_asker(lower_bound, float("inf"))
    print(f"ok then, a number between {lower_bound} and {higher_bound}?")

    actualnumber = random.randint(lower_bound, higher_bound)

    guessed = False

    while not guessed:
        guessed_number = not_number_rejector("Guess a number: ")
        print(f"You guessed {guessed_number},")
        if guessed_number == actualnumber:
            print(f"You got it! it was {guessed_number}")
            guessed = True
        elif guessed_number < actualnumber:
            print("too small, try again")
        else:
            print("too big, try again")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
