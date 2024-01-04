# Provided Libraries
import adjacency_list_graph as alg
from dijkstra import dijkstra as dj
from bellman_ford import bellman_ford as bf
import mst

# Additional Libraries
import pandas as pd
import matplotlib.pyplot as plt


# Open the file
df = pd.read_csv('London Underground data.csv', index_col=False, header=None)

# Add labels to the columns
df.columns = ['Lines', 'Station1', 'Station2', 'Time']

# Convert the table into a dataframe
df = pd.DataFrame(df)


# Find and add all lines in the dataset
lines = list()
for index, row in df.iterrows():
    if list(row)[0].strip() not in lines:
        lines.append(list(row)[0])


# Go through the dataset and separate the rows which have only stations and the rows which contain connections
# And also break all rows into cells
stations = dict()
connections = list()
for index, row in df.iterrows():
    formatted_row = list()
    for column in df.columns:
        cell = row[column]
        if isinstance(cell, str):
            cell = cell.strip()
        if not pd.isna(cell):
            formatted_row.append(cell)
    if len(formatted_row) > 2:
        connections.append([formatted_row[1], formatted_row[2], formatted_row[3], formatted_row[0]])
    else:
        if formatted_row[1] not in stations.keys():
            belongs = [False for i in range(len(lines))]
            for i in range(len(lines)):
                if formatted_row[0] == lines[i]:
                    belongs[i] = True
            stations[formatted_row[1]] = belongs
        else:
            for i in range(len(lines)):
                if formatted_row[0] == lines[i]:
                    stations[formatted_row[1]][i] = True
# After executed the code above, the format of data in the dictionary "stations" will be store like below
# "Bank": [False, True, False, False, True, False, False, True, False, False, False]
# Note: the line above is just an example of the structure. The actual Bank station might have different values


# Create a dictionary where key-value pairs are stored,
# Keys - stations' IDs and values - station names
station_indices = dict()
for index in range(len(stations)):
    station_indices[index] = [list(stations.keys())[index], list(stations.values())[index]]
# After executing the code above, the format of data in the dictionary "stations" will be stored as:
# 0: ["Bank", [False, True, False, False, True, False, False, True, False, False, False]]
# Note: the line above is just an example of the structure. The actual Bank station might have different values


# Replace station names in connections with station IDs
# Because provided libraries do not support a graph where nodes are strings
# values list is created to make the retrival of station names from the dictionary easier
values = list()
for i in range(len(station_indices)):
    values.append(station_indices[i][0])
for j in range(len(connections)):
    connections[j][0] = values.index(connections[j][0])
    connections[j][1] = values.index(connections[j][1])

# Sort the connections based on their weights so that when the graph is being created,
# lines that share the same connection(s) only the fastest connection gets added to the graph.
# E.g. Farringdon to King's Cross St. Pancras has a connection through:
# Circle (4 min), Hammersmith & City (4 min), and Metropolitan (2) lines.
connections.sort(key=lambda x: int(x[2]))
# Create a graph via adjacency_list_graph library.
a = alg.AdjacencyListGraph((len(stations)), False, True)
for i in range(len(connections)):
    if not a.find_edge(connections[i][0], connections[i][1]):
        a.insert_edge(connections[i][0], connections[i][1], weight=connections[i][2])


# The same graph as "a" but all weights are = 1. This is to calculate the minimum number of intermediary stops
b = alg.AdjacencyListGraph((len(stations)), False, True)
for i in range(len(connections)):
    if not b.find_edge(connections[i][0], connections[i][1]):
        b.insert_edge(connections[i][0], connections[i][1], weight=1)


# Answering Questions
# ----------------------------------------------------------------------------------------------------------------------
# Gather the route information
while True:
    start = input('Where are you?: ')
    if start in values:
        break
    else:
        print(f'Sorry, there is no such station named: \'{start}\'. Please try again.')

while True:
    finish = input('Where do you want to get to?: ')
    if finish in values:
        break
    else:
        print(f'Sorry, there is no such station named: \'{finish}\'. Please try again.')

