import time

def event_grenator(n):
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, n + 1):
        player_name = players[i % len(players)]
        action = actions[i % len(actions)]
        level = (i % 20) + 1
        event = {
            "id": i,
            "player": player_name,
            "action": action,
            "level": level,
        }
        yield event

gen = event_grenator(10)

print(next(gen))
print(next(gen))
print(next(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
