import datetime

# current date time
current_date_time = datetime.datetime.now()
print(current_date_time)

# create date objects
prev_x = datetime.datetime(2024, 12, 16)
print(prev_x)
print('='*20)

print(current_date_time.strftime('%Y')) # year full form
print(current_date_time.strftime('%y')) # year short form
print('='*20)
print(current_date_time.strftime('%B')) # month full name
print(current_date_time.strftime('%b')) # month short name
print(current_date_time.strftime('%m')) # month number
print('='*20)
print(current_date_time.strftime('%A')) # day full name
print(current_date_time.strftime('%a')) # day short name
print(current_date_time.strftime('%d')) # day number
print(current_date_time.strftime('%w')) # weekday number (0-6)
print(current_date_time.strftime('%W')) # weekday number (0-53)
print('='*20)
print(current_date_time.strftime('%H')) # 0-23 hour format
print(current_date_time.strftime('%I')) # 0-12 hour format
print(current_date_time.strftime('%p')) # am/pm show
print('='*20)
print(current_date_time.strftime('%M')) # Minute
print(current_date_time.strftime('%S')) # Seconds
print(current_date_time.strftime('%f')) # micro seconds
print('='*20)
print(current_date_time.strftime('%z')) # UTC offset
print(current_date_time.strftime('%Z')) # UTC zone
print('='*20)
print(current_date_time.strftime('%x')) # local date format
print(current_date_time.strftime('%X')) # local time format
print(current_date_time.strftime('%c')) # local date time format 
print(current_date_time.strftime('%C')) # Century