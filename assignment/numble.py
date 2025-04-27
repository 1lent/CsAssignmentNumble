import random

wins = 0  # total wins and stuff
losses = 0
money = 1000


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
    return user_number

def get_user_money():
    global money
    print("Your current amount of money is"  , money)
    inputMoney = input("Enter how much money you want to put in: ")
    inputMoney = int(inputMoney)
    money = money - inputMoney

    if money < 0:
        print("Sorry, you are broke, game over man")
        exit()

    return inputMoney

def checking_guess(random_num):
    guesses = 0
    global money
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
            print(f"You win! You guessed in {guesses + 1} guess")
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
        print(f"Your money has risen to {money}")
    else:
        losses += 1
    print("Total losses: ", losses)
    print("Total wins:", wins)
    yn = input("Play again? Y/N: ")
    if yn.lower() == "y":
        main()
    else: exit()

def main():
    game = checking_guess(get_random_number())
    check_wins(game)

main()
#63