# Convert start and finish stations to their corresponding IDs so that they're compatible with the libraries
start_index = values.index(start)
finish_index = values.index(finish)


# ----------------------------------------------------------------------------------------------------------------------
# Task 1a - Dijkstra
times_to_root, predecessors = dj(a, start_index)

route = list()  # keeps track of stations on the journey
time = times_to_root[finish_index]
print(f'\n\033[1mDijkstra\'s Algorithm\033[0m')
print(f'\u001b[36mQ1\033[0m: It will take {time} min to get from {start} to {finish}.\n')

# Trace the route from finish to start and reverse it at the end
last_station_index = finish_index
route.append(station_indices[finish_index][0])
while True:
    last_station_index = predecessors[last_station_index]
    if last_station_index is None:
        break
    else:
        station_name = station_indices[last_station_index][0]
        route.append(station_name)
route.reverse()

# Print all stations on the route
print(f'\033[1mHere is the detailed list of stations for the journey\033[0m: ')
for i in range(len(route)):
    print(f'{i + 1}. {route[i]}')


# ----------------------------------------------------------------------------------------------------------------------
# Task 1b - Dijkstra
# For all station pairs I and Y, calculate the shortest route in min, and in the # of intermediary stops
all_possible_route_times = list()
all_possible_route_stations = list()
for i in range(alg.AdjacencyListGraph.get_card_V(a)):
    t, pre = dj(a, i)
    for j in t[i:len(t)]:
        all_possible_route_times.append(j)
    for y in pre[i:len(pre)]:
        i_y_route = list()
        if y is None:
            all_possible_route_stations.append(len(i_y_route))
        else:
            last_station_index = y
            while True:
                last_station_index = pre[last_station_index]
                if last_station_index is None:
                    all_possible_route_stations.append(len(i_y_route))
                    break
                else:
                    i_y_route.append(last_station_index)


# Display all the station pairs times
x_bins = list(range(0, int(max(all_possible_route_times))+1))
plt.style.use('fivethirtyeight')
plt.hist(all_possible_route_times, bins=x_bins, edgecolor='black')
plt.title('Question 1(b): Total # of routes in min')
plt.xlabel('Time of a route (in min)')
plt.ylabel('# of such routes')
plt.show()


# ----------------------------------------------------------------------------------------------------------------------
# Task 2a - Dijkstra
times_to_root, predecessors = dj(b, start_index)
route = list()
time_between_stations = list()
time = times_to_root[finish_index]
print(f'\n\033[1mDijkstra\'s Algorithm\033[0m')
print(f'\u001b[36mQ2\033[0m: It will take {time} intermediary stops to get from {start} to {finish}.')

# Trace the route from finish to start and reverse the route
route.append(station_indices[finish_index][0])
last_station_index = finish_index
while True:
    last_station_index = predecessors[last_station_index]
    if last_station_index is None:
        break
    else:
        station_name = station_indices[last_station_index][0]
        route.append(station_name)
route.reverse()

# Print out the route
for i in range(len(route)):
    print(f'{i + 1}. {route[i]}')
print(f'\nPerfect! Now, let\'s try another algorithm.\n')


# ----------------------------------------------------------------------------------------------------------------------
# Task 2b (it was calculated in task 1b)
# Display all the station pairs stops
x_bins = list(range(0, int(max(all_possible_route_stations))+1))
plt.style.use('fivethirtyeight')
plt.hist(all_possible_route_stations, bins=x_bins, edgecolor='black')
plt.title('Question 2(b): Total # of routes stops')
plt.xlabel('Duration of a route (# of intermediary stops)')
plt.ylabel('# of such routes')
plt.show()


# ----------------------------------------------------------------------------------------------------------------------
# Task 3a - Shortest route from start to finish (in times) using Bellman-ford
route = list()
time_between_stations = list()
times_to_root, predecessors, cycle = bf(a, start_index)
time = times_to_root[finish_index]
print(f'\n\033[1mBellman Fords\'s Algorithm\033[0m')
print(f'\u001b[36mQ3\033[0m: It will take {time} min to get from {start} to {finish}.\n')

