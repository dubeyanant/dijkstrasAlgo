import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
FONT_SIZE = 20


def draw_nodes(window, nodes, graph, start_node):
    """Draw nodes and node labels on the window"""
    font = pygame.font.SysFont(None, FONT_SIZE)
    for node, pos in nodes.items():
        color = BLACK
        if node == start_node:
            color = RED
        pygame.draw.circle(window, color, pos, 20)

        # Draw node label
        label_text = f"{node} ({graph[start_node]})"
        label = font.render(label_text, True, BLACK)
        label_pos = (pos[0] - FONT_SIZE, pos[1] - FONT_SIZE)
        window.blit(label, label_pos)


def draw_edges(window, nodes, graph):
    """Draw edges and edge labels on the window"""
    font = pygame.font.SysFont(None, FONT_SIZE)
    for node, neighbors in graph.items():
        for neighbor, distance in neighbors.items():
            start_pos = nodes[node]
            end_pos = nodes[neighbor]
            pygame.draw.line(window, BLACK, start_pos, end_pos, 3)

            # Draw edge label
            label_text = str(distance)
            label = font.render(label_text, True, BLACK)

            # Compute label position
            mid_x = (start_pos[0] + end_pos[0]) // 2
            mid_y = (start_pos[1] + end_pos[1]) // 2
            label_pos = (mid_x - FONT_SIZE // 2, mid_y - FONT_SIZE // 2)

            # Draw label on window
            window.blit(label, label_pos)


def draw_path(window, path, nodes, graph):
    """Draw shortest path and path labels on the window"""
    font = pygame.font.SysFont(None, FONT_SIZE)
    for i in range(len(path) - 1):
        start_pos = nodes[path[i]]
        end_pos = nodes[path[i + 1]]
        pygame.draw.line(window, RED, start_pos, end_pos, 3)

        # Draw edge label
        label_text = str(graph[path[i]][path[i + 1]])
        label = font.render(label_text, True, RED)

        # Compute label position
        mid_x = (start_pos[0] + end_pos[0]) // 2
        mid_y = (start_pos[1] + end_pos[1]) // 2
        label_pos = (mid_x - FONT_SIZE // 2, mid_y - FONT_SIZE // 2)

        # Draw label on window
        window.blit(label, label_pos)
