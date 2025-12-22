task = input("Enter a task description: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound (yes or no)? ")

message_base = f"Reminder: '{task}' has {priority} priority"
time_message = ''


if time_bound.lower() == 'yes':
    time_message = 'that requires immediate attention today!'
else:
    time_message = '.' 

match priority.lower():
    case 'high':
        final_message = f"{message_base} {time_message}"
    case 'medium':
        final_message = f"{message_base} {time_message}"
    case 'low':
        final_message = f"{message_base} {time_message}"
    case _:
        final_message = "Invalid priority entered."

print(final_message)