# Trace the route from finish to start and reverse the route
last_station_index = finish_index
route.append(station_indices[finish_index][0])
while True:
    last_station_index = predecessors[last_station_index]
    if last_station_index is None:
        break
    else:
        station_name = station_indices[last_station_index][0]
        route.append(station_name)
route.reverse()

# Print out the route
print(f'\033[1mHere is the detailed list of stations for the journey\033[0m: ')
for i in range(len(route)):
    print(f'{i + 1}. {route[i]}')


# ----------------------------------------------------------------------------------------------------------------------
# Task 3a - Shortest route from start to finish (# of intermediary stops) using Bellman-ford
start_index = values.index(start)
times_to_root, predecessors, cycle = bf(b, start_index)
route = list()
time_between_stations = list()
time = times_to_root[finish_index]
print(f'\n\033[1mBellman Ford\'s Algorithm\033[0m')
print(f'\u001b[36mQ3\033[0m: It will take {time} intermediary stops to get from {start} to {finish}.')

# Trace the route from finish to start and reverse the route
last_station_index = finish_index
route.append(station_indices[finish_index][0])
while True:
    last_station_index = predecessors[last_station_index]
    if last_station_index is None:
        break
    else:
        station_name = station_indices[last_station_index][0]
        route.append(station_name)
route.reverse()
# Print out the route
for i in range(len(route)):
    print(f'{i + 1}. {route[i]}')
print(f'\nLovely! Enjoy you ride! And... Please, mind the gap!')
print(f'If you see something that doesn\'t look right, speak to a member of staff or text the British Transport Police '
      f'on 61016. We will sort it. See it; Say it; Sorted.\n')


# ----------------------------------------------------------------------------------------------------------------------
# Task 3b - Bellman-Ford
# For all station pairs I and Y, calculate the shortest route in min, and in the # of intermediary stops
all_possible_route_stations = list()
for i in range(alg.AdjacencyListGraph.get_card_V(a)):
    t, pre, cycle = bf(a, i)
    for y in pre[i:len(pre)]:
        i_y_route = list()
        if y is None:
            all_possible_route_stations.append(len(i_y_route))
        else:
            last_station_index = y
            while True:
                last_station_index = pre[last_station_index]
                if last_station_index is None:
                    all_possible_route_stations.append(len(i_y_route))
                    break
                else:
                    i_y_route.append(last_station_index)


# Display all the station pairs stops
x_bins = list(range(0, int(max(all_possible_route_stations))+1))
plt.style.use('fivethirtyeight')
plt.hist(all_possible_route_stations, bins=x_bins, edgecolor='black')
plt.title('Question 3(b): Total # of routes stops')
plt.xlabel('Duration of a route (# of intermediary stops)')
plt.ylabel('# of such routes')
plt.show()


# ----------------------------------------------------------------------------------------------------------------------
# Question 4 - Kruskal and Dijkstra
print(f'\n\033[1mOh, no! Please, wait a moment, something is not right...\033[0m\n')

# Minimum spanning tree is the case where the most number of edges that can be closed simultaneously.
minimum_span_tree = mst.kruskal(a)

# Just showing the closed edges.
print(f'\u001b[36mQ4\033[0m: Oh, no! The government has decided to shut down the following connections: ')
affected_connection = 0
closed_edges_simultaneous = list()
for i in alg.AdjacencyListGraph.get_edge_list(a):
    if i not in alg.AdjacencyListGraph.get_edge_list(minimum_span_tree):
        affected_connection += 1
        first, second = values[i[0]], values[i[1]]
        closed_edge = [first, second]
        closed_edges_simultaneous.append(closed_edge)
        print(f'{affected_connection}. {first} <---> {second}')
print(f'\033[1mTotal # of affected connections: {affected_connection}.\033[0m')
print(f'The list above showcases the minimum spanning tree. In this case, this is the largest number of connection '
      f'that can be closed simultaneously while maintaining access to all stations.\n'
      f'However, more connections can be closed. But they cannot be closed simultaneously'
      f'Please, read the report for more details.\n')


