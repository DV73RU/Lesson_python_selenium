import datetime 

# current_date_time = datetime.datetime.now()
# current_time = current_date_time.date()
# print(current_time)

# days_input = int(input("Ввдите количество дней: "))

# past_date = datetime.datetime.today() + datetime.timedelta(days=10)
# print(past_date)

# current_date = datetime.datetime.now()
# current_date_string = current_date.strftime('%m/%d/%y')
# print(current_date_string)

current_date = datetime.datetime.today()
delta_data = datetime.timedelta(days=10)

past_date = current_date + delta_data
print(past_date.strftime('%m/%d/%y'))

new_date = driver_g.find_element(
    By.XPATH, "//input[@id='datePickerMonthYearInput']")

# print(new_date)
new_date.send_keys(Keys.BACKSPACE*10)
print("Дада стёрта")
time.sleep(2)

new_date.send_keys(past_date.strftime('%m/%d/%y'))
print("Введена новая дата")
time.sleep(2)
new_date.send_keys(Keys.RETURN)