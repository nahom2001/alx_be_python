task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time bound? (yes/no): ")

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder '{task}' is a {priority} task that requires immediate attention today!")
        else:
            print(f"Reminder '{task}' is a {priority} task. Consider completing it when you have free time.")

    case 'medium':
        if time_bound == 'yes':
            print(f"Note: '{task}' is a {priority} task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} task. Consider completing it when you have free time.")
    case 'low':
        if time_bound == 'yes':
            print(f"Note: '{task}' is a {priority} task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} task. Consider completing it when you have free time.")



input("Is it time bound (yes/no)")
correction: /tmp/correction/1008188449509963505603933022569103408866_5/100740/648508/control-flow/daily_reminder.py doesn't contain input\s*\(\s*['\"]Is it time-bound\?\s*\(yes\/no\):\s*['\"]\s*\)
