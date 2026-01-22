#!/usr/bin/env python3

def preservation_system() -> None:
    """Preservation System.

    Establishes a new storage unit named new_discovery.txt and
    inscribe three critical data entries.
    """
    file_name = "new_discovery.txt"
    print("=== CYBER ARCHIVE - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {file_name}")
    f = open(file_name, "w")
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")
    data = "{[}ENTRY 001{]} New quantum algorithm discovered\n"
    data += "{[}ENTRY 002{]} Efficiency increased by 347%\n"
    data += "{[}ENTRY 003{]} Archived by Data Archivist trainee"
    f.write(data)
    print(data, "\n")

    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")
    f.close()


if __name__ == "__main__":
    preservation_system()
