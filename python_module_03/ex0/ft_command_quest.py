import sys


def main() -> None:

    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
