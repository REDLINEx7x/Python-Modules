import sys


def main() -> None:
    """
    Analyzes and displays command-line arguments provided to the script.

    Prints the program name and total argument count if no arguments are given.
    Otherwise, it iterates through and displays each provided argument.
    """
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
    elif len(sys.argv) > 1:
        count = len(sys.argv)
        print(f"Arguments received: {count - 1}")
        i = 1
        while i < count:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {count}")


if __name__ == "__main__":
    main()
