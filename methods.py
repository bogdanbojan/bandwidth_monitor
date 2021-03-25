"""
A small utility program that tracks how much data you have uploaded and downloaded from the internet during the course of
your current online session. See if you can find out what periods of the day you use more and less and generate a report
or graph that shows it.
"""

# TODO: add time for each db insertion in order to see what periods of the day use more data
# TODO: make it plot realtime

import psutil
import time
import datetime

from config import cursor, connection
from graph import bytes_sent, bytes_received

def append_data_to_DB(per_second_bytes_sent, per_second_bytes_received):

    cursor.execute(
        f"INSERT INTO bandwidth (date,bytes_sent,bytes_received,time) VALUES (current_date,{per_second_bytes_sent},{per_second_bytes_received},current_time)")
    connection.commit()

def append_data_to_graph(per_second_bytes_sent, per_second_bytes_received):

    bytes_sent.append(per_second_bytes_sent)
    bytes_received.append(per_second_bytes_received)


def calculate_bytes_sent_and_received(current_time, set_time):
    while current_time < set_time:

        current_time = datetime.datetime.now().time().strftime("%H:%M:%S")

        bytes_sent_before_time_sleep = psutil.net_io_counters().bytes_sent
        bytes_received_before_time_sleep = psutil.net_io_counters().bytes_recv
        time.sleep(1)
        bytes_sent_after_time_sleep = psutil.net_io_counters().bytes_sent
        bytes_received_after_time_sleep = psutil.net_io_counters().bytes_recv

        per_second_bytes_sent = bytes_sent_after_time_sleep - bytes_sent_before_time_sleep
        per_second_bytes_received = bytes_received_after_time_sleep - bytes_received_before_time_sleep

        append_data_to_DB(per_second_bytes_sent, per_second_bytes_received)
        append_data_to_graph(per_second_bytes_sent, per_second_bytes_received)

    cursor.close()
    connection.close()