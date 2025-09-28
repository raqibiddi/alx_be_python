from datetime import datetime, timedelta, date

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Today's date and time: ", formatted_date)


display_current_datetime()

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = date.today() + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date


print(f"Future date: {calculate_future_date()}")

