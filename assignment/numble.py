import random

wins = 0  # total wins and stuff
losses = 0
money = 1000
hints = False

"""Addition for the assignment to add hints, in checking_guess() it will put an input saying do u want hints, if so it will call this once it sets hints = True"""


def get_hints(random_num):
    global hints
    if hints:
        print(f"The number {random.choice(random_num[1])} is in the numble")


def get_random_number():
    numbers = []
    with open("five_digit_numbers.txt") as open_file:
        open_file = open_file.readlines()
    for i in open_file:
        numbers.append(i.strip())
    random_num = random.choice(numbers)
    return random_num



def get_user_number():
    user_number = input("Enter a 5 digit number to guess the numble: ")
    if len(user_number) != 5:
        print("\ntry again\n5 Digits")
        return get_user_number()
    else:
        return user_number

def get_user_money():
    global money
    print("\nYour current amount of money is"  , money, "\n")
    inputMoney = input("Enter how much money you want to put in: ")
    inputMoney = int(inputMoney)
    if inputMoney < 0:
        print("Negatives dont work pal retry.")
        return get_user_money()
    money = money - inputMoney

    if money < 0:
        print("Sorry, you are broke, game over man")
        exit()

    return inputMoney

def checking_guess(random_num):
    guesses = 0
    global money
    global hints

    """This new feature will make so if input = y then it will make hints = True and call the function which prints out which number is in the numble"""

    hintsOn = input("Do you want hints? y/n: ")
    if hintsOn == "y":
            hints = True
            get_hints(random_num)



    moneyInput = get_user_money()
    while guesses < 6:
        colour_positions = []
        user = get_user_number()

        for i in range(len(random_num)):
            if user[i] == random_num[i]:
                colour_positions.append("🟩")
            elif user[i] in random_num:
                colour_positions.append("🟧")
            else:
                colour_positions.append("⬜")
        print(colour_positions)
        if colour_positions == ['🟩','🟩','🟩','🟩','🟩']:
            print(f"You win! You guessed in {guesses + 1} guess(es)")
            money += moneyInput * 2
            return True  # Win
        guesses += 1
    print(f"You lose! The correct number was {random_num}")
    return False  # return a false sop when u go to check_wins  it says if win which says if true pretty much

def check_wins(win):
    global wins
    global losses
    if win:
        wins += 1
        print(f"Your money has risen to {money}\n")
    else:
        losses += 1
    print("Total losses: ", losses)
    print("Total wins:", wins, "\n")
    yn = input("Play again? Y/N: ")
    if yn.lower() == "y":
        main()
    else: exit()

def main():
    game = checking_guess(get_random_number())
    check_wins(game)

main()