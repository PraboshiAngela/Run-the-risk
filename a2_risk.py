"""
CP5639 2020-2 Assignment 2
Run the Risk
Student Name: Kollara Angela
Date started: 09/10/2020

Pseudocode:

MENU = "(P)lay\n(I)nstructions\n(D)isplay Report\n(S)how Statistics\n(Q)uit"
RISK_OPTION_MENU = "C)onservative, A)ggressive, S)illy: "
CONSERVATIVE_WIN_CHANCE = 66
AGGRESSIVE_WIN_CHANCE = 45
SILLY_WIN_CHANCE = 5
CONSERVATIVE_REWARD_PERCENTAGE = 20
AGGRESSIVE_REWARD_PERCENTAGE = 60
SILLY_REWARD_PERCENTAGE = 110
BALANCE_AT_START = 1000

function main()
    play_amount = ""
    account_balance = BALANCE_AT_START
    results = empty list
    display welcome to run the risk!
    display MENU
    get choice
    while choice != Q
        if choice = P
            if account_balance = 0
                display You have nothing left. Time to quit...
            else
                play_amount = get_valid_amount(account_balance)
                round_result = play_turn(play_amount)
                account_balance = account_balance +round_result
                add round_result to results
        else if choice = I
            print_instruction()
        else if choice = D
            if play_amount = ""
                display No risks taken yet. Go on...
            else
                display_report(results)
         else if choice = S
            if play_amount = ""
                display There are no statistics if you don't take any risks.
            else
                show_statistics(results)
        else
            display invalid choice
        display MENU
        get choice
    display_report()
    display Thank you for playing

function get_valid_amount(account_balance)
    get risk_amount
    while risk_amount > account_balance or risk_amount < 0
        display You can't risk a negative amount or more than you have.
        get risk_amount
    return risk_amount

function play_turn(play_amount)
    display RISK_OPTION_MENU
    get risk_option
    while risk_option != "C" and risk_option != "A" and risk_option != "S"
        display Please choose from the available options.
        display RISK_OPTION_MENU
        get risk_option
    decision_number = random selection of a number from 1 to 100
    if risk_option = "C" and decision_number <= CONSERVATIVE_WIN_CHANCE
        reward = play_amount * (CONSERVATIVE_REWARD_PERCENTAGE / 100)
    else if risk_option = "A" and decision_number <= AGGRESSIVE_WIN_CHANCE
        reward = play_amount * (AGGRESSIVE_REWARD_PERCENTAGE / 100)
    else if risk_option = "S" and decision_number <= SILLY_WIN_CHANCE
        reward = play_amount * (SILLY_REWARD_PERCENTAGE / 100)
     else
        reward = play_amount
    if reward = play_amount
        display Oh... You lost reward
        return -reward
    else:
        display Congratulations! You earned reward
        return reward



"""
import random

MENU = "(P)lay\n(I)nstructions\n(D)isplay Report\n(S)how Statistics\n(Q)uit"
RISK_OPTION_MENU = "C)onservative, A)ggressive, S)illy: "
CONSERVATIVE_WIN_CHANCE = 66
AGGRESSIVE_WIN_CHANCE = 45
SILLY_WIN_CHANCE = 5
CONSERVATIVE_REWARD_PERCENTAGE = 20
AGGRESSIVE_REWARD_PERCENTAGE = 60
SILLY_REWARD_PERCENTAGE = 110
BALANCE_AT_START = 1000


def main():
    play_amount = ""
    account_balance = BALANCE_AT_START
    results = []
    print("Welcome to Run the Risk!")
    print(MENU)
    choice = input("Choose: ").upper()
    while choice != "Q":
        if choice == "P":
            if account_balance == 0:
                print("You have nothing left. Time to quit...")
            else:
                play_amount = get_valid_amount(account_balance)
                round_result = play_turn(play_amount)
                account_balance += round_result
                results.append(round_result)
        elif choice == "I":
            print_instructions()
        elif choice == "D":
            if play_amount == "":
                print("No risks taken yet. Go on...")
            else:
                display_report(results)
        elif choice == "S":
            if play_amount == "":
                print("There are no statistics if you don't take any risks.")
            else:
                show_stats(results)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Choose: ").upper()
    print(f"Here is a summary of your {len(results)} turns.")
    display_report(results)
    print("Thank you for playing.")


