import random
import time as t

# Countdown
def count(seconds):
    for i in range(seconds):
        print(str(seconds - i) + "...\n")
        t.sleep(1)


def playOrNot(question):
    answer = input(question)
    if answer == "Yes":
        count(5)
    else:
        exit()


# RockPaperScissors
def play():
    # create a list of play options
    t = {1: "Kéo", 2: "Búa", 3: "Giấy"}

    # assign a random play to the computer
    computer = random.choice(list(t.keys()))

    # set player to False
    player = False

    chooselanguage = int(input("(1) - English\n(2) - Tiếng Việt\n"))
    if chooselanguage == 1:
        while player == False:
            # set player to True
            print("Choose your dicision...")
            player = int(input("(1) - Scissors\n(2) - Rock\n(3) - Paper\n"))
            # int(player)
            count(3)
            if player == computer:
                print("Tie!")
            elif player == 1:
                if computer == 2:
                    print("You lose...", "Rock", "smashed", "Scissors")
                else:
                    print("Chúc mừng bạn đã thắng!", "Scissors", "cut", "Paper")
            elif player == 2:
                if computer == 3:
                    print("You lose...", "Paper", "covers", "Rock")
                else:
                    print("You win!", "Rock", "smashed", "Scissors")
            elif player == 3:
                if computer == 1:
                    print("You lose...", "Scissors", "cut", "Paper")
                else:
                    print("You win!", "Paper", "covers", "Rock")
            else:
                print("Oops, invalid, choose again...")
            # player was set to True, but we want it to be False so the loop continues
            player = False
            computer = random.choice(list(t.keys()))
            playOrNot("Again? Yes/No\n")
    elif chooselanguage == 2:
        while player == False:
            # set player to True
            print("Hãy chọn đi nào...")
            player = int(input("(1) - Kéo\n(2) - Búa\n(3) - Giấy\n"))
            # int(player)
            print("Oẳn tù tì ra cái gì ra cái này...\n")
            count(3)
            if player == computer:
                print("Bất phân thắng bại!")
            elif player == 1:
                if computer == 2:
                    print("Bạn đã thua!", "Búa", "đập cong", "Kéo")
                else:
                    print("Chúc mừng bạn đã thắng!", "Kéo", "cắt được", "Giấy")
            elif player == 2:
                if computer == 3:
                    print("Bạn đã thua!", "Giấy", "bọc được", "Búa")
                else:
                    print("Chúc mừng bạn đã thắng!", "Búa", "đập cong", "Kéo")
            elif player == 3:
                if computer == 1:
                    print("Bạn đã thua!", "Kéo", "cắt được", "Giấy")
                else:
                    print("Chúc mừng bạn đã thắng!", "Giấy", "bọc được", "Búa")
            else:
                print("Nhập sai rồi, nhập lại nha!")
            # player was set to True, but we want it to be False so the loop continues
            player = False
            computer = random.choice(list(t.keys()))
            playOrNot("Chơi lại nhé? Yes/No\n")
    else:
        print("Invalid")


if __name__ == "__main__":
    play()