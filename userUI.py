import time
import os


def set_timer(total_time, reminder1 = "000000", reminder2 = "000000"):
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

def pause_timer():
    with open('controller.txt', 'r+', encoding='utf-8') as controller_file:
        controller_file.seek(0)
        controller_file.truncate()
        controller_file.write("stop")

def cancel_timer():
    """Upon form submission"""
    with open('controller.txt', 'r+', encoding='utf-8') as controller_file:
        controller_file.seek(0)
        controller_file.truncate()
        controller_file.write("reset")
    with open('time.txt', 'r+', encoding='utf-8') as time_file:
        time_file.seek(0)
        time_file.truncate()
        time_file.write("000000000000000000")

def watch():
    while True:
        with open('time.txt', 'r+', encoding='utf-8') as time_file:
            alert = time_file.read()
            if alert == "0s":
                print("Time's up")
                break
            if alert == "5s":
                print("5s remaining")
            if alert == "3s":
                print("3s remaining")

# Countdown from 10, pausing the timer for 2 seconds after starting, then continue countdown until time ends.
# Submission reminders at 5 and 3 seconds.
set_timer("000010", "000005", "000003")
start_timer()
watch()
time.sleep(2)
pause_timer()
time.sleep(2)
start_timer()
time.sleep(10)

# Countdown from 5s, reset timer at 3s. This would mimic a user submitting a form within 2s.
set_timer("000005")
start_timer()
time.sleep(2)
cancel_timer()
time.sleep(3)

# Countdown from 4s.
set_timer("000004")
start_timer()




