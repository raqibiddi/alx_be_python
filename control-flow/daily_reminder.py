task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): "))
time_bound = str(input("Is it time-bound? (yes/no): "))

match priority:
    case high:
        if time_bound == "yes":
            print(f"{task}' is a high priority task that requires immediate attention today!" )
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")

"""
match priority:
    case low:
        if time_bound == "no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time." )
        else:
            print(f"{task}' is a high priority task that requires immediate attention today!" )
"""