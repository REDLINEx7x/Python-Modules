

def verifying_access(file_name: str):

    try:
        with open(file_name, "r+") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered- ``{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as error:
        print(f"RESPONSE: Unexpected system anomaly: {error}")
        print("STATUS: Emergency protocols initiated")


if __name__ == "__main__":

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    verifying_access("lost_archive.txt")
    print()
    print("CRISIS ALERT: Attempting access to 'classified_data.txt'...")
    verifying_access("classified_vault.txt")
    print()
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    verifying_access("standard_archive.txt")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")
