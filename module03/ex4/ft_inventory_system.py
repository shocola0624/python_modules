#!/usr/bin/env python3

def show_inventory(user: dict, catalog: dict) -> None:
    """Shows user's items."""
    categories = {}
    ctgs = ""
    total_value = 0
    item_count = 0

    for item, n in user.get("items").items():
        item_catalog = catalog.get(item)
        if not item_catalog:
            continue
        item_type = item_catalog.get("type")
        item_value = item_catalog.get("value")
        item_rarity = item_catalog.get("rarity")
        item_count += n
        total_value += item_value * n
        if item_type in categories.keys():
            new = categories.get(item_type) + n
            categories.update({item_type: new})
        else:
            categories.update({item_type: n})
        print(f"{item} ({item_type}, {item_rarity}): "
              f"{n}x @ {item_value} gold each = {item_value*n} gold")

    for item_type, item_num in categories.items():
        if ctgs != "":
            ctgs += ", "
        ctgs += f"{item_type}({item_num})"
    print("\n"
          f"Inventory value: {total_value} gold\n"
          f"Item count: {item_count} items\n"
          f"Categories: {ctgs}\n")


def transaction(user1: str, user2: str, item: str, num: int,
                players: dict, catalog: dict) -> None:
    """Moves the items from user1 to user2."""
    err = False
    if num < 0:
        print("Error: Negative number of items is invalid.")
        return

    # Player
    u1 = players.get(user1)
    u2 = players.get(user2)
    if not u1:
        print(f"Error: {user1} is not on the player list.")
        err = True
    if not u2:
        print(f"Error: {user2} is not on the player list.")
        err = True
    if err:
        print()
        return
    u1_val = u1.get("total_value")
    u1_items = u1.get("item_count")
    u2_val = u2.get("total_value")
    u2_items = u2.get("item_count")

    # Item
    item_data = catalog.get(item)
    if not item_data:
        print(f"Error: {item} is not on the item list.\n")
        return
    i1 = u1.get("items")
    i2 = u2.get("items")
    if not i1.get(item) or i1.get(item) < num:
        print(f"Error: {user1} doesn't have enough items.\n")
        return
    n1 = i1.get(item)
    n2 = i2.get(item)

    # Transaction
    i1.update({item: n1-num})
    if n2:
        i2.update({item: n2+num})
    else:
        i2.update({item: num})
    item_value = item_data.get("value") * num
    u1.update({"total_value": u1_val-item_value})
    u1.update({"item_count": u1_items-num})
    u2.update({"total_value": u2_val+item_value})
    u2.update({"item_count": u2_items+num})
    print("Transaction successful!\n")


def analytics(players: dict, catalog: dict, rarities: dict) -> None:
    """Shows Inventory Analytics."""
    max_value = -1
    max_items = -1
    rarity = 0
    rarest_items = []
    rarest = ""
    for name in players.keys():
        player = players.get(name)
        if player.get("total_value") > max_value:
            max_value = player.get("total_value")
            mvp = name[0].upper()
            if len(name) > 1:
                mvp += name[1:]
        if player.get("item_count") > max_items:
            max_items = player.get("item_count")
            mip = name[0].upper()
            if len(name) > 1:
                mip += name[1:]
        for item_name in player.get("items").keys():
            item = catalog.get(item_name)
            item_rarity = item.get("rarity")
            if rarities.get(item_rarity) == rarity:
                rarest_items.append(item_name)
            if rarities.get(item_rarity) > rarity:
                rarest_items = [item_name]
                rarity = rarities.get(item_rarity)
    if max_value == -1 or max_items == -1:
        print("Error: Invalid value of players.")
        return
    for item in rarest_items:
        if rarest:
            rarest += ", "
        rarest += item
    print(f"Most valueable player: {mvp} ({max_value} gold)\n"
          f"Most items: {mip} ({max_items} items)\n"
          f"Rarest items: {rarest}")


def inventory_system() -> None:
    """Run the player inventory demo.

    Prints each player's inventory with its value.
    Executes a simple transaction and prints updated item counts.
    """
    # Data
    data = {
        "players": {
            "alice": {
                "items": {"sword": 1, "potion": 5, "shield": 1},
                "total_value": 950,
                "item_count": 7
            },
            "bob": {
                "items": {"magic_ring": 1},
                "total_value": 500,
                "item_count": 1
            }
        },
        "catalog": {
            "sword": {"type": "weapon", "value": 500, "rarity": "rare"},
            "potion": {"type": "consumable", "value": 50, "rarity": "common"},
            "shield": {"type": "armor", "value": 200, "rarity": "uncommon"},
            "magic_ring": {"type": "ring", "value": 500, "rarity": "rare"}
        }
    }
    rarities = {"common": 0, "uncommon": 1, "rare": 2, "legendary": 3}
    players = data.get("players")
    catalog = data.get("catalog")
    if not players or not catalog:
        print("Error: data is broken!")
    alice = players.get("alice")
    bob = players.get("bob")

    # Print
    print("=== Player Inventory System ===\n")

    if alice:
        print("=== Alice's Inventory ===")
        show_inventory(alice, catalog)

    if alice and bob:
        print("=== Transaction: Alice gives Bob 2 potions ===")
        item = "potion"
        transaction("alice", "bob", item, 2, players, catalog)
        alice_item = alice.get("items").get(item)
        bob_item = bob.get("items").get(item)

        print("=== Updated Inventories ===\n"
              f"Alice {item}s: {alice_item}\n"
              f"Bob {item}s: {bob_item}\n")

    print("=== Inventory Analytics ===")
    analytics(players, catalog, rarities)


if __name__ == "__main__":
    inventory_system()
