# Dijkstra's Algorithm Implementation

The code consists of three files: dijkstra.py, draw.py, and main.py.

## dijkstra.py

The dijkstra.py file contains the implementation of Dijkstra's algorithm. This is a widely used algorithm to find the
shortest path between two nodes in a graph. The implementation takes a graph represented as a dictionary of
dictionaries, where each key is a node in the graph, and the value is another dictionary representing the edges from
that node, where the keys are the neighboring nodes and the values are the edge weights. The dijkstra() function returns
the shortest path and its length between a start node and an end node using the Dijkstra's algorithm.

### Code Explanation

```
import heapq
```

This line imports the heapq module, which provides an implementation of the heap queue algorithm.

```
def dijkstra(graph, start, end):
```

This is the function signature and the docstring for the dijkstra function. The function takes three arguments: graph,
start, and end, and returns a list representing the shortest path from start to end.

``` 
distances = {node: float('inf') for node in graph}
previous = {node: None for node in graph}
distances[start] = 0
```

These lines initialize two dictionaries: distances and previous. distances stores the shortest distance from the start
node to each node in the graph, and previous stores the previous node in the shortest path to each node. Initially, all
distances are set to infinity and all previous nodes are set to None, except for the start node, which is set to 0.

```
pq = [(0, start)]
```

This line initializes a priority queue pq with a tuple containing the distance to the start node (0) and the start node
itself. The priority queue will be used to keep track of the nodes to visit in order of increasing distance from the
start node.

```
while pq:
    current_distance, current_node = heapq.heappop(pq)
```

These lines start a while loop that continues until the priority queue pq is empty. In each iteration of the loop, the
node with the smallest distance is removed from the priority queue using the heapq.heappop method. The current_distance
variable stores the distance to the current node, and the current_node variable stores the current node.

```
if current_node == end:
    path = []
    while current_node:
        path.append(current_node)
        current_node = previous[current_node]
    return path[::-1]
```
This block of code checks if the current node is the end node. If it is, the function reconstructs and returns the
shortest path from start to end by following the previous nodes. It does this by initializing an empty list path, and
then appending each node to the list in reverse order by following the previous nodes. The [::-1] at the end of the
return statement reverses the order of the nodes in the list, so that the path is from start to end.

```
    for neighbor, distance in graph[current_node].items():
        new_distance = current_distance + distance
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            previous[neighbor] = current_node
            heapq.heappush(pq, (new_distance, neighbor))
```
This block of code iterates through the neighbors of the current node and checks if the distance to each neighbor can be improved by going through the current node. If the new distance is less than the current distance to the neighbor, then the distance and previous node for the neighbor are updated, and the neighbor is added to the priority queue with its new distance. The heapq.heappush method is used to add the neighbor to the priority queue in the correct order based on its new distance.

```
return None
```
If the end node is not found and the priority queue becomes empty, the function returns None to indicate that there is no path from start to end in the graph.

## draw.py

The draw.py file contains functions responsible for drawing the nodes, edges, and shortest path on the pygame window.
The draw_nodes() function takes the window, dictionary of nodes and their positions, graph, and the start node, and
draws the nodes with their labels. The draw_edges() function takes the same inputs and draws the edges with their
labels. The draw_path() function takes the window, the shortest path, the dictionary of nodes and their positions, and
the graph and draws the shortest path with its labels.

### Code Explanation

```
import pygame
```
The pygame module is imported to allow drawing on a Pygame window.

```
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FONT_SIZE = 20
```
These three constants are defined to set the colors and font size used for drawing on the window.

```
def draw_nodes(window, nodes, graph, start_node):
```
This function draws circles on the Pygame window to represent the nodes in the graph. The position of each node is specified in the nodes dictionary, and the starting node is highlighted in red. A label is also drawn next to each node showing its name and the distances to its neighbors.

```
def draw_edges(window, nodes, graph):
```
This function draws lines on the Pygame window to represent the edges in the graph. The position of each node is specified in the nodes dictionary, and the edges are drawn between the positions of their two endpoints. A label is also drawn next to each edge showing its weight.

```
def draw_path(window, path, nodes, graph):
```
This function is used to highlight the shortest path between two nodes on the window. It draws a red line connecting the nodes on the path and also draws a label next to each edge on the path showing its weight.

In all three functions, a Pygame font object is created using the pygame.font.SysFont function with None as the font name, which means that the default system font is used. The pygame.draw functions are then used to draw shapes and lines on the Pygame window, and the window.blit function is used to draw the labels on the window.

## main.py

The main.py file is the main file that uses the above files to visualize the graph, shortest path, and nodes on a pygame
window. The main() function initializes the pygame window, reads the graph from a CSV file, prompts the user for the
start and end nodes, calls the dijkstra() function to get the shortest path, and calls the draw_nodes(), draw_edges(),
and draw_path() functions to draw the nodes, edges, and shortest path on the window. The run() function runs the pygame
window and the main() function.

### Code Explanation



## Summary

The code uses Dijkstra's algorithm to find the shortest path between two nodes in a graph and visualizes the graph,
shortest path, and nodes on a pygame window. It's a great example of how to implement a common algorithm and how to use
a popular library like pygame to visualize the results.