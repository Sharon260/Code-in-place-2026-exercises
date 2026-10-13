#To start out, one of the most straightforward flags to draw using Python graphics is the flag of Indonesia: The dimensions of your flag should be based off the provided constants: 450, 300. The top half of the flag should be red, and the bottom half should be white. You can use the create_rectangle method to draw the two halves of the flag.

# The width of the canvas
CANVAS_WIDTH = 450
# The height of the canvas
CANVAS_HEIGHT = 300
from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO, your code here
    left_x=0
    top_y= 0
    right_x=CANVAS_WIDTH
    bottom_y= CANVAS_HEIGHT/2
    rect= canvas.create_rectangle( left_x, top_y, right_x, bottom_y, 'red')
    

if __name__ == '__main__':
    main()