import random


def random_decision():
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

    print("\nBy choosing randomly between stay and switch")
    print("In {} tries, stay win: {}, switch win: {}".format(i+1, stay_win, switch_win))
    print('Of total wins: Stay Percentage: {:0.2f}%, Switch Percentage: {:0.2f}%'.format((stay_win / (stay_win + switch_win)) * 100, (switch_win / (stay_win + switch_win)) * 100))


def staying():
    stay_win = 0
    for i in range(1000):
        doors = ['goat', 'car', 'goat']
        random.shuffle(doors)
        players_choice = doors.pop()
        doors.pop(doors.index('goat'))

        if players_choice == 'car':
                stay_win += 1

    print("Wins by staying: {}/{} ({:0.2f}% chance of winning)".format(stay_win, i+1, (stay_win/1000)*100))


def switching():
    switch_win = 0
    for i in range(1000):
        doors = ['goat', 'car', 'goat']
        random.shuffle(doors)
        players_choice = doors.pop()
        doors.pop(doors.index('goat'))

        if players_choice != 'car':
                switch_win += 1

    print("Wins by switching: {}/{} ({:0.2f}% chance of winning)".format(switch_win, i+1, (switch_win/1000)*100))


staying()
switching()
random_decision()
