import pygame
from dijkstra import dijkstra
from draw import draw_nodes, draw_edges, draw_path

# Initialize Pygame
pygame.init()

# Create window
WINDOW_SIZE = (800, 600)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Shortest Path")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define graph
graph = ({'A': {'B': 5, 'D': 1},
          'B': {'A': 5, 'C': 2},
          'C': {'B': 2, 'D': 1},
          'D': {'A': 1, 'C': 1, 'E': 3},
          'E': {'D': 3}},
         {'A': {'B': 3, 'C': 2, 'D': 4},
          'B': {'A': 3, 'C': 1, 'E': 2},
          'C': {'A': 2, 'B': 1, 'D': 2, 'E': 3},
          'D': {'A': 4, 'C': 2, 'F': 3},
          'E': {'B': 2, 'C': 3, 'F': 1, 'G': 2},
          'F': {'D': 3, 'E': 1, 'G': 4},
          'G': {'E': 2, 'F': 4}},
         {'A': {'B': 3, 'C': 2, 'D': 4},
          'B': {'A': 3, 'C': 1, 'E': 2},
          'C': {'A': 2, 'B': 1, 'D': 2, 'E': 3},
          'D': {'A': 4, 'C': 2, 'F': 3},
          'E': {'B': 2, 'C': 3, 'F': 1, 'G': 2},
          'F': {'D': 3, 'E': 1, 'G': 4},
          'G': {'E': 2, 'F': 4}}
         )

# Define nodes
NODE_RADIUS = 20
nodes = ({'A': (100, 100),
          'B': (300, 100),
          'C': (500, 100),
          'D': (200, 400),
          'E': (400, 400)},
         {'A': (100, 100),
          'B': (200, 100),
          'C': (150, 200),
          'D': (100, 300),
          'E': (200, 300),
          'F': (300, 300),
          'G': (250, 200)},
         {'A': (50, 50),
          'B': (100, 100),
          'C': (100, 25),
          'D': (150, 50),
          'E': (150, 125),
          'F': (200, 100),
          'G': (250, 100)}
         )

# Define start and end nodes
start_node = 'A'
end_node = 'D'

# Define example between 0 and 2
option = 1

# Define font
FONT_SIZE = 20
font = pygame.font.SysFont(None, FONT_SIZE)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    window.fill(WHITE)

    # Draw nodes and labels
    draw_nodes(window, nodes[option], graph[option], start_node)

    # Draw edges and labels
    draw_edges(window, nodes[option], graph[option])

    # Find the shortest path
    path = dijkstra(graph[option], start_node, end_node)

    # Draw path and labels
    draw_path(window, path, nodes[option], graph[option])

    # Update screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
