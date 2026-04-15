from collections.abc import Callable  # not needed here but good habit


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(sum(map(lambda m: m["power"], mages)) / len(mages), 2),
    }


if __name__ == "__main__":

    artifacts = [
        {"name": "Light Prism", "power": 74, "type": "accessory"},
        {"name": "Crystal Orb", "power": 84, "type": "focus"},
        {"name": "Lightning Rod", "power": 105, "type": "relic"},
        {"name": "Fire Staff", "power": 92, "type": "fire"},
    ]
    mages = [
        {"name": "Alex", "power": 95, "element": "fire"},
        {"name": "Jordan", "power": 45, "element": "water"},
        {"name": "Riley", "power": 70, "element": "earth"},
    ]
    spells = ["fireball", "heal", "shield", "flash"]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]["name"]} ({sorted_artifacts[0]["power"]} power) comes before {sorted_artifacts[1]["name"]} ({sorted_artifacts[1]["power"]})"
    )

    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(f"{transformed_spells[0]} {transformed_spells[1]} {transformed_spells[2]}")
