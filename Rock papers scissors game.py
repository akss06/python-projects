import random
import time

options = ['rock', 'paper', 'scissors']
best_out_of = int(input("Best out of: "))
# assuming best out of three
user_points = 0
ai_points = 0

while user_points + ai_points < best_out_of :
    user = input("Choose your action: ").lower()
    ai = random.choice(options)
    time.sleep(0.5)
    print("Ai chooses:", ai)

    if user not in options:
        print("Invalid option \n Pick again.")

    elif user == 'rock' and ai == 'rock' or user == 'paper' and ai == 'paper' or user == 'scissors' and ai == 'scissors':
        print('Pick Again')

    elif user == 'rock' and ai == 'scissors':
        user_points += 1
        print('You win:', user_points, 'points')

    elif user == 'scissors' and ai == 'rock':
        ai_points += 1
        print('Ai win:', ai_points, 'points')

    elif user == 'scissors' and ai == 'paper':
        user_points += 1
        print('You win:', user_points, 'points')


    elif user == 'paper' and ai == 'scissors':
        ai_points += 1
        print('Ai win:', ai_points, 'points')


    elif user == 'paper' and ai == 'rock':
        user_points += 1
        print('You win:', user_points, 'points')


    elif user == 'rock' and ai == 'paper':
        ai_points += 1
        print('Ai win:', ai_points, 'points')
    print()
print()

if user_points > ai_points:
    print("Final points")
    print("User:", user_points)
    print("Ai:", ai_points)

    print("You win")

else:
    print("Final points")
    print("User:", user_points)
    print("Ai:", ai_points)
    print("Ai wins")
