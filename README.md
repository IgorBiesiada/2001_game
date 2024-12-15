# 2001 Game

A simple web-based dice rolling game built with Flask. Compete against the bot, roll the dice, and collect points. May the luckiest win!

---

## Features

- **Dynamic Dice Selection**: Choose two dice for your rolls from a list of available dice types (e.g., D3, D6, D20, etc.).
- **Score Tracking**: The game keeps track of points for both the player and the bot.
- **Special Rules**: Unique multipliers for specific results (e.g., roll a `7` to divide your score by 7, or an `11` to multiply by 11).
- **Responsive UI**: A sleek and user-friendly interface to enhance the game experience.

---

## How It Works

1. Select two dice from the dropdown menus.
2. Submit your choice to roll the dice.
3. View your roll results, the bot's roll results, and updated scores.
4. Repeat to accumulate points and outscore the bot!

---

## Installation and Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/2001-game.git
   cd 2001-game
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## Code Structure

```
.
├── app.py          # Main Flask application logic
├── templates/
│   └── index.html  # Frontend UI template
└── static/         # (Optional) Static files (CSS, JS, Images)
```

---

## Rules

1. **Dice Options**:
   - Choose from dice with different maximum values, e.g., `D6` for 6-sided dice.
2. **Scoring System**:
   - Your total score is updated based on your dice roll.
   - Special results:
     - Roll `7`: Your score is divided by 7.
     - Roll `11`: Your score is multiplied by 11.
3. **Bot**:
   - The bot rolls random dice and updates its score similarly.

---

## Customization

To add more dice types, update the `dice_type_list` dictionary in `app.py`:

```python
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
```

---
## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.