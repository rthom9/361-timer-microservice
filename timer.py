import time

while True:
    time_file = open('time.txt', 'r+', encoding='utf-8')
    time_data = time_file.read()
    time_file.seek(0)
    time_file.truncate()
    time_file.write("000000000000000000")
    time_file.close()

    def time_converter(time_string):
        hours_int = int(time_string[0:2])
        minutes_int = int(time_string[2:4])
        seconds_int = int(time_string[4:6])
        total_seconds = (hours_int * 3600) + (minutes_int * 60) + seconds_int
        return total_seconds


    countdown_start = time_converter(time_data[0:6])
    reminder_1 = time_converter(time_data[6:12])
    reminder_2 = time_converter(time_data[12:18])

    def timer_countdown(countdown_time, reminder_1, reminder_2):
        while countdown_time:
            with open('controller.txt', 'r+', encoding='utf-8') as controller_file:
                controller_command = controller_file.read()

            if controller_command == "run":
                print(countdown_time)
                time.sleep(1)
                countdown_time -= 1

                if countdown_time == reminder_1:
                    print("You have " + str(reminder_1) + " seconds left.")
                if countdown_time == reminder_2:
                    print("You have " + str(reminder_2) + " seconds left.")
                if countdown_time == 0:
                    print("Time is up!")
                    # change controller.txt to stop
                    with open('controller.txt', 'r+', encoding='utf-8') as controller_file:
                        controller_file.seek(0)
                        controller_file.truncate()
                        controller_file.write("stop")
                    with open('time.txt', 'r+', encoding='utf-8') as time_file:
                        time_file.seek(0)
                        time_file.truncate()
                        time_file.write("000000000000000000")
            if controller_command == "reset":
                # on a reset it needs to get fully out o
                return
                # break
                    # exit()

    # Convert all to seconds
    timer_countdown(countdown_start, reminder_1, reminder_2)








