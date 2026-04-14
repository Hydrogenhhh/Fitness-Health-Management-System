def load_food():
    try:
        with open("food_list.txt", "r", encoding="utf-8") as f:
            food_dict = {}
            for line in f:
                line = line.strip()
                if not line:
                    continue
                name, cal = line.split("=")
                food_dict[name] = int(cal)
            return food_dict
    except:
        return {
            "apple": 52,
            "egg": 143,
            "beef": 105,
            "chicken breast": 106,
            "milk": 65,
            "brocoli": 34,
            "carrot": 41,
            "tomato": 18
        }

def save_food(food_dict):
    with open("food.txt", "w", encoding="utf-8") as f:
        for name, cal in food_dict.items():
            f.write(f"{name}={cal}\n")

food = load_food()

def load_exercise():
    try:
        with open("exercise.txt", "r", encoding="utf-8") as f:
            exercise_dict = {}
            for line in f:
                line = line.strip()
                if line:
                    name, cals = line.split("=")
                    cal_list = [int(c) for c in cals.split(",")]
                    exercise_dict[name] = cal_list
            return exercise_dict
    except:
        return {
            "running": [300, 600, 900],
            "swimming": [250, 500, 750],
            "yoga": [150, 300, 450],
            "cycling": [200, 400, 600],
            "weight lifting": [350, 700, 1050]
        }

def save_exercise(exercise_dict):
    with open("exercise.txt", "w", encoding="utf-8") as f:
        for name, cal_list in exercise_dict.items():
            cal_str = ",".join([str(c) for c in cal_list])
            f.write(f"{name}={cal_str}\n")

exercise = load_exercise()

def heapify(arr, day_arr, n, i, sort_index):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l][sort_index] > arr[largest][sort_index]:
        largest = l

    if r < n and arr[r][sort_index] > arr[largest][sort_index]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        day_arr[i], day_arr[largest] = day_arr[largest], day_arr[i]
        heapify(arr, day_arr, n, largest, sort_index)


def heap_sort(arr, day_arr, sort_index):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, day_arr, n, i, sort_index)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        day_arr[i], day_arr[0] = day_arr[0], day_arr[i]
        heapify(arr, day_arr, i, 0, sort_index)


