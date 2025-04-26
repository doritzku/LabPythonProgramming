import json
import os

class UserProfile:
    def __init__(self, name, age, weight, body_type):
        self.name = name
        self.age = age
        self.weight = weight
        self.body_type = body_type
        self.history = []

    def save_to_file(self):
        data = {
            "name": self.name,
            "age": self.age,
            "weight": self.weight,
            "body_type": self.body_type,
            "history": self.history
        }
        with open(f"{self.name}_profile.json", "w") as f:
            json.dump(data, f)

    @staticmethod
    def load_from_file(name):
        if os.path.exists(f"{name}_profile.json"):
            with open(f"{name}_profile.json", "r") as f:
                data = json.load(f)
                user = UserProfile(data['name'], data['age'], data['weight'], data['body_type'])
                user.history = data['history']
                return user
        else:
            print("No profile found.")
            return None

    def log_workout(self, workout_name):
        self.history.append(workout_name)
        self.save_to_file()

class FitnessAssistant:
    def __init__(self, user):
        self.user = user

    def start(self):
        while True:
            print("\nChoose an option:")
            print("1. Start Workout")
            print("2. Diet Plan")
            print("3. Workout History")
            print("4. Stretching")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.start_workout()
            elif choice == "2":
                self.show_diet_plan()
            elif choice == "3":
                self.show_workout_history()
            elif choice == "4":
                self.stretching()
            elif choice == "5":
                print("Exiting... Stay fit!")
                break
            else:
                print("Invalid option. Please try again.")

    def start_workout(self):
        print("\nLet's start your workout based on your body type!")
        ecto = [
            "Jumping Jacks – 1 minute (Warm-up)",
            "Push-ups – 3 sets of 10 reps",
            "Pull-ups – 3 sets of 6 reps",
            "Dumbbell Rows – 3 sets of 12 reps",
            "Barbell Squats – 3 sets of 10 reps"
        ]
        endo = [
            "Push-ups – 3 sets of 10 reps",
            "Burpees – 3 sets of 15 reps",
            "Mountain Climbers – 3 sets of 30 seconds",
            "Lunges – 3 sets of 12 reps (each leg)",
            "Plank – 3 rounds of 30 seconds"
        ]
        meso = [
            "Jump Rope – 1 minute (Warm-up)",
            "Deadlifts – 3 sets of 8 reps",
            "Bench Press – 3 sets of 10 reps",
            "Overhead Press – 3 sets of 12 reps",
            "Dumbbell Lunges – 3 sets of 10 reps"
        ]

        body_type = self.user.body_type.lower()
        if body_type == "ectomorph":
            self.show_exercises(ecto, "Ectomorph Strength Training")
        elif body_type == "endomorph":
            self.show_exercises(endo, "Endomorph Strength + Fat Loss")
        elif body_type == "mesomorph":
            self.show_exercises(meso, "Mesomorph Balanced Workout")
        else:
            print("Unknown body type.")

    def show_exercises(self, exercises, workout_name):
        print(f"\n--- {workout_name} ---")
        print("Get ready! You'll be guided through each exercise one by one.")
        print("After completing each exercise, type '1' and press Enter to continue.\n")

        for i, exercise in enumerate(exercises, 1):
            print(f"Exercise {i}: {exercise}")
            while True:
                done = input("Enter '1' when you're done: ")
                if done.strip() == '1':
                    break
                else:
                    print("Just type '1' when you're finished with the exercise.")

        self.user.log_workout(workout_name)
        print("\n✅ Workout complete! Great job! Remember to stay hydrated.")

    def show_diet_plan(self):
        print("\n--- Diet Plan ---")
        if self.user.body_type.lower() == "ectomorph":
            print("High-protein, high-carb meals with healthy fats. Eat 5–6 times a day.")
        elif self.user.body_type.lower() == "endomorph":
            print("High-protein, low-carb meals. Focus on whole foods, avoid sugar.")
        elif self.user.body_type.lower() == "mesomorph":
            print("Balanced macros. Include lean protein, moderate carbs and fats.")
        else:
            print("No diet plan available for this body type.")

    def show_workout_history(self):
        print("\n--- Workout History ---")
        if self.user.history:
            for entry in self.user.history:
                print(f"- {entry}")
        else:
            print("No workouts logged yet.")

    def stretching(self):
        print("\n--- Stretching ---")
        print("Choose a body part to stretch: 1. Shoulders 2. Legs 3. Back 4. Chest")
        choice = input("Enter your choice: ")
        stretches = {
            "1": ["Arm Circles", "Cross-Body Shoulder Stretch", "Overhead Triceps Stretch"],
            "2": ["Hamstring Stretch", "Quad Stretch", "Calf Stretch"],
            "3": ["Cat-Cow Stretch", "Child’s Pose", "Seated Spinal Twist"],
            "4": ["Chest Opener", "Wall Chest Stretch", "Doorway Stretch"]
        }

        if choice in stretches:
            print("Perform each stretch and enter '1' when done.\n")
            for stretch in stretches[choice]:
                print(f"Stretch: {stretch}")
                while True:
                    done = input("Enter '1' when you're done: ")
                    if done.strip() == '1':
                        break
                    else:
                        print("Please enter '1' once you finish the stretch.")
            print("✅ Stretching complete!")
        else:
            print("Invalid option.")

def create_profile():
    print("Welcome! Let's create your fitness profile.")
    name = input("Enter your name: ")
    existing = UserProfile.load_from_file(name)
    if existing:
        print("Profile loaded.")
        return existing

    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    body_type = input("Enter your body type (ectomorph / endomorph / mesomorph): ").lower()
    user = UserProfile(name, age, weight, body_type)
    user.save_to_file()
    print("Profile created and saved.")
    return user

# Run the program
user = create_profile()
assistant = FitnessAssistant(user)
assistant.start()
