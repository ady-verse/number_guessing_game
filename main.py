import art
print(art.logo)
import random
print("Welcome to the Number Guessing Game!")
print()
print("I'm thinking of a number between 1 and 100.")
c_choice=random.randint(1,100)
def game():
    u_choice=int(input("choose your number"))
    if u_choice<c_choice:
        print("too low")
        return False
    if u_choice>c_choice:
        print("too high")
        return False
    if u_choice==c_choice:
        print("you guessed it right")
        return True


wish=input("how u wud like to play the game hard or easy")
if wish=="hard":
    print("you'll play this game 5 times")
    attempts=5
    for i in range(0,5):
        result=game()
        if result==True:
            break
        else:
            attempts -= 1
            print(f"you have {attempts} attempts left")

if wish=="easy":
    print("you'll play this game 10 times")
    attempts=10
    for i in range(0,10):
        resultt=game()
        if resultt==True:
            break
        else:
            attempts -= 1
            print(f"you have {attempts} attempts left")








