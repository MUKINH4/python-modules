def ft_recursive_harvest(day: int) -> None:
    if (day == 0):
        return
    print(f'Day {day}')
    ft_recursive_harvest(day - 1)


def ft_count_harvest_recursive() -> None:
    days_until_harvest = int(input('Days until harvest: '))
    ft_recursive_harvest(days_until_harvest)
    print('Harvest time!')
