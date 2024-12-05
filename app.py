from flask import Flask, render_template, request
from random import randint, choice
import re

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
    dice_code = request.form.get('dice_code')
    points = request.form.get('points', 0, type=int)
    roll_result = roll_dice(dice_code)
    update_points = count_points(points, dice_code)

    return render_template('index.html', dice_type_list=dice_type_list, points=update_points, roll_result=roll_result)


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

if __name__ == "__main__":
    app.run(debug=True)
