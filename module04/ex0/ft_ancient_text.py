#!/usr/bin/env python3

def data_format(data: str) -> str:
    """Encloses '[' and ']' with {}.

    Args:
        data (str): Text data to format

    Returns:
        Formatted text data.
    """
    s = ""
    for i in data:
        if i == "[" or i == "]":
            s += "{" + i + "}"
        else:
            s += i
    return s


def data_recovery_system() -> None:
    """Data Recovery System.

    Accesses the storage unit containing ancient_fragment.txt,
    extract all preserved data, and display the recovery process.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        file = open("ancient_fragment.txt", "r")
    except FileNotFoundError:
        print("Error: Storage vault not found. Run data generator first.")
        return None
    print("Connection established...\n")
    data = file.read()
    print("RECOVERED DATA:")
    print(data_format(data), "\n")
    print("Data recovery complete. Storage unit disconnected.")
    file.close()


if __name__ == "__main__":
    data_recovery_system()
