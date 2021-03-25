import matplotlib.pyplot as plt


bytes_sent = []
bytes_received = []


def plot_graph_and_print_stats(current_time, set_time):
    plt.title(label=f'Bandwidth Usage from {current_time} to {set_time}')
    plt.xlabel('Bytes Sent')
    plt.ylabel('Bytes Received')

    print('Monitoring complete!')
    # print(bytes_sent, bytes_received, sep='\n,\n')
    total_sent = int(sum(bytes_sent)/1024/1024)
    total_received = int(sum(bytes_received)/1024/1024)
    print(f'You sent a total of {total_sent} MB')
    print(f'You received a total of {total_received} MB')


    plt.plot(bytes_sent, bytes_received, 'ro')
    plt.show()

