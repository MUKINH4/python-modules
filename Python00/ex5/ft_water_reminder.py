def ft_water_reminder() -> None:
    days_last_watering = int(input('Days since last watering: '))
    if days_last_watering > 2:
        print('Water the plants!')
        return
    print('Plants are fine')
