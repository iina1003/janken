if hand == CPU_hand:
    print("あいこです。")
elif (hand == 1 and CPU_hand == 2) or (hand == 2 and CPU_hand == 3) or (hand == 3 and CPU_hand == 1):
    print("<><><><><><><><>")
    print("あなたの勝ちです！")
    print("<><><><><><><><>")
    player_score += 1
else:
    print("<><><><><><><><>")
    print("あなたの負けです！")
    print("<><><><><><><><>")
    cpu_score += 1