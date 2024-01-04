Hello! This is my term 1 coursework project for the Algorithms and Data Structures modules. 

In essence, given libraries with prebuilt algorithms (such as Dijkstra or Bellman-Ford algorithms) develop a navigation system for the London Underground Network. The assignment also provides a spreadsheet with all of the stations, the connections in-between them, and the travel time. First, it lists just the stations on a given line. After that, it shows the connections between the two stations and their travel time. (i.e., "Bakerloo, Harrow & Wealdstone, Kenton,	2" means that it would take 2 min on Bakerloo line to get from Harrow & Wealdstone to Kenton and vice versa).

The coursework is: to download all of the libraries, load and access the spreadsheets, and build a network simulating the London Underground. Afterwards, the coursework has 4 subtasks:

1. Gather the route information from the user (starting station and destination) and utilising provided libraries, calculate the fastest route from starting station to the destination.
For this task, I used Dijkstra's algorithm. However, the given libraries were not compatible with string inputs. Therefore, I had to convert all stations into numbers by assigning them IDs. (for example, Harrow & Wealdstone is  
0, Kenton is 1, etc.). However, this enabled me to better understand Dijkstra's algorithm. We also had to produce a histogram showcasing time for all possible station pairs (i.e. all possible routes on the network).
2. For task 2, we had to find the shortest path from the starting station to the destination by counting the number of intermediary stops. In other words, the fewer stations between the starting station and the destination, the  
better. For this task, I also used Dijkstra's algorithm but first had to set all connections to be equal to 1. Thus, the algorithm would calculate the number of intermediary stops. We had to produce another histogram for all station pairs, but now counting the number of intermediary stops for each possible journey on the network.
3. The same as task 2 but the requirement is to use a different algorithm. I chose Bellman-Ford's algorithm for this problem.
4. Create a program that would decide if a connection could be closed. For example, a user enters a line name (i.e. Central) and the program should display all of the connections on that line that can be closed while still maintaining access to all stations. Because I used a dictionary for the Network, I just had to retrieve all stations on that line and check if these stations had any other lines going through them. If other lines do, the station would still be accessible. If not, that connection cannot be closed, and therefore, will not be displayed.

For more information about the coursework specifications, please, check Coursework_2023-2024_v2.pdf file.

All of my code was written in Main.py

Thank you for your time!
