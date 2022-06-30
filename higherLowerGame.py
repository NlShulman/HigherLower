from glob import glob
from higherLowerGame_art import logo, vs
import higherLowerGame_data
import os
import random
clear = lambda: os.system('cls')
data = higherLowerGame_data.data
score = 0
random_account_a = []
random_account_b = []


def get_random_accout():
    account = random.choice(data)
    return account 
    
def account_data(account, user):
    print(f"Compare {user} : {account['name']}, a {account['description']}, from {account['country']}.")

def get_followers(account):
    return int(account['follower_count'])

def check_guess(user_guess, followers_a, followers_b):
    global score
    if user_guess == "a" :
        if followers_a >= followers_b :
            score += 1 
            return game()
        else:
            print(f"Sorry, that's wrong. Final score {score}")
    elif user_guess == "b" :
        if followers_a <= followers_b :
            score += 1 
            return game()
        else:
            print(f"Sorry, that's wrong. Final score {score}")

def game():
    global random_account_a, random_account_b
    clear()
    print(logo)
    if score >= 1:
        print(f"You are right! Current score: {score}")
        random_account_a = random_account_b

    else:
        random_account_a = get_random_accout()
    account_data(random_account_a, "A")
    print(vs)
    random_account_b = get_random_accout()
    if random_account_b == random_account_a:
        random_account_b = get_random_accout()
    else:
        account_data(random_account_b, "B")

    user_guess = input("Who has more followers? Type A or B ").lower()
    followers_a = get_followers(random_account_a)
    followers_b = get_followers(random_account_b)
    check_guess(user_guess, followers_a, followers_b)

    
game()