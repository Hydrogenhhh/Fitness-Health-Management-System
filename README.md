# Fitness-Health-Management-System
# Calories Count

Our team creat a simple Python command-line tool to calculate your Basal Metabolic Rate (BMR), Body Mass Index (BMI), and track your daily food intake, helping you manage your calorie goals.



## Features

- **Personal Profile Management**: Records your name, gender, age, height, and weight, and automatically calculates your BMI.
- **BMR Calculation**: Computes your Basal Metabolic Rate, tailored for both men and women.
- **Calorie Tracking**: Select from a built-in food database, enter the grams consumed, and automatically accumulate your total calorie intake.
- **Smart Feedback**: Provides real-time feedback on your calorie intake compared to your BMR, feedback whether your calorie intake needs to be supplemented or reduced.
- **Continuous Input**: Supports adding multiple food items in a single session until you choose to stop.




## Quick Start


1. **Run the program**:
    
        python calories_count.py
    
2.  **Usage Method**：
    1.  Initialize a `user` object with your personal information.
    2.  Call the `add_calories()` method to start tracking your food.
    3.  Follow the prompts to enter the food name and the number of grams you ate.
    4.  The program will display your current calorie intake and ask if you want to add more food.



## Core Class and Methods

### `user` Class

| Method | Description |
| :--- | :--- |
| `__init__(name, gender, age, weight, height)` | Initializes a user object, calculates BMI and BMR. |
| `get_bmi()` | Prints the user's Body Mass Index (BMI). |
| `get_data()` | Prints the user's basic information. |
| `get_bmr()` | Prints the user's Basal Metabolic Rate (BMR). |
| `get_calories()` | Prints the total accumulated calorie intake. |
| `add_calories()` | Starts the interactive food calorie tracking process. |



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
