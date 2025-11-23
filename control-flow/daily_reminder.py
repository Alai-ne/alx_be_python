task = input("Enter your task: ")
priority = input("priority (hight/medium/low): ").lower()
time_bound = input("is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f "'{task}'is a high prioritty "
         if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Make sure to work on it soon."

    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that you should complete today."
        else:
            reminder += " and can be done later."

    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " that still requires attention today."
        else:
            reminder += " and can be done whenever you have time."

    case _:
        reminder = "Invalid priority level entered"
print("\nReminder:", reminder)
