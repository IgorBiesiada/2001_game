from random import randint, choice
import re

dice_type_list = {
        'D3': 3,
        'D4': 4,
        'D6': 6,
        'D8': 8,
        'D10': 10,
        'D12': 12,
        'D20': 20,
        'D100': 100
    }

def roll_dice(dice_code):

    pattern = r'^(D\d+)(,D\d+)*$'
    match = re.match(pattern, dice_code)

    if not match:
        return 'Invalid dice code'

    dice_list = dice_code.split(',')
    result = []

    for dice in dice_list:
        if dice not in dice_type_list:
            return 'Invalid dice code'

        dice_max = dice_type_list[dice]
        result.append(randint(1, dice_max))

    total = sum(result)
    return total

def count_points(points, dice_code):
    roll = roll_dice(dice_code)
    if isinstance(roll, str):
        print(roll)
        return points

    if roll == 7:
        points //= 7
    elif roll == 11:
        points *= 11
    else:
        points += roll
    return points

def get_random_dice():
    random_dice = [choice(list(dice_type_list)) for _ in range(2)]
    return ','.join(random_dice)

def game_2001():
    player_points = 0
    computer_points = 0

    dice_code = input('Enter a dice')


    while True:
        input('press enter to roll')
        player_points = count_points(player_points, dice_code)
        print(f'Your points is {player_points}')
        computer_points = count_points(computer_points, get_random_dice())
        print(f'Computer points is {computer_points}')

        dice_code = input('Enter a dice')

        if player_points >= 2001:
            return 'You won'
        elif computer_points >= 2001:
            return "bot won"
        else:
            continue

print(game_2001())
