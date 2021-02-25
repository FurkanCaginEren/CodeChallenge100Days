import smtplib
import datetime as dt
import random


my_email = "seignour71@gmail.com"
password = "damla1971*"
    
    
now = dt.datetime.now()
if now.weekday() == 3:
    with open("quotes.txt") as data:
        quotes = data.readlines()
        new_quote = random.choice(quotes)

    # port 587 is works for gmail mail port without if default is 25
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        #transport layer security
        connection.starttls()
        connection.login(user=my_email,password=password)

        connection.sendmail(from_addr=my_email,
                            to_addrs="fcagineren@gmail.com",
                            msg=f"Subject:Motivation Quote\n\n{new_quote}")

############ DATETIME LIB USAGE ################

# now ==> class with attributes in it
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week =now.weekday() #starts from monday=0 gives number day


# date_of_birth = dt.datetime(year=1997,month=6,day=19)










