#!/usr/bin/env python3

from typing import Iterator


def create_events(num: int) -> list[dict]:
    """Creates a list of events.

    Creates random events and adds them into a list.

    Args:
        num (int): Number of events

    Returns:
        A list of events.
    """
    events = []
    default = [
        {"id": 1, "player": "alice", "event_type": "kill",
         "data": {"level": 5}},
        {"id": 2, "player": "bob", "event_type": "item_found",
         "data": {"level": 12}},
        {"id": 3, "player": "charlie", "event_type": "level_up",
         "data": {"level": 8}}
    ]
    players = ["alice", "bob", "charlie", "diana", "eve", "frank", "giant"]
    event_types = ["login", "logout", "level_up",
                   "death", "item_found", "kill"]
    i = 1
    while i <= num and i <= 3:
        events.append(default[i-1])
        i += 1
    while i <= num:
        event = {"id": i, "player": players[i % 7],
                 "event_type": event_types[i % 6],
                 "data": {"level": i * 7 % 100}}
        events.append(event)
        i += 1
    return events


def event_login(event: dict) -> str:
    """Builds a login event message.

    Args:
        event (dict): A dictionary containing event information.

    Returns:
        A formatted event log message containing ID, player name, and level.
    """
    id = event.get("id")
    name = event.get("player")
    lvl = event.get("data").get("level")
    return f"Event {id}: Player {name} (level {lvl}) joined in the world"


def event_logout(event: dict) -> str:
    """Builds a logout event message.

    Args:
        event (dict): A dictionary containing event information.

    Returns:
        A formatted event log message containing ID, player name, and level.
    """
    id = event.get("id")
    name = event.get("player")
    lvl = event.get("data").get("level")
    return f"Event {id}: Player {name} (level {lvl}) left the world"


def event_lvl(event: dict) -> str:
    """Builds a level up event message.

    Args:
        event (dict): A dictionary containing event information.

    Returns:
        A formatted event log message containing ID, player name, and level.
    """
    id = event.get("id")
    name = event.get("player")
    lvl = event.get("data").get("level")
    event.get("data").update({"level": lvl + 1})
    return f"Event {id}: Player {name} (level {lvl}) leveled up"


def event_death(event: dict) -> str:
    """Builds a death event message.

    Args:
        event (dict): A dictionary containing event information.

    Returns:
        A formatted event log message containing ID, player name, and level.
    """
    id = event.get("id")
    name = event.get("player")
    lvl = event.get("data").get("level")
    return f"Event {id}: Player {name} (level {lvl}) was dead"


def event_item(event: dict) -> str:
    """Builds an item found event message.

    Args:
        event (dict): A dictionary containing event information.

    Returns:
        A formatted event log message containing ID, player name, and level.
    """
    id = event.get("id")
    name = event.get("player")
    lvl = event.get("data").get("level")
    return f"Event {id}: Player {name} (level {lvl}) found tresure"


def event_kill(event: dict) -> str:
    """Builds a kill event message.

    Args:
        event (dict): A dictionary containing event information.

    Returns:
        A formatted event log message containing ID, player name, and level.
    """
    id = event.get("id")
    name = event.get("player")
    lvl = event.get("data").get("level")
    return f"Event {id}: Player {name} (level {lvl}) killed monster"


def process_events(events: list, analytics: dict) -> Iterator[str]:
    """Processes each event one by one.

    Args:
        events (list): All event log
        analytics (dict): Processed event counter

    Yields:
        An event message.
    """
    events_funcs = {"login": event_login,
                    "logout": event_logout,
                    "level_up": event_lvl,
                    "death": event_death,
                    "item_found": event_item,
                    "kill": event_kill}
    for event in events:
        if "event_type" in event:
            event_type = event["event_type"]
            if event_type in events_funcs:
                msg = events_funcs[event_type](event)
                n = analytics[event_type]
                analytics.update({event_type: n+1})
                yield msg
        else:
            print("Error: An event doesn't have event_type!")


def fib_store(length: int) -> str:
    """Creates fibonacci sequence.

    Args:
        length (int): Length of sequence

    Returns:
        String of fibonacci sequence.
    """
    a, b = 0, 1
    fib = ""
    for i in range(length):
        if not fib == "":
            fib += ", "
        fib += f"{a}"
        a, b = b, a+b
    return fib


def prime_stream() -> Iterator[str]:
    """Creates prime sequence.

    Yields:
        String of prime sequence.
    """
    prev_prime = 1
    yield "2"

    while True:
        is_prime = False
        cur = prev_prime
        while not is_prime:
            cur += 2
            for i in range(2, cur):
                if cur % i == 0:
                    break
                if i**2 > cur:
                    yield f"{cur}"
                    is_prime = True
                    prev_prime = cur
                    break


def data_stream(processes: int) -> None:
    """Demonstrates stream process.

    Args:
        processes (int): Number of events to process
    """
    events = create_events(processes)
    analytics = {"login": 0, "logout": 0, "level_up": 0,
                 "death": 0, "item_found": 0, "kill": 0}
    msgs = process_events(events, analytics)

    print("=== Game Data Stream Provessor ===\n"
          "\n"
          f"Processing {processes} game events...\n")

    for msg in msgs:
        print(msg)
    print()

    print("=== Stream Analytics ===\n"
          f"Total events processed: {processes}\n"
          "Login events:", analytics["login"], "\n"
          "Logout events:", analytics["logout"], "\n"
          "Level up events:", analytics["level_up"], "\n"
          "Death events:", analytics["death"], "\n"
          "Tresure events:", analytics["item_found"], "\n"
          "Kill events:", analytics["kill"], "\n")

    # fibbonacci sequence
    fib = fib_store(10)

    # prime numbers
    n = 5
    prime = prime_stream()
    prime_numbers = ""
    for _ in range(n):
        if not prime_numbers == "":
            prime_numbers += ", "
        prime_numbers += next(prime)

    print("=== Store vs Stream ===\n"
          "Store - Fibonacci sequence (first 10):", fib, "\n"
          f"Stream - Prime numbers (first {n}): {prime_numbers}")


if __name__ == "__main__":
    data_stream(1000)