class user:
    def __init__(self, name, gender, age, weight, height):
        self.name = name
        self.gender = gender.upper()
        self.age = age
        self.w = weight
        self.h = height
        self.bmi = round(self.w / ((self.h / 100) ** 2), 2)
        self.calories = 0

        if self.gender == "M":
            self.bmr = 10 * self.w + 6.25 * self.h - 5 * self.age + 5
        else:
            self.bmr = 10 * self.w + 6.25 * self.h - 5 * self.age - 161

    def get_bmi(self):
        print(f"\nYour BMI: {self.bmi}")

    def get_data(self):
        print(f"\nName: {self.name} \nGender: {self.gender} \nWeight: {self.w}kg \nHeight: {self.h}cm")

    def get_bmr(self):
        print(f"\nYour BMR: {self.bmr} cal/day")

    def get_calories(self):
        print(f"\nToday total calories: {self.calories:.1f}")

    def add_calories(self):
        food_list = list(food.items())
        print("\n==================== Food List ====================")
        for idx, (name, cal) in enumerate(food_list):
            print(f"{idx + 1}. {name}  ——  {cal} cal / 100g")
        print(f"{len(food_list) + 1}. Add new food")

        try:
            choice = int(input("\nPlease enter number: "))
        except ValueError:
            print("Please enter number only!")
            return self.add_calories()

        food_name = ""
        food_cal = 0

        if 1 <= choice <= len(food_list):
            food_name, food_cal = food_list[choice - 1]

        elif choice == len(food_list) + 1:
            print("\n--- Add New Food ---")
            food_name = input("Enter food name: ").strip()
            if food_name in food:
                print("This food already exists!")
                return self.add_calories()

            try:
                food_cal = int(input("Calories per 100g: "))
            except ValueError:
                print("Please enter number!")
                return self.add_calories()

            food[food_name] = food_cal
            save_food(food)
            print(f"Add {food_name} success!")

        else:
            print("Invalid number!")
            return self.add_calories()

        try:
            grams = float(input(f"\nHow many grams of {food_name}? "))
        except ValueError:
            print("Please enter number!")
            return self.add_calories()

        self.calories += grams * food[food_name] / 100

        print(f"\nAdded: {grams * food[food_name] / 100:.1f} cal")
        print(f"Total today: {self.calories:.1f} cal")

        if self.calories < self.bmr:
            print(f"Still need: {self.bmr - self.calories:.1f} cal")
        elif self.calories > self.bmr:
            print(f"Need to burn: {self.calories - self.bmr:.1f} cal")
        else:
            print("Perfect! You matched your BMR!")

        date = int(input("\nPlease enter date(1-7): "))
        weekly_calorie_matrix[date-1][0] +=  grams * food[food_name] / 100
        weekly_calorie_matrix[date - 1][2] += grams * food[food_name] / 100

        again = input("\nAdd more food? (y/n): ").upper()
        if again == "Y":
            self.add_calories()

    def calculate_exercise(self):
        global exercise
        exercise_list = list(exercise.items())

        print("\n==================== Exercise List ====================")
        print(f"{'No.':<4} {'Exercise':<15} {'30min':<8} {'60min':<8} {'90min':<8}")
        print("-" * 50)
        for idx, (name, cal_list) in enumerate(exercise_list):
            print(f"{idx + 1:<4} {name:<15} {cal_list[0]:<8} {cal_list[1]:<8} {cal_list[2]:<8}")
        print(f"{len(exercise_list) + 1:<4}  Add new exercise")

        try:
            choice = int(input("\nPlease enter exercise number: "))
        except ValueError:
            print(" Please enter number only!")
            return self.calculate_exercise()

        exercise_name = ""
        cal_list = []

        if 1 <= choice <= len(exercise_list):
            exercise_name, cal_list = exercise_list[choice - 1]
        elif choice == len(exercise_list) + 1:
            print("\n--- Add New Exercise ---")
            exercise_name = input("Enter exercise name: ").strip()
            if exercise_name in exercise:
                print(" This exercise already exists!")
                return self.calculate_exercise()

            try:
                cal_30 = int(input("Calories burned in 30 mins: "))
                cal_60 = int(input("Calories burned in 60 mins: "))
                cal_90 = int(input("Calories burned in 90 mins: "))
                cal_list = [cal_30, cal_60, cal_90]
            except ValueError:
                print(" Please enter number only!")
                return self.calculate_exercise()

            exercise[exercise_name] = cal_list
            save_exercise(exercise)
            print(f" {exercise_name} added successfully!")
        else:
            print(" Invalid number!")
            return self.calculate_exercise()

        try:
            duration = int(input(f"\nEnter duration for {exercise_name} (30/60/90 mins): "))
            if duration == 30:
                burn = cal_list[0]
            elif duration == 60:
                burn = cal_list[1]
            elif duration == 90:
                burn = cal_list[2]
            else:
                print(" Only 30/60/90 mins are supported!")
                return self.calculate_exercise()
        except ValueError:
            print(" Please enter number only!")
            return self.calculate_exercise()

        self.calories -= burn
        print(f"\nYou burned: {burn} cal")
        print(f"New total calories today: {self.calories:.1f} cal")
        date = int(input("\nPlease enter date(1-7): "))
        weekly_calorie_matrix[date - 1][1] += burn
        weekly_calorie_matrix[date - 1][2] -= burn

        if input("\nAdd more exercise? (y/n): ").upper() == "Y":
            self.calculate_exercise()

    def weekly_report(self):
        weekly_calorie = weekly_calorie_matrix.copy()
        week = week_days.copy()
        ask = int(input("1.sort by day(default)\n"
                        "2.sort by intake\n"
                        "3.sort by burn\n"
                        "4.sort by net\n"))5
        if ask == 2:
            heap_sort(weekly_calorie, week, 0)
        elif ask == 3:
            heap_sort(weekly_calorie, week, 1)
        elif ask == 4:
            heap_sort(weekly_calorie, week, 2)

        print("\n===== Weekly Calorie Report (MATRIX) =====")
        print(f"{'Day':<15} {'Cal Consumed':<15} {'Cal Burned':<15} {'Net Cal':<15}")
        print("-" * 55)
        total_intake = 0
        total_burn = 0
        total_net = 0

        for i, day in enumerate(week):
            intake = weekly_calorie[i][0]
            burn = weekly_calorie[i][1]
            net = weekly_calorie[i][2]
            print(f"{day:<15} {intake:<15.1f} {burn:<15.1f} {net:<15.1f}")
            total_intake += intake
            total_burn += burn
            total_net += net

        print("-" * 55)
        print(f"{'Total':<15} {total_intake:<15.1f} {total_burn:<15.1f} {total_net:<15.1f}")
        print(f"\nAverage daily net calories: {total_net / 7:.1f}")

def create():
    name = input("Enter your name: ")
    gender = input("Enter your gender (M/F): ").upper()
    age = int(input("Enter your age: "))
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (cm): "))
    return user(name, gender, age, weight, height)

def login():
    while True:
        ask = input("\nCreate new account? (y/n): ").upper()
        if ask == "Y":
            return create()
        elif ask == "N":
            return user("test", "M", 20, 65, 170)
        print("Please enter Y or N.")

exercise_matrix = [
    [300, 600, 900],
    [250, 500, 750],
    [150, 300, 450],
    [200, 400, 600],
    [350, 700, 1050]
]

exercise_names = ["running", "swimming", "yoga", "cycling", "weight lifting"]

weekly_calorie_matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def menu(user):
    while True:
        print(f"\n========== Welcome {user.name} ==========")
        print("1. Add calories")
        print("2. My data")
        print("3. Check BMI")
        print("4. Check BMR")
        print("5. Today calories")
        print("6. Weekly report")
        print("7. Calculate Burn")
        print("8. Exit")
        try:
            ask = int(input("Enter choice: "))
        except ValueError:
            print("Enter number 1-6!")
            continue

        if ask == 1:
            user.add_calories()
        elif ask == 2:
            user.get_data()
        elif ask == 3:
            user.get_bmi()
        elif ask == 4:
            user.get_bmr()
        elif ask == 5:
            user.get_calories()
        elif ask == 6:
            user.weekly_report()
        elif ask == 7:
            user.calculate_exercise()

        elif ask == 8:
            print("Bye!")
            break
        else:
            print("Please enter 1-6.")
        input("\nPress Enter to continue...")

def main():
    u = login()
    menu(u)

if __name__ == "__main__":
    main()