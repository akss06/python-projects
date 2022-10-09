import random

num = random.randint(0,101)

count = 0

print("You get only 5 try")


trys = 5


while count < trys:
    count += 1
    
    guess = int(input("Your guess: "))
    
    
    if guess == num:
        print(f"You did it in {count} try.")
        break
    
    elif guess < num:
        print("Guess higher")
        

    elif guess > num:
        print("Guess lower")
        

    
if count >= trys:
    print("The number is",num)
    print("Better luck next time")
