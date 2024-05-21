import time

def set_timer(total_time, reminder1, reminder2):
    """Users must provide time arguments in HHMMSS format"""
    if validate_user_input(total_time) and validate_user_input(reminder1) and validate_user_input(reminder2):
        time_file = open('time.txt', 'r+', encoding='utf-8')
        time_file.seek(0)
        time_file.truncate()
        time_file.write(str(total_time) + str(reminder1) + str(reminder2))
        time_file.close()
    else:
        raise TypeError("Inappropriate argument types")

def validate_user_input(user_input):
    if user_input.isnumeric() and len(user_input) == 6:
        return True
    else:
        return False

def start_timer():
    with open('controller.txt', 'r+', encoding='utf-8') as controller_file:
        controller_file.seek(0)
        controller_file.truncate()
        controller_file.write("run")

def stop_timer():
    with open('controller.txt', 'r+', encoding='utf-8') as controller_file:
        controller_file.seek(0)
        controller_file.truncate()
        controller_file.write("stop")

def reset_timer():
    """Upon form submission"""
    with open('controller.txt', 'r+', encoding='utf-8') as controller_file:
        controller_file.seek(0)
        controller_file.truncate()
        controller_file.write("reset")
    with open('time.txt', 'r+', encoding='utf-8') as time_file:
        time_file.seek(0)
        time_file.truncate()
        time_file.write("000000000000000000")

# Countdown from 10, pausing the timer for 2 seconds after starting, then continue countdown until time ends.
# Submission reminders at 5 and 3 seconds.
set_timer("000010", "000005", "000003")
start_timer()
time.sleep(2)
stop_timer()
time.sleep(2)
start_timer()
time.sleep(10)
reset_timer()

# Countdown from 5, reset timer at 3 seconds. This would mimic a user submitting a form within 2 seconds.
set_timer("000005", "000000", "000000")
start_timer()
time.sleep(2)
reset_timer()
time.sleep(3)

# Countdown from 8, reminders at 3 and 1 second(s).
set_timer("000008", "000003", "000001")
start_timer()
time.sleep(10)
reset_timer()



