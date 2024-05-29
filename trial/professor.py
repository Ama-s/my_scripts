import random


def main():
    count = 0
    score = 0
    level = get_level()
    while count < 10:
        f_number = generate_integer(level)
        s_number = generate_integer(level)
        sum = f_number + s_number

        print(str(f_number) + " + " + str(s_number) + " = ", end = "")
        answer = int(input())
        score += 1

        attempts = 0
        while answer != sum:
            print(str(f_number) + " + " + str(s_number) + " = ", end = "")
            answer = int(input())
            attempts += 1
            if attempts == 2:
                print("EEE")
                print(str(f_number) + " + " + str(s_number) + " = " + str(sum))
                score -= 1
                break
        count += 1
    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except (ValueError):
            pass
    return level
def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
    elif level == 2:
        number = random.randint(10, 99)
    else:
        number = random.randint(100, 999)
    return number

if __name__ == "__main__":
    main()
