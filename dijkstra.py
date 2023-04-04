import heapq


def dijkstra(graph, start, end):
    """
    Find the shortest path between start and end in a graph using Dijkstra's algorithm.

    Args:
        graph (dict): A dictionary representing the graph, where the keys are the nodes and the values
            are dictionaries containing the neighbors and their distances.
        start (any): The starting node.
        end (any): The ending node.

    Returns:
        A list representing the shortest path from start to end.
    """
    # Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0

    # Initialize priority queue
    pq = [(0, start)]

    while pq:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)

        # Check if we have found the end node
        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous[current_node]
            return path[::-1]

        # Check neighbors
        for neighbor, distance in graph[current_node].items():
            new_distance = current_distance + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (new_distance, neighbor))

    # No path found
    return None
