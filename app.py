from random import randint
import re
def roll_dice(dice_code):

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

    pattern = r'^(\d*)D(\d+)([+-]\d+)?$'
    match = re.match(pattern, dice_code)

    if not match:
        return 'Invalid dice code'


    roll = int(match.group(1)) if match.group(1) else 1
    dice_type = f'D{match.group(2)}'
    mod = int(match.group(3)) if match.group(3) else 0

    if dice_type not in dice_type_list:
        return 'Invalid dice type'

    dice_max = dice_type_list[dice_type]
    result = [randint(1, dice_max) for _ in range(roll)]
    total = sum(result) + mod

    return total

def count_points(points):
    roll = roll_dice('2D6')
    if roll == 7:
        points //= 7
    elif roll == 11:
        points *= 11
    else:
        points += roll
    return points

def game_2001():
    player_points = 0
    computer_points = 0

    input('press Enter to roll a dice')
    player_points += roll_dice('2D6')
    computer_points += roll_dice('2D6')

    while player_points < 2001 or computer_points < 2001:
        print(f'punkty gracza {player_points}, punkty komputera {computer_points}')
        player_points = count_points(player_points)
        computer_points = count_points(computer_points)
        input('press Enter to roll a dice')

        if player_points > 2001:
            return 'Brawo wygrałes'
        elif computer_points > 2001:
            return "komputer wygrał"
        else:
            continue

print(game_2001())