print('Enter temperature of the water:')
temperatureOfCleanWater=float(input())
if temperatureOfCleanWater <= 0:
    print('твърдо')
elif temperatureOfCleanWater >= 100:
    print('газообразно')
else:
    print('течно')
