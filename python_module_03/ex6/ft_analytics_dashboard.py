players = [
    {
        "name": "alice",
        "score": 2300,
        "achievements": ["first_kill", "level_10"],
        "region": "north",
        "active": True ,
    },
    {
        "name": "bob",
        "score": 1800,
        "achievements": ["first_kill"],
        "region": "east",
        "active": True ,
    },
    {
        "name": "charlie",
        "score": 2150,
        "achievements": ["boss_slayer", "level_10"],
        "region": "north",
        "active": True ,
    },
    {
        "name": "diana",
        "score": 2050,
        "achievements": ["first_kill"],
        "region": "central",
        "active": False ,
    },
]
high_scores = []
doubled_scores = []
active_palyers = []
for player in players:
    score = player['score']
    if(score > 2000):
        high_scores.append(player['name'])
    doubled_scores.append(int(score * 2))
    if player['active'] == True:
        active_palyers.append(player['name'])
print(high_scores)
print(doubled_scores)
print(active_palyers)

all_cats = []
players_d = {}
for player in players:
    name = player['name']
    score = player['score']
    if player['active']:
        players_d.update({name: score})
    if score > 2100:
        all_cats.append("high")
    elif score > 1900:
        all_cats.append("medium")
    else:
        all_cats.append("low")

score_categories = {cat: all_cats.count(cat) for cat in all_cats}
print(players_d)
print(f"Score categories: {score_categories}")
achievement_counts = {player['name']: len(player['achievements']) for player in players}
print(achievement_counts)
print()
unique_palyers = {player["name"] for player in players}
print(unique_palyers)
unique_achievements = {player["achievements"] for player in players}
print(unique_achievements)
