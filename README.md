## Dijkstra's Algorithm Implementation

The code consists of three files: dijkstra.py, draw.py, and main.py.

### dijkstra.py
The dijkstra.py file contains the implementation of Dijkstra's algorithm. This is a widely used algorithm to find the shortest path between two nodes in a graph. The implementation takes a graph represented as a dictionary of dictionaries, where each key is a node in the graph, and the value is another dictionary representing the edges from that node, where the keys are the neighboring nodes and the values are the edge weights. The dijkstra() function returns the shortest path and its length between a start node and an end node using the Dijkstra's algorithm.
### draw.py
The draw.py file contains functions responsible for drawing the nodes, edges, and shortest path on the pygame window. The draw_nodes() function takes the window, dictionary of nodes and their positions, graph, and the start node, and draws the nodes with their labels. The draw_edges() function takes the same inputs and draws the edges with their labels. The draw_path() function takes the window, the shortest path, the dictionary of nodes and their positions, and the graph and draws the shortest path with its labels.
### main.py
The main.py file is the main file that uses the above files to visualize the graph, shortest path, and nodes on a pygame window. The main() function initializes the pygame window, reads the graph from a CSV file, prompts the user for the start and end nodes, calls the dijkstra() function to get the shortest path, and calls the draw_nodes(), draw_edges(), and draw_path() functions to draw the nodes, edges, and shortest path on the window. The run() function runs the pygame window and the main() function.
### Summary
The code uses Dijkstra's algorithm to find the shortest path between two nodes in a graph and visualizes the graph, shortest path, and nodes on a pygame window. It's a great example of how to implement a common algorithm and how to use a popular library like pygame to visualize the results.