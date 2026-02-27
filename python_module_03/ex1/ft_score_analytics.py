import sys


def main() -> None:
    """
    Processes and analyzes player scores provided via command-line arguments.

    Calculates total, average, high, low, and range of valid integer scores.
    Skips any non-numerical input gracefully.
    """
    print("=== Player Score Analytics ===")
    list_len = len(sys.argv)

    if list_len > 1:
        i = 1
        scores = []
        while i < list_len:
            try:
                scores.append(int(sys.argv[i]))
            except ValueError:
                print(f"Skipping invalid input: {sys.argv[i]}")
            i += 1

        if len(scores) > 0:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")

            average = sum(scores) / len(scores)
            print(f"Average score: {average}")

            high = max(scores)
            low = min(scores)
            print(f"High score: {high}")
            print(f"Low score: {low}")
            print(f"Score range: {high - low}")
        else:
            print("No valid numerical scores were found.")

    else:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
