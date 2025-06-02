from datetime import datetime, timedelta

def display_current_datetime():
    current_time = datetime.now()
    formatted_current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_current_time

def calculate_future_date():
    current_time = datetime.now()
    formatted_date = current_time.strftime("%Y-%m-%d")
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    future_date = current_time + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    return formatted_future_date







def main():
    current_time = display_current_datetime()
    print(f"Current date adn time: {current_time}")

    future_date = calculate_future_date()
    print(f"Future date: {future_date}")

    

if __name__ == "__main__":
    main()