def get_valid_amount(account_balance):
    """"Get a valid risk amount """
    risk_amount = float(input(f"Amount to risk (up to ${account_balance:.2f}): $"))
    while risk_amount > account_balance or risk_amount < 0:
        print("You can't risk a negative amount or more than you have.")
        risk_amount = float(input(f"Amount to risk (up to ${account_balance:.2f}): $"))
    return risk_amount


def play_turn(play_amount):
    """" Determine whether user earn or lose money"""
    risk_option = input(RISK_OPTION_MENU).upper()
    while risk_option != "C" and risk_option != "A" and risk_option != "S":
        print("Please choose from the available options.")
        risk_option = input(RISK_OPTION_MENU).upper()
    decision_number = random.randint(1, 100)
    # Calculating the result based on selected risk option and random number generated
    if risk_option == "C" and decision_number <= CONSERVATIVE_WIN_CHANCE:
        reward = play_amount * (CONSERVATIVE_REWARD_PERCENTAGE / 100)
    elif risk_option == "A" and decision_number <= AGGRESSIVE_WIN_CHANCE:
        reward = play_amount * (AGGRESSIVE_REWARD_PERCENTAGE / 100)
    elif risk_option == "S" and decision_number <= SILLY_WIN_CHANCE:
        reward = play_amount * (SILLY_REWARD_PERCENTAGE / 100)
    else:
        reward = play_amount
    if reward == play_amount:
        print(f"Oh... You lost ${reward:.2f}")
        return 0 - reward  # returning reward as a negative figure as it was a loss
    else:
        print(f"Congratulations! You earned ${reward:.2f}")
        return reward


def print_instructions():
    """" Print Instructions of the game"""
    print("Run the Risk!")
    print("Each turn, you can risk some of your cash to win rewards.")
    print("Will you be:")
    print(f"- conservative ({CONSERVATIVE_WIN_CHANCE}% chance for a +{CONSERVATIVE_REWARD_PERCENTAGE}% reward),")
    print(f"- aggressive ({AGGRESSIVE_WIN_CHANCE}% chance for a +{AGGRESSIVE_REWARD_PERCENTAGE}% reward),")
    print(f"- silly ({SILLY_WIN_CHANCE}% chance for a +{SILLY_REWARD_PERCENTAGE}% reward)?")
    print("If your risk-taking doesn't pay off, you lose the amount you choose to risk.")


def display_report(results):
    """"Display the results of each play turn"""
    current_balance = BALANCE_AT_START
    print("Risk-Reward Record:")
    print(f"Starting balance: ${BALANCE_AT_START:.2f}")
    for round_result in results:
        current_balance += round_result
        print(f"${round_result:8.2f}  ->   ${current_balance:8.2f}")
    print(f"Current balance:${current_balance:8.2f}")


def show_stats(results):
    """Display statistics of play turns"""
    gain_count = 0
    loss_count = 0
    print(f"Maximum gain: ${max(results):8.2f}")
    print(f"Maximum loss: ${min(results):8.2f}")
    for round_result in results:
        if round_result < 0:
            loss_count += 1
        else:
            gain_count += 1
    gain_percentage = (gain_count / len(results)) * 100  # calculating the percentage of wins
    loss_percentage = (loss_count / len(results)) * 100  # calculating the percentage of losts
    print(f"{gain_percentage:6.1f}% of your turns were gains  ({gain_count}/{len(results)})")
    print(f"{loss_percentage:6.1f}% of your turns were losses ({loss_count}/{len(results)})")
    print("Results in sorted order:")
    for round_result in sorted(results):
        print(f"$ {round_result:8.2f}")


main()
