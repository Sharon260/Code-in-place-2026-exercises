# To start out, one of the most straightforward flags to draw using Python graphics is the flag of Indonesia:
# The dimensions of your flag should be based off the provided constants: 450, 300.
# The top half of the flag should be red, and the bottom half should be white.
# You can use the create_rectangle method to draw the two halves of the flag.

# The width of the canvas
CANVAS_WIDTH = 450
# The height of the canvas
CANVAS_HEIGHT = 300

try:
    from importlib import import_module

    Canvas = import_module("graphics").Canvas
except ImportError:
    class Canvas:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def create_rectangle(self, left_x, top_y, right_x, bottom_y, color):
            return {
                "left": left_x,
                "top": top_y,
                "right": right_x,
                "bottom": bottom_y,
                "color": color,
            }


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT / 2, 'red')
    canvas.create_rectangle(0, CANVAS_HEIGHT / 2, CANVAS_WIDTH, CANVAS_HEIGHT, 'white')


if __name__ == '__main__':
    main()