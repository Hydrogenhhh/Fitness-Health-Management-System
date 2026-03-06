food = {"apple" : 52, "egg" : 143, "beef" : 105, "chicken breast" : 106, "milk" : 65, "brocoli" : 34, "carrot" : 41, "tomato" : 18 }

class user:
    def __init__(self, name, gender, age, weight, height):
        self.name = name
        self.gender = gender #(M/F)
        self.age = age
        self.w = weight
        self.h = height
        self.bmi = round(self.w/((self.h/100) ** 2), 2)
        self.calories = 0
        if self.gender == "M":
            self.bmr = 10 * self.w + 6.25 * self.h - 5 * self.age + 5
        elif self.gender == "F":
            self.bmr = 10 * self.w + 6.25 * self.h - 5 * self.age - 161
    def get_bmi(self):
        print(self.bmi)
    def get_data(self):
        print(f"Name : {self.name} \n Gender : {self.gender} \n Weight : {self.w} \n Height : {self.h}")
    def get_bmr(self):
        print(self.bmr)
    def get_calories(self):
        print(self.calories)
    def add_calories(self):
        food_type = input("Enter your food: ")
        number = int(input("Enter your amount per (g): "))
        self.calories += number * food[food_type] / 100
        if self.calories < self.bmr:
            print(f"you earned {self.calories} calories, you still need {self.bmr - self.calories} calories")
        elif self.calories > self.bmr:
            print(f"you earned {self.calories}, you need burn {self.calories - self.bmr} calories")
        else:
            print(f"you earned {self.calories} calories, you matched your bmr {self.bmr} calories, good job!")
        ans = input("Do you want to choose more food? (y/n): ").upper()
        if ans == "Y":
            return self.add_calories()
        else:
            return




def create():
    name = input("Enter your name: ")
    gender = input("Enter your gender(M/F): ").upper()
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight(kg): "))
    height = float(input("Enter your height(cm): "))
    return user(name, gender, age, weight, height)

def login():
    ask = input("Do you want to create a new data (y/n): ").upper()
    if ask == "Y":
        return create()
    elif ask == "N":
        return test()
    else:
        print("Please enter Y or N")
        return login()

def test():
    return user("fish","M",18,67,167)

def menu(user):
    ask = int(input(f"Welcome {user.name}, what would you like to do? \n"
                    "1.Add calories\n"
                    "2.Data\n"
                    "3.bmi\n"
                    "4.bmr\n"
                    "5.Exit\n"
                    "Enter:"))
    if ask == 1:
        user.add_calories()
    elif ask == 2:
        user.get_data()
    elif ask == 3:
        user.get_bmi()
    elif ask == 4:
        user.get_bmr()
    elif ask == 5:
        return
    else:
        print("Please enter 1-5")
    space = input("(press enter to continue)")
    menu(user)


def main():
    user = login()
    menu(user)

main()
