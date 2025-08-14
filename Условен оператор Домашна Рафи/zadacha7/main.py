windSpeedPerSecond = float(input('Enter speed in m/s:'))
windSpeedPerHour = windSpeedPerSecond * 3.6
if 0 <= windSpeedPerHour < 1:
    print('щил')
elif 1 <= windSpeedPerSecond <= 6:
    print('тих вятър')
elif 7 <= windSpeedPerHour <= 11:
    print('лек бриз')
elif 12 <= windSpeedPerSecond <= 19:
    print('слаб вятър')
elif 20 <= windSpeedPerHour <= 29:
    print('умерен вятър')
elif 30 <= windSpeedPerSecond <= 39:
    print('полусилен вятър')
elif 40 <= windSpeedPerHour <= 50:
    print('силен вятър')
elif 51 <= windSpeedPerSecond <= 62:
    print('доста силен вятър')
elif 63 <= windSpeedPerHour <= 75:
    print('много силен вятър')
elif 76 <= windSpeedPerSecond <= 87:
    print('щорм')
elif 88 <= windSpeedPerHour <= 102:
    print('силен щорм')
elif 103 <= windSpeedPerSecond <= 117:
    print('жесток щорм')
elif 117 <= windSpeedPerHour <= 100000000000000000000000000000000000000000:
    print('ураган')
else:
    print('Невалидна скорост')