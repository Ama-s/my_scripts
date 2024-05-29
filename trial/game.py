from random import randint

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except (ValueError):
        pass
    
userRandom = randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            pass
        elif guess > userRandom:
            print("Too large!")
        elif guess < userRandom:
            print("Too small!")
        else:
            print("Just right!")
            break

    except (ValueError):
        pass