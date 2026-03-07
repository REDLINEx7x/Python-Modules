if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    try:
        print("Initiating secure vault access...")
        with open("classified_data.txt", "r+") as f:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(f.read())
            print()
            print("SECURE PRESERVATION:")
            f.write("\n[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion\n")
            print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("ERROR: Classified vault not found.")
