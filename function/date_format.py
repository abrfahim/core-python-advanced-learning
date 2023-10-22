from  datetime import datetime

current_date = datetime.now()
print(current_date)

#strftime method
print(current_date.strftime("%Y/%m/%d"))
print(current_date.strftime("%H:%M:%S"))
print(current_date.strftime("%Y-%m-%d"))

print(datetime.strftime(current_date,"%Y-%m-%d %H:%M:%S"))

print('----------------------------------------------------------------')

#strptime method
ghost_birthdate = "16, May, 1999"

converting = datetime.strptime(ghost_birthdate,"%d, %B, %Y")
print(converting)