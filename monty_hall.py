import random

stay_win = 0
switch_win = 0

for i in range(1000):
    doors = ['goat', 'car', 'goat']
    random.shuffle(doors)
    players_choice = doors.pop()
    doors.pop(doors.index('goat'))
    switch = random.randrange(2)

    if not switch:
        if players_choice == 'car':
            stay_win += 1
    elif switch:
        if doors[0] == 'car':
            switch_win += 1

print("In 1000 tries, stay win: {}, switch win: {}".format(stay_win, switch_win))
print('Stay Percentage: {:0.2f}%, Switch Percentage: {:0.2f}%'.format((stay_win / (stay_win + switch_win)) * 100, (switch_win / (stay_win + switch_win)) * 100))
