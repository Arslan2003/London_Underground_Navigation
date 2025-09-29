# London Underground Navigation

A Python-based navigation tool for the London Underground. This project allows users to find the shortest routes between stations, analyse route distributions, and simulate line or edge closures while maintaining network accessibility.

<br>

## 📖 Overview

This project is a standalone Python application for modelling and analysing the London Underground Network. Users can:
- Find shortest paths between stations (by travel time or number of stops).
- Visualise distributions of travel times and route lengths.
- Simulate closures of lines or station connections while ensuring network connectivity.

The project uses custom libraries that are built with the guidelines from the book [Introduction to Algorithms](https://www.cs.mcgill.ca/~akroit/math/compsci/Cormen%20Introduction%20to%20Algorithms.pdf) by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.

<br>

## 📂 Structure

```Main.py``` is the main file which executed the algorithms to solve the given tasks:
1. Implement a route planner that finds the shortest journey time (in minutes) between two stations.
2. Modify the planner to compute the shortest route based on the number of stops instead of time.
3. Re-implement Task 2 using a different pathfinding algorithm/library.
4. Identify which station-to-station connections can be closed while keeping the network fully connected.
All other ```.py``` files implement the libraries from the book, [Introduction to Algorithms](https://www.cs.mcgill.ca/~akroit/math/compsci/Cormen%20Introduction%20to%20Algorithms.pdf).
The ```London Underground data.csv``` file provide the station, station-pairs, durations, and lines in a csv format. 



<br>

## 📊 Findings

<img width="100%" alt="Frequency of Routes by their Lenth in min" title="Frequency of Routes by their Lenth in min" src="https://github.com/user-attachments/assets/4db49f3d-cd86-4e2b-9e38-3770d2dcbc7f"/>

***Figure 1**. Most routes take between 15 to 45 minutes to complete.*

<br>

<img width="100%" alt="Frequency of Routes by their Lenth in # of Intermediary Stops" title="Frequency of Routes by their Lenth in # of Intermediary Stops" src="https://github.com/user-attachments/assets/036b4335-9c31-41d1-8fe1-d679aae6b119" />

***Figure 2**. Most station pairs are 6 to 17 stations apart from each other.*

<br>

<img width="100%" alt="Frequency of Routes by their Lenth in # of Intermediary Stops" title="Frequency of Routes by their Lenth in # of Intermediary Stops" src="https://github.com/user-attachments/assets/545c3c3b-c6e3-4b55-8077-0b863b2b515b"/>

***Figure 3**. This figure confirms findings form Figure 2.*

<br>

<img width="100%" alt="Frequency of Routes by their Lenth in # of Intermediary Stops" title="Frequency of Routes by their Lenth in # of Intermediary Stops" src="https://github.com/user-attachments/assets/97262b95-610f-43a1-a27d-d0b5e6b3e1ac"/>

***Figure 4**. With the minimum spanning tree, most station-pairs are, now, 10 to 30 stations apart from each other - a ~70% increase.*

<br>


## ⚙️ Installation

1. Clone the repository
```
git clone https://github.com/your-username/london-underground-navigation.git
cd london-underground-navigation
```

2. Create a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate         # On Windows
```

3. Install required Python packages
```
pip install pandas matplotlib numpy
```

4. Ensure custom libraries are accessible

Make sure the custom Python modules provided are in the same directory as ```main.py``` or are in your Python path.

5. Run the main program
```
python main.py
```
<br>

## 🤝 Contributing
If you see something that doesn't look right, speak to staff ([Arslonbek Ishanov](https://github.com/Arslan2003)), open an issue or submit a pull request. We will sort it. See it. Say it. Sorted.  

<br>

Here are a few areas that can be improved:
- Implement new algorithms.
- Add a user-friendly interface.
- Test for edge cases.
- Improve performance.

<br>

## 🧑‍💻 Author
[Arslonbek Ishanov](https://github.com/Arslan2003) - First-Class Graduate Data Scientist & AI/ML Enthusiast.

<br>

## ⚖️ License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<br>

## Tags

