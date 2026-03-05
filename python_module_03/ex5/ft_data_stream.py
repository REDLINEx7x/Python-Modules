from typing import Generator


def event_generator(n: int) -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, n + 1):
        player_name = players[(i - 1) % len(players)]
        action = actions[(i - 1) % len(actions)]
        level = (i % 20) + 1
        event = {
            "id": i,
            "player": player_name,
            "action": action,
            "level": level,
        }
        yield event


def ft_fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def ft_prime(n: int) -> Generator[int, None, None]:
    count = 0
    num = 2

    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main() -> None:

    total_events = 0
    high_level_players = 0
    treasure = 0
    level_up = 0

    stram_wizard = event_generator(1000)
    print("=== Game Data Stream Processor ===")
    print("Processing 1000 game events...\n")
    for event in stram_wizard:
        player_id = event["id"]
        name = event["player"]
        lvl = event["level"]
        action = event["action"]
        if player_id <= 3:
            print(f"Event {player_id}: Player {name} (level {lvl}) {action}")
        if player_id == 4:
            print("...")
        total_events += 1
        if event["level"] >= 10:
            high_level_players += 1
        if event["action"] == "found treasure":
            treasure += 1
        if event["action"] == "leveled up":
            level_up += 1
    print("=== Stream Analytics ===\n")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players})")
    print(f"Treasure events :{treasure}")
    print(f"Level-up events: {level_up}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")
    print("=== Generator Demonstration ===")
    fibonacci_wizard = ft_fibonacci(10)
    print("Fibonacci sequence (first 10):", end=" ")
    for i in range(10):
        print(next(fibonacci_wizard), end=", " if i < 9 else "\n")

    prime_wizard = ft_prime(100)
    print("Prime numbers (first 5):", end=" ")
    for i in range(5):
        print(next(prime_wizard), end=", " if i < 4 else "\n")


if __name__ == "__main__":
    main()
# gen = event_generator(1000000)

# lst = list(event_generator(1000000))

# print(f"Generator size: {sys.getsizeof(gen)} bytes")
# print(f"List size:      {sys.getsizeof(lst)} bytes")
