import datetime
from graph import plot_graph_and_print_stats
from calculate_bytes_and_append_to_db import calculate_bytes_sent_and_received


current_time = datetime.datetime.now().time().strftime("%H:%M:%S")

default_current_time = datetime.datetime.now()
default_stop_time = default_current_time + datetime.timedelta(minutes = 10)
default_time_limit = default_stop_time.time().strftime("%H:%M:%S")
_default_time_limit = default_time_limit.split(':')

hour = int(_default_time_limit[0])
minute = int(_default_time_limit[1])
second = int(_default_time_limit[2])
_set_time = datetime.time(hour, minute, second)
set_time = str(_set_time)

def checker():
    def input_checker(hour, minute, second, set_time):
        set_time_check = False
        if set_time > current_time:
            set_time_check = True
        positive_int_check = False
        if hour >= 0 and minute >= 0 and second >= 0:
            positive_int_check = True
        total_duration_check = False
        if hour < 25 and minute < 61 and second < 61:
            total_duration_check = True

        if set_time_check and positive_int_check and total_duration_check:
            return True
        else:
            return False

    is_input_data_valid = False
    while not is_input_data_valid:
        print('Set the time when you want the network monitoring to stop')
        hour = int(input('Enter the hour - '))
        minute = int(input('Enter the minute - '))
        second = int(input('Enter the second - '))
        _set_time = datetime.time(hour, minute, second)
        set_time = str(_set_time)

        if input_checker(hour, minute, second, set_time):
            global hour, minute, second, set_time
            is_input_data_valid = True
        else:
            print('Make sure you typed everything correctly!')
            choice = input('Type 0 to try again OR 1 to set default timer to 10')
            if choice == 0:
                is_input_data_valid = True
            if choice == 1:
                is_input_data_valid = False


# print('Set the time when you want the network monitoring to stop')
# hour = int(input('Enter the hour - '))
# minute = int(input('Enter the minute - '))
# second = int(input('Enter the second - '))
# _set_time = datetime.time(hour, minute, second)
# set_time = str(_set_time)

print(f'Now monitoring network usage - monitoring will stop at {set_time}')

if __name__ == "__main__":
    checker()
    calculate_bytes_sent_and_received(current_time, set_time)
    plot_graph_and_print_stats(current_time, set_time)
