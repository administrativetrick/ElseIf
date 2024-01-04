# Eli's Adventure - If-Then Program

def main():
    print("Welcome to Eli's Adventure!")
    print("Let's make some decisions, just like Eli does in his book.")

    while True:
        weather = input("Is it sunny or rainy outside? (Type 'sunny' or 'rainy'): ")

        if weather == 'sunny':
            print("Eli wants to play at the park! Have fun like Eli in the book.")
        elif weather == 'rainy':
            print("Eli needs another plan.")
            print("Eli grabs his umbrella and goes on an adventure!")
            print("Eli sees a beautiful rainbow along the way!")
        else:
            print("Hmm, that's not a valid option. Try again!")

        bedtime = input("Is it bedtime? (Type 'yes' or 'no'): ")

        if bedtime == 'yes':
            print("Goodnight! Eli goes to sleep, ready for new adventures tomorrow.")
        elif bedtime == 'no':
            print("Eli stays up a bit longer, just like in the book.")
        else:
            print("Hmm, that's not a valid option. Try again!")

        play_again = input("Do you want to go on another adventure with Eli? (Type 'yes' or 'no'): ")
        if play_again.lower() != 'yes':
            print("Thanks for joining Eli's Adventure! Goodbye!")
            break

if __name__ == "__main__":
    main()
