import sys

online_players = set()
while True:
    input_line = sys.stdin.readline().strip()
    if input_line == "0":
        break
    action, player_id = input_line.split()
    if action == "1":
        online_players.add(player_id)
    elif action == "2":
        print(1 if player_id in online_players else 0)
    elif action == "3":
        online_players.discard(player_id)