task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f'"{task}" is a high priority task that requires immediate attention today!')
        else:
            print(f'Note: "{task}" is a high priority task. Try to address it soon.')
    case "medium":
        if time_bound == "yes":
            print(f'"{task}" is a medium priority task that requires attention today!')
        else:
            print(f'Note: "{task}" is a medium priority task. Plan to do it when possible.')
    case "low":
        if time_bound == "yes":
            print(f'"{task}" is a low priority task that is time-bound. Try to finish it today.')
        else:
            print(f'Note: "{task}" is a low priority task. Consider completing it when you have free time.')
    case _:
        print("Invalid priority entered.")

