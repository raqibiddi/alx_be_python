from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()
    print("Today's date and time: ", current_date)


display_current_datetime()

number_of_days = int(input("Enter the number of days: "))

def calculate_future_date():
    future_date = date.today() + timedelta(days=number_of_days)
    return future_date


print(f"Future date: {calculate_future_date()}")

