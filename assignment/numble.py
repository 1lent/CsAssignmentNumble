import random

wins = 0  # total wins and stuff
losses = 0
money = 1000
hints = False

"""Addition for the assignment to add hints, in checking_guess(),
 it will put an input saying do u want hints,
  if so it will call this once it sets hints = True"""


def get_hints(random_num):
    global hints
    if hints:
        print(f"The number {random.choice(random_num[1])} is in the numble")


def get_random_number():
    """Added This to get random numble from the list of numbers in the txt file.
    Stupid me should have coded it to get a random number 10000-99999"""
    numbers = []
    with open("five_digit_numbers.txt") as open_file:
        open_file = open_file.readlines()
    for i in open_file:
        numbers.append(i.strip())
    random_num = random.choice(numbers)
    return random_num



def get_user_number():
    """Gets user number, when called and returns the users input user_number
    if number is !=5 recalls the function which is called recursion so they have to redo
    the input"""

    user_number = input("Enter a 5 digit number to guess the numble: ")
    if len(user_number) != 5:
        print("\ntry again\n5 Digits")
        return get_user_number()
    else:
        return user_number

def get_user_money():
    """
    Added Gambling system i asked carl to playtest my game he said it was alright bit boring so added this
    What it does is you start with 1000 and when this is called you input the money u want to bet and it takes it from your bal
    if you guess the number your money will get doubled but thats in another function

    i used recursion again here to recall the function if the user enters -1 money as that was a bug if they bet negative number
    if they lost they would get the money

    if the money is <0 they would lose and go bankrupt ending the game.
    I made it < instead of <= so if they didnt want to bet anything.
    """
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

    """This new feature will make so if input = y then it will make hints = True,
     and call the function which prints out which number is in the numble"""
    hintsOn = input("\nDo you want hints? y/n: ")
    if hintsOn == "y":
            hints = True
            get_hints(random_num)

    moneyInput = get_user_money() #calls get_user_money which is the gambling function

    while guesses < 6: #guessing system after 6 guesses game over
        colour_positions = []
        user = get_user_number()

        for i in range(len(random_num)):
            if user[i] == random_num[i]:
                colour_positions.append("🟩") #if in correct spot in array it prints this meaning correct spot
            elif user[i] in random_num:
                colour_positions.append("🟧") #if in array not rright spot prints this  but means its in diff spot
            else:
                colour_positions.append("⬜") #not in numble at all
        print(colour_positions)
        if colour_positions == ['🟩','🟩','🟩','🟩','🟩']: #winning if the array is all green with system above you win and money is doubled returning true meaning Win

            print(f"You win! You guessed in {guesses + 1} guess(es)") #guesess goes up so if u win it just doesnt disreguard the guess
            money += moneyInput * 2
            return True  # Win
        guesses += 1
    print(f"You lose! The correct number was {random_num}")
    return False  # return a false sop when u go to check_wins  it says if win which says if true pretty much

def check_wins(win):
    global wins
    global losses #gets updated global variables

    if win: #if win so if checking_guess returned True then does this if statement
        wins += 1
        print(f"Your money has risen to {money}\n") #shows that money has doubled if win
    else: #if guessing_guess returned false then does this else
        losses += 1 #losees count goes up 1
    print("Total losses: ", losses)
    print("Total wins:", wins, "\n")
    yn = input("Play again? Y/N: ") #continuous if y or n, if y play again if n exit program
    if yn.lower() == "y":
        main()
    else: exit()


def main():
    """Main function that makes the game working passing get_random_number as the parameter for the checkingguess function
    then once that returns True or False Check_wins will be called with game as the parameter
    """
    game = checking_guess(get_random_number())
    check_wins(game)

main()