import datetime
from graph import plot_graph_and_print_stats
from calculate_bytes_and_append_to_db import calculate_bytes_sent_and_received


current_time = datetime.datetime.now().time().strftime("%H:%M:%S")

print('Set the time when you want the network monitoring to stop')
hour = int(input('Enter the hour - '))
minute = int(input('Enter the minute - '))
second = int(input('Enter the second - '))
_set_time = datetime.time(hour, minute, second)
set_time = str(_set_time)

print(f'Now monitoring network usage - monitoring will stop at {set_time}')

if __name__ == "__main__":
    calculate_bytes_sent_and_received(current_time, set_time)
    plot_graph_and_print_stats(current_time, set_time)
