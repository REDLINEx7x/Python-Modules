players = [
    {
        "name": "alice",
        "score": 2300,
        "achievements": ["first_kill", "level_10"],
        "region": "north",
        "active": True,
    },
    {
        "name": "bob",
        "score": 1800,
        "achievements": ["first_kill"],
        "region": "east",
        "active": True,
    },
    {
        "name": "charlie",
        "score": 2150,
        "achievements": ["boss_slayer", "level_10"],
        "region": "north",
        "active": True,
    },
    {
        "name": "diana",
        "score": 2050,
        "achievements": ["first_kill"],
        "region": "central",
        "active": False,
    },
]
if __name__ == "__main__":

    print("=== Game Analytics Dashboard ===")

    # --- List Comprehensions ---
    print("\n=== List Comprehension Examples ===")
    high_scores = [p["name"] for p in players if p["score"] > 2000]
    doubled_scores = [p["score"] * 2 for p in players]
    active_players = [p["name"] for p in players if p["active"]]

    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {doubled_scores}")
    print(f"Active players: {active_players}\n")

    # --- Dict Comprehensions ---
    print("\n=== Dict Comprehension Examples ===")
    players_d = {p["name"]: p["score"] for p in players if p["active"]}
    all_ranks = [
        "high" if p["score"] > 2100
        else "medium" if p["score"] > 1900
        else "low"
        for p in players
    ]
    score_categories = {cat: all_ranks.count(cat) for cat in all_ranks}
    achievement_counts = {p["name"]: len(p["achievements"]) for p in players}

    print(f"Player scores (Active): {players_d}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}\n")

    # --- Set Comprehensions ---
    print("\n=== Set Comprehension Examples ===")
    unique_players = {p["name"] for p in players}
    unique_achievements = {ach for p in players for ach in p["achievements"]}
    active_regions = {p["region"] for p in players}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}\n")

    # --- Combined Analysis ---
    print("=== Combined Analysis ===")
    total_players = len(players)
    all_achievements_count = len(unique_achievements)
    avg_score = sum([p["score"] for p in players]) / total_players
    top_performer = max(players, key=lambda p: p["score"])

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {all_achievements_count}")
    print(f"Average score: {avg_score:.1f}")
    print(
        f"Top performer: {top_performer['name']} "
        f"({top_performer['score']} points, "
        f"{len(top_performer['achievements'])} achievements)"
    )
