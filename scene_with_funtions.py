#you will draw a natural scene while practicing how to break a program into functions with parameters. You are also being given an AI code-completion tool for this assignment. The tool can suggest code, but you are responsible for reading the generated code carefully and deciding whether it is correct.

#This assignment is self-graded. When you have visited the page, read this disclosure, and tried the assignment, use the normal mark-complete action to acknowledge participation and complete it.

from graphics import Canvas  # type: ignore[reportMissingImports]

import math
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

x = random.randint(1, CANVAS_WIDTH)

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # draw clouds
    draw_cloud(canvas, x * 2, 10, 'dark blue')
    draw_cloud(canvas, x * 4, 40, 'blue')
    draw_cloud(canvas, x * 3, 50, 'light blue')
    draw_cloud(canvas, x, 100, 'blue')

    # draw trees
    draw_tree(canvas, 60, TREE_BOTTOM_Y)
    draw_tree(canvas, 180, TREE_BOTTOM_Y)
    draw_tree(canvas, 300, TREE_BOTTOM_Y)

    # draw flowers
    draw_flower(canvas, 80, 250)
    draw_flower(canvas, 200, 255)
    draw_flower(canvas, 320, 250)


def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in
    different values of x and y (the location of the cloud) and
    color (the color of the cloud).
    """

    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH

    # Bottom two puffs
    canvas.create_oval(
        x,
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH,
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )


def draw_tree(canvas, x, bottom_y):
    """Draw a tree with a trunk and leaves at the given x position."""
    trunk_top_y = bottom_y - TRUNK_HEIGHT

    # Draw trunk
    canvas.create_line(x, bottom_y, x, trunk_top_y, "brown")

    # Draw leaves
    leaf_radius = LEAVES_SIZE / 2
    canvas.create_oval(
        x - leaf_radius,
        trunk_top_y - leaf_radius,
        x + leaf_radius,
        trunk_top_y + leaf_radius,
        "green"
    )
    canvas.create_oval(
        x - (2 * leaf_radius / 3),
        trunk_top_y - (leaf_radius + 10),
        x + (2 * leaf_radius / 3),
        trunk_top_y + 10,
        "green"
    )
    canvas.create_oval(
        x - (leaf_radius / 2),
        trunk_top_y - leaf_radius,
        x + (leaf_radius * 1.5),
        trunk_top_y + (leaf_radius * 0.5),
        "green"
    )


def draw_flower(canvas, x, y):
    """Draws a flower at the given (x, y) location."""
    # Draw stem
    canvas.create_line(x, y, x, y + 50, "green")

    # Draw left leaf
    canvas.create_oval(x - 15, y + 20, x + 5, y + 40, "green")

    # Draw right leaf
    canvas.create_oval(x, y + 20, x + 20, y + 40, "green")

    # Draw flower petals
    petal_radius = 13
    canvas.create_oval(x - petal_radius, y - petal_radius, x, y, "violet")
    canvas.create_oval(x, y - petal_radius, x + petal_radius, y, "violet")
    canvas.create_oval(x - petal_radius, y, x, y + petal_radius, "violet")
    canvas.create_oval(x, y, x + petal_radius, y + petal_radius, "violet")

    # Draw center of flower
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, "yellow")




if __name__ == '__main__':
    main()