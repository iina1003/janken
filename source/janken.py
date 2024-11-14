
import computer
import player
import janken_judge

def janken_main():
    player_score = 0
    cpu_score = 0
    rounds = 3
    for i in range(rounds):
        player_hand = player.player_pon()  
        cpu_hand = computer.computer_pon() 
        result = janken_judge.judge(player_hand, cpu_hand) 

        if result == "player":
            player_score += 1
        elif result == "cpu":
            cpu_score += 1

    if player_score > cpu_score:
        print("あなたの総合勝利です！")
    elif player_score < cpu_score:
        print("CPUの総合勝利です！")
    else:
        print("引き分けです！")
if __name__ == '__main__':

      janken_main()