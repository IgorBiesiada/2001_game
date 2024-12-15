from flask import Flask, render_template, request
from random import randint, choice


app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html', dice_type_list=dice_type_list)

@app.route('/roll', methods=['POST'])    
def roll():
    dice1 = request.form.get('dice1')
    dice2 = request.form.get('dice2')

    player_points = request.form.get('player_points', 0, type=int)
    bot_points = request.form.get('bot_points', 0, type=int)

    bot_roll_result = bot_roll_dice()
    player_roll_result = player_roll_dice(dice1, dice2)

    update_player_points = count_player_points(player_roll_result, player_points)
    update_bot_points = count_bot_points(bot_roll_result, bot_points)
    
    return render_template('index.html', dice_type_list=dice_type_list,
                           player_points=update_player_points, player_roll_result=player_roll_result, bot_roll_result=bot_roll_result, bot_points= update_bot_points)


def player_roll_dice(dice1, dice2):

    if dice1 not in dice_type_list or dice2 not in dice_type_list:
        return 'Invalid dice type'
    
    dice1_max = dice_type_list[dice1]
    dice2_max = dice_type_list[dice2]

    result1 = randint(1, dice1_max)
    result2 = randint(2, dice2_max)
    
    result_sum = result1 + result2
    return result_sum


def bot_roll_dice():
    random_dice = [choice(list(dice_type_list)) for _ in range(2)]

    random_dice1, random_dice2 = random_dice

    bot_dice_max1 = dice_type_list[random_dice1]
    bot_dice_max2 = dice_type_list[random_dice2]

    bot_result1 = randint(1, bot_dice_max1)
    bot_result2 = randint(1, bot_dice_max2)

    return bot_result1 + bot_result2

def count_player_points(player_roll_result, player_points):

    if isinstance(player_points, str):
        print(player_points)
        return player_points

    if player_roll_result == 7:
        player_points //= 7
    elif player_roll_result == 11:
        player_points *= 11
    else:
        player_points += player_roll_result

    return player_points

def count_bot_points(bot_roll_result, bot_points):
    if isinstance(bot_points, str):
        return bot_points

    if bot_roll_result == 7:
        bot_points //= 7
    elif bot_roll_result == 11:
        bot_points *= 11
    else:
        bot_points += bot_roll_result

    return bot_points

if __name__ == "__main__":
    app.run(debug=True)
