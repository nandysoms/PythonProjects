from datetime import datetime,date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

name = input('Please enter your name:')
dob = datetime.strptime(input('Please enter your Dob in YYYY-MM-DD format:'), "%Y-%m-%d")
display_msgs = input('Please enter the number of times the message has to be displayed:')
age = calculate_age(dob)
diff = 100 - age
today = date.today()
hundreth_year = int(today.year) + diff
for _ in range(0, int(display_msgs)):
    print("Hi " + name + " in " + str(hundreth_year) + " you will turn 100!!!")
