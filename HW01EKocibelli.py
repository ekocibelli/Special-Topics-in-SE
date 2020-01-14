from random import choice


def get_computer_choice():
    """ randomly choose and return one of 'rock', 'paper', 'scissors' """
    move = choice(['rock', 'paper', 'scissors'])
    return move


def get_human_choice():
    """Function that gets the human's choice and checks if are the values that are meant to be chosen in the game"""
    human = input("Please choose 'R', 'P', 'S' or 'Q' to quit: ")
    human = human.upper()
    if human not in ['R', 'P', 'S', 'Q']:
        print("Wrong INPUT!")
        human = get_human_choice()
    if human == 'Q':
        print("Thanks for playing!")
        exit()
    return human


appendix = {'R': 'rock', 'P': 'paper', 'S': 'scissors'}

if __name__ == '__main__':
    human_input = get_human_choice()
    while True:
        computer_input = get_computer_choice()
        if computer_input == appendix[human_input]:
            print("TIE: we both chose", appendix[human_input])
        elif computer_input == 'rock' and appendix[human_input] == 'paper':
            print('paper beats rock - You win!')
        elif computer_input == 'rock' and appendix[human_input] == 'scissors':
            print('rock beats scissors -  I win!')
        elif computer_input == 'paper' and appendix[human_input] == 'rock':
            print('paper beats rock - I win!')
        elif computer_input == 'paper' and appendix[human_input] == 'scissors':
            print('scissors beats paper - You win!')
        elif computer_input == 'scissors' and appendix[human_input] == 'rock':
            print('rock beats scissors - You win!')
        else:
            print('scissors beats paper - I win!')

        human_input = get_human_choice()
