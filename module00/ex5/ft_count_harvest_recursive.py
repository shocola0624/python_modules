def ft_print_days_recursive(today: int, days: int) -> None:
    print(f"Day {today}")
    if (today < days):
        ft_print_days_recursive(today + 1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    if (days > 0):
        ft_print_days_recursive(1, days)
    print("Harvest time!")
