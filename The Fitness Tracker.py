# 5. The Fitness Tracker

# def log_activity():
#     activities = []
#     durations = []
    
#     while True:
#         activity = input("Enter the fitness activity (or 'done' to finish): ")
#         if activity.lower() == 'done':
#             break
#         duration = float(input(f"Enter the duration in minutes for {activity}: "))
#         activities.append(activity)
#         durations.append(duration)
    
#     return activities, durations


# # Task 2

# def calculate_calories_burned(durations):
#     total_calories = sum(duration * 3.5 for duration in durations)
#     return total_calories

# # Task 3

# def summarize_activities(activities, durations):
#     print("\nActivity Summary:")
#     for activity, duration in zip(activities, durations):
#         print(f"{activity}: {duration} minutes")
#     total_calories = calculate_calories_burned(durations)
#     print(f"\nTotal calories burned: {total_calories:.2f}")

# def main():
#     print("Welcome to the Fitness Tracker!")
#     activities, durations = log_activity()
#     summarize_activities(activities, durations)

# if __name__ == "__main__":
#     main()