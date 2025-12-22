task = input("Enter a task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound (yes or no)? ").lower()

reminder_message = f"Reminder: '{task}' has {priority} priority"
time_sensitive_message = ''

if time_bound == 'yes':
    time_sensitive_message = ' that requires immediate attention today!'

if priority == 'high':
    pass
elif priority == 'medium':
    pass
elif priority == 'low':
    pass
else:
    reminder_message = f"Reminder: '{task}' has an unspecified priority"

full_reminder = reminder_message + time_sensitive_message
print(full_reminder)

