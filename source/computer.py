import random
def computer_pon():
    CPU_hand = random.randint(1, 3)
    if CPU_hand == 1:
        print('CPUの手: グー')
    elif CPU_hand == 2:
        print('CPUの手: チョキ')
    else:
        print('CPUの手: パー')
