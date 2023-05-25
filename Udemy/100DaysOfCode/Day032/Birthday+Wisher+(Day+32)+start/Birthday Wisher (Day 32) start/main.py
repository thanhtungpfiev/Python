import datetime as dt
import random
import smtplib

# * get current day of the week
now = dt.datetime.now()
current_day_of_the_week = now.weekday()

match current_day_of_the_week:
    case 0:
        current_day_of_the_week_str = "Monday"
    case 1:
        current_day_of_the_week_str = "Tuesday"
    case 2:
        current_day_of_the_week_str = "Wednesday"
    case 3:
        current_day_of_the_week_str = "Thursday"
    case 4:
        current_day_of_the_week_str = "Friday"
    case 5:
        current_day_of_the_week_str = "Saturday"
    case 6:
        current_day_of_the_week_str = "Sunday"
    case _:
        current_day_of_the_week_str = ""

print(current_day_of_the_week_str)

# * Pick a quote
with open("quotes.txt") as file:
    quotes = file.readlines()
    quote = random.choice(quotes).strip()
    print(quote)

# * send an email
my_email = "cuongphong2508@gmail.com"
password = "aatdvndewyaanawc"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="thanhtungpfiev@gmail.com",
                        msg=f"Subject:{current_day_of_the_week_str} Motivation\n\n{quote}")
