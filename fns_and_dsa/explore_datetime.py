import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Today's date and time: ", current_date)


display_current_datetime()

number_of_days = int(input("Enter the number of days: "))

def calculate_future_date():
    future_date = datetime.date.today() + datetime.timedelta(days=number_of_days)
    return future_date


calculate_future_date()

print(f"Future date: {calculate_future_date()}")

