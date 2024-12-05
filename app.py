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
    dice1 = request.form.get('dice1')
    dice2 = request.form.get('dice2')
    points = request.form.get('points', 0, type=int)
    roll_result = roll_dice(dice1, dice2)
    update_points = count_points(points, dice1, dice2)

    return render_template('index.html', dice_type_list=dice_type_list, points=update_points, roll_result=roll_result)


def roll_dice(dice1, dice2):

    if dice1 not in dice_type_list or dice2 not in dice_type_list:
        return 'Invalid dice type'
    
    
    
    dice1_max = dice_type_list[dice1]
    dice2_max = dice_type_list[dice2]

    result1 = randint(1, dice1_max)
    result2 = randint(2, dice2_max)
    
    return result1 + result2

def count_points(points, dice1, dice2):
    roll = roll_dice(dice1, dice2)
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
