task = input("Enter your task for today: ")


priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()
reminder = f"Reminder: Your task is '{task}'. "

if priority == "high":
    reminder += "This is a HIGH priority task. "
elif priority == "medium":
    reminder += "This is a MEDIUM priority task. "
elif priority == "low":
    reminder += "This is a LOW priority task. "
else:
    reminder += "Priority not recognized. "


if time_bound == "yes":
    reminder += "This task requires immediate attention today!"
else:
    reminder += "You can complete this task at your convenience today."


for i in range(1):
    print("\n" + reminder)