# ----------------------------------------------------------------------------------------------------------------------
# For all station pairs I and Y, calculate the shortest route in min, and in the # of intermediary stops
# This is done after mst and not after a user's input to always get the same result to better compare this with
# tasks 2b and 3b
all_possible_route_stations = list()
for i in range(alg.AdjacencyListGraph.get_card_V(minimum_span_tree)):
    t, pre = dj(minimum_span_tree, i)
    for y in pre[i:len(pre)]:
        i_y_route = list()
        if y is None:
            all_possible_route_stations.append(len(i_y_route))
        else:
            last_station_index = y
            while True:
                last_station_index = pre[last_station_index]
                if last_station_index is None:
                    all_possible_route_stations.append(len(i_y_route))
                    break
                else:
                    i_y_route.append(last_station_index)


# Display all the station pairs stops
x_bins = list(range(0, int(max(all_possible_route_stations))+1))
plt.style.use('fivethirtyeight')
plt.hist(all_possible_route_stations, bins=x_bins, edgecolor='black')
plt.title('Question 4(b): Total # of routes stops')
plt.xlabel('Duration of a route (# of intermediary stops)')
plt.ylabel('# of such routes')
plt.show()


# ----------------------------------------------------------------------------------------------------------------------
# This bit tracks all potential closures that can be implemented. Important: They might not be acceptable for closure
# all at once but rather all independently, one at a time
potential_closure = list()  # all alternative edges that can be closed
for i in range(len(connections)):
    # Check if both stations of the edge have alternative lines (routes) to them. If both do, the edge can be closed.
    # If at least one of them doesn't, it cannot.
    if station_indices[connections[i][0]][1].count(True) > 1 and station_indices[connections[i][1]][1].count(True) > 1:
        potential_closure.append([connections[i][0], connections[i][1]])


# Ask a user for an input. Check if the input is a line or a station. If neither, ask again.
# If it's a station, ask for the second station. Check if the second station exists. Convert them into indexes.
# Check if the edge is in potential_closure. If not, one of the stations would be inaccessible. If it is,
# it can be closed.
# If it is a line, recall all stations on that line. If ALL stations have different line(s) going through them, they
# will be accessible after closure. If not, print the station that would become inaccessible and say that closure is not
# possible

line_values = list()  # the same list as "values" but instead of station names, stores which line pass through the
# station
for i in range(len(station_indices)):
    line_values.append(station_indices[i][1])


while True:
    close = input('Enter an edge (just the first station of the edge) or a line to check if it can be closed: ')
    if close in lines:
        break
    elif close in values:
        close_index = values.index(close)
        break
    else:
        print(f'Sorry, the entered value is not an existing line or station. Please try again.')


if close in lines:
    # By default, a line can be closed (no station on the line). However, even if one station doesn't have alternative
    # paths to it, it cannot be closed.
    may_close_line = False
    line_connections = list()  # recall all connection on that line
    for i in connections:
        if i[3] == close:
            line_connections.append([i[0], i[1]])
    for i in line_connections:
        if [i[0], i[1]] in potential_closure or [i[1], i[0]] in potential_closure:
            may_close_line = True
            print(f'The edge between station {values[i[0]]} and {values[i[1]]} \u001b[32mcan\033[0m be closed')
    if may_close_line:
        print(f'Thus, the line \'\u001b[36m{close}\033[0m\' \u001b[32mcan\033[0m be closed, at least partially.')
    else:
        print(f'Thus, the line \'\u001b[36m{close}\033[0m\' \u001b[31mcannot\033[0m be closed at all.')
elif close in values:
    while True:
        close2 = input('Enter the second station of the edge: ')
        if close2 in values:
            close2_index = values.index(close2)
            if [close_index, close2_index] in potential_closure or [close2_index, close_index] in potential_closure:
                print(f'Yes, this edge \u001b[32mcan\033[0m be closed as both stations would still be accessible.')
            else:
                print('The edge \u001b[31mcannot\033[0m be closed as at least one of the stations would be '
                      'inaccessible or the edge does not exist.')
            break
        else:
            print(f'Sorry, the entered station does not exist. Please try again.')
