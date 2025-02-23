print('Welcome to Higher or Lower!')
print('Who have more instagram followers?')

from data import cricketers
import random


def format_data(player):
    name=player['name']
    followers=player['instagram_followers']
    role=player['role']
    team=player['team']
    return f'{name}, a {role} from {team}.'

def compare(guess,player1_followers,player2_followers):
    if player1_followers>player2_followers:
        return guess=='a'
    else:
        return guess=='b'
    
guess_score=0
game_continue=True

player2=random.choice(cricketers)



while game_continue:
    

    player1=player2
    player2=random.choice(cricketers)

    if player1==player2:
        player2=random.choice(cricketers)


    print(f'Compare A: {format_data(player1)}')
    print('vs')
    print(f'Against B: {format_data(player2)}')

    guess=input('Who has more followers? Type "A" or "B": ').lower()
    print("\n"*5)


    player1_followers=player1['instagram_followers']
    player2_followers=player2['instagram_followers']
    is_correct=compare(guess,player1_followers,player2_followers)

    if is_correct:
        guess_score+=1
        print(f"You're right!, your current score is {guess_score}")
    else:
        print(f"Sorry, that's wrong!, your final score is {guess_score}")
        game_continue=False






    








