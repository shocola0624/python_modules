#!/usr/bin/env python3

def data_format(data: str) -> str:
    """Encloses '[' and ']' with {}.

    Args:
        data (str): Text data to format

    Returns:
        Formatted test data.
    """
    s = ""
    for i in data:
        if i == "[" or i == "]":
            s += "{" + i + "}"
        else:
            s += i
    return s


def vault_sequrity_system() -> None:
    """Vault Security System.

    Implements secure file operations using the 'with statement'
    for both reading classified data and preserving new information
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    vault_path = "classified_data.txt"
    new_vault_path = "security_protocols.txt"
    print("Vault connection established with failsafe protocols\n")

    # Extraction
    with open(vault_path, "r") as f:
        print("SECURE EXTRACTION:")
        data = f.read()
        print(data_format(data), "\n")

    # Preservation
    with open(new_vault_path, "w") as f:
        print("SECURE PRESERVATION:")
        discovery = "[CLASSIFIED] New security protocols archived"
        f.write(discovery)
        print(data_format(discovery))
        print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    vault_sequrity_system()
