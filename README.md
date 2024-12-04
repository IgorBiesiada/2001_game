# Dice Rolling Game - 2001

## Game Description

"Dice Rolling Game - 2001" is a turn-based game where you compete against a computer to reach 2001 points first. The game allows you to customize the dice configuration for your rolls, while the computer randomly selects its dice for each turn.

### Game Features:
- Support for rolling multiple dice in a single turn.
- Ability to specify your own dice configurations.
- Automatic random dice selection for the computer.

---

## How to Play?

1. **Start the game**:  
   Run the game script in your terminal.

2. **Enter dice configuration**:  
   At the start of the game, specify the dice you want to use in the format `D<number>` (e.g., `D6,D10`).

3. **Roll the dice**:  
   Press Enter to roll the dice and update your score.

4. **Check results**:  
   After each roll, you will see both your score and the computer's score.

5. **Winning condition**:  
   The first player to reach 2001 points wins.

---

## Rules

1. **Allowed dice types**:  
   The game supports the following dice types:
   - `D3, D4, D6, D8, D10, D12, D20, D100`
   - You can roll one or multiple dice in the format `D<size>` or as a comma-separated list (e.g., `D6,D10`).

2. **Scoring**:  
   - If the sum of your rolls is `7`, your score is divided by `7`.  
   - If the sum of your rolls is `11`, your score is multiplied by `11`.  
   - Otherwise, the sum of your rolls is added to your score.

3. **Computer's dice**:  
   - The computer randomly selects two dice from the available types before each roll.

---

## Requirements

- Python 3.x
- `random` and `re` libraries (built-in with Python)

---

## How to Run?

1. Clone or download the script to your local machine.  
2. Open a terminal in the directory containing the script.  
3. Run the script using the command:  
   ```bash
   python3 game_2001.py
