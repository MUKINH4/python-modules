def ft_count_harvest_iterative() -> None:
    days_until_harvest = int(input('Days until harvest: '))
    for day in range(days_until_harvest, 0, -1):
        print(f'Day {day}')
    print('Harvest time!')
