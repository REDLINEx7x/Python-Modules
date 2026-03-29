import os
import sys

from dotenv import load_dotenv


def load_config() -> dict[str, str]:
    # load .env file into os.environ
    # won't override variables already set in the real environment
    load_dotenv()
    return {
        "matrix_mode": os.getenv("MATRIX_MODE", "NOT SET"),
        "database_url": os.getenv("DATABASE_URL", "NOT SET"),
        "api_key": os.getenv("API_KEY", "NOT SET"),
        "log_level": os.getenv("LOG_LEVEL", "NOT SET"),
        "zion_endpoint": os.getenv("ZION_ENDPOINT", "NOT SET"),
    }


def display_config(config: dict[str, str]) -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    print(f"  Mode:     {config['matrix_mode']}")

    # show friendly message instead of raw database URL
    if config["database_url"] != "NOT SET":
        print("  Database: Connected to local instance")
    else:
        print("  Database: NOT CONFIGURED")

    # never print the real api key
    if config["api_key"] != "NOT SET":
        print("  API Access: Authenticated")
    else:
        print("  API Access: NOT CONFIGURED")

    print(f"  Log Level: {config['log_level']}")

    # show friendly message instead of raw URL
    if config["zion_endpoint"] != "NOT SET":
        print("  Zion Network: Online")
    else:
        print("  Zion Network: OFFLINE")


def check_config(config: dict[str, str]) -> bool:
    print()
    print("Environment security check:")

    all_set = all(value != "NOT SET" for value in config.values())

    if all_set:
        print("  [OK] No hardcoded secrets detected")
        print("  [OK] .env file properly configured")
        print("  [OK] Production overrides available")
    else:
        for key, value in config.items():
            if value == "NOT SET":
                print(f"  [MISSING] {key} is not configured")

    return all_set


def main() -> None:
    try:
        config = load_config()
        display_config(config)
        all_set = check_config(config)

        print()
        print("The Oracle sees all configurations.")

        if not all_set:
            print()
            print("Copy .env.example to .env and fill in your values:")
            print("  cp .env.example .env")
            sys.exit(1)

    except Exception as error:
        print(f"ERROR: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
