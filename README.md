# Fitness-Health-Management-System
## Video Link: https://youtu.be/Xw2-ODuhelQ
## Calories Count

Our team created a simple Python command-line tool to help users manage their daily health data. The system can calculate Body Mass Index (BMI), Basal Metabolic Rate (BMR), track food calorie intake, calculate exercise calorie burn, and generate a weekly calorie report.

## Features

- **Personal Profile Management**: Records your name, gender, age, height, and weight, and automatically calculates your BMI and BMR.
- **BMI Calculation**: Computes your Body Mass Index based on your height and weight.
- **BMR Calculation**: Computes your Basal Metabolic Rate according to gender, age, height, and weight.
- **Calorie Tracking**: Select food items from a built-in food database, enter the grams consumed, and automatically accumulate total calorie intake.
- **Exercise Burn Calculation**: Select exercises and duration to calculate calories burned.
- **Weekly Report**: Displays calorie intake, calories burned, and net calories for each day of the week.
- **Continuous Input**: Supports adding multiple food items and exercises in one session until the user chooses to stop.
- **Custom Food and Exercise Data**: Allows users to add new food items and exercise types into the system.



## Quick Start

1. **Run the program**:

   ```bash
   python Fitness-Health-Management-System
    
2.  **Usage Method**：<br>
    1.Create a new user account or use the default test account.<br>
    2.Enter the menu and choose the function you need.<br>
    3.Add food calories by selecting a food and entering the grams consumed.<br>
    4.Calculate calories burned by selecting an exercise and duration.<br>
    5.View your BMI, BMR, today’s calories, or weekly report at any time.<br>



## Core Class and Methods

### `user` Class

| Method | Description |
| :--- | :--- |
| `__init__(name, gender, age, weight, height)` | Initializes a user object and calculates BMI and BMR. |
| `get_bmi()` | Prints the user's Body Mass Index (BMI). |
| `get_data()` | Prints the user's basic information. |
| `get_bmr()` | Prints the user's Basal Metabolic Rate (BMR). |
| `get_calories()` | Prints the user's current total calorie intake. |
| `add_calories()` | Starts the interactive food calorie tracking process. |
| `calculate_exercise()` | Starts the interactive exercise calorie burn calculation process. |
| `weekly_report()` | Displays the weekly calorie intake, burn, and net calorie report. |



## Built-in Food Database


The program comes with a built-in database of common foods and their calories (per g)

| Food | Calories (kcal) |
| :--- | :--- |
| apple | 52 |
| egg | 143 |
| beef | 105 |
| chicken breast | 106 |
| milk | 65 |
| broccoli | 34 |
| carrot | 41 |
| tomato | 18 |

 You can easily modify the `food` dictionary in the code to add or update food items and their calorie values.

| Exercise        | 30 min | 60 min | 90 min |
| :-------------- | :----- | :----- | :----- |
| running         | 300    | 600    | 900    |
| swimming        | 250    | 500    | 750    |
| yoga            | 150    | 300    | 450    |
| cycling         | 200    | 400    | 600    |
| weight lifting  | 350    | 700    | 1050   |
| football        | 300    | 600    | 900    |

## Example Code

```
# Create a user instance
me = user(name="Alice", gender="F", age=25, weight=60, height=165)

# View personal information
me.get_data()

# View BMI
me.get_bmi()

# View Basal Metabolic Rate
me.get_bmr()

# Start tracking food calories
me.add_calories()

# Calculate exercise burn
me.calculate_exercise()

# View weekly report
me.weekly_report()



