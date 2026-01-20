#!/usr/bin/env python3

def all_achs(players: list) -> set:
    """Returns all unique achievements."""
    all_achievements = set()
    for player in players:
        all_achievements = all_achievements.union(player)
    return all_achievements


def common_achs(players: list) -> set:
    """Returns achievements shared by all players."""
    players_len = len(players)
    if players_len == 0:
        return set()
    common = players[0]
    for player in players:
        common = player.intersection(common)
    return common


def ultra_rare_achs(players: list[set[str]]) -> set:
    """Returns the ultra-rare achievements."""
    rare = set()
    for i, player1 in enumerate(players):
        for j, player2 in enumerate(players):
            if i != j:
                player1 = player1.difference(player2)
        rare = rare.union(player1)
    return rare


def achievement_tracker() -> None:
    """Prints all achievements and analytics."""
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    players = [alice, bob, charlie]
    all_achievements = all_achs(players)
    common = common_achs(players)
    rare = ultra_rare_achs(players)

    print("=== Achievement Tracker System ===\n"
          "\n"
          f"Player alice achievements: {alice}\n"
          f"Player bob achievements: {bob}\n"
          f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===\n"
          f"All unique achievements: {all_achievements}\n"
          f"Total unique achievements: {len(all_achievements)}\n"
          "\n"
          f"Common to all players: {common}\n"
          f"Rare achievements (1 player): {rare}\n"
          "\n"
          f"Alice vs Bob common: {alice.intersection(bob)}\n"
          f"Alice unique: {alice.difference(bob)}\n"
          f"Bob unique: {bob.difference(alice)}\n")

    # "See who's missing what achievements"
    alice_miss = all_achievements.difference(alice)
    bob_miss = all_achievements.difference(bob)
    charlie_miss = all_achievements.difference(charlie)
    print(f"Alice missing: {alice_miss}\n"
          f"Bob missing: {bob_miss}\n"
          f"Charlie missing: {charlie_miss}")


if __name__ == "__main__":
    achievement_tracker()
