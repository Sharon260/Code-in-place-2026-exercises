#Your first objective is to recreate this quilt:

#Each patch has height and width of 100 pixels, given by the constant PATCH_SIZE. There are two different patch patterns that repeat in different locations.

#In this assignment each patch will be defined by a function. For example consider the draw_square_patch function which is already implemented for you in the starter code. This function draws a square patch at the given (start_x, start_y) location. You will implement the draw_circle_patch function to draw a circle patch at the given (start_x, start_y) location.

from graphics import Canvas  # type: ignore[import-not-found]

# each patch is a square with this width and height:
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # draw the first row of patches
    draw_square_patch(canvas, 0, 0)
    draw_circle_patch(canvas, PATCH_SIZE, 0)
    draw_square_patch(canvas, PATCH_SIZE*2, 0)
    draw_square_patch(canvas, PATCH_SIZE, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE*3, PATCH_SIZE)

    # TODO: your code here
    
def draw_circle_patch(canvas, start_x, start_y):
    #draws a salmon circle
        oval=canvas.create_oval (0, PATCH_SIZE, PATCH_SIZE * (0 +1),CANVAS_HEIGHT , "salmon")
        oval=canvas.create_oval ( 1* PATCH_SIZE, 0, PATCH_SIZE * (1 +1),PATCH_SIZE , "salmon")
        oval=canvas.create_oval ( 2* PATCH_SIZE, PATCH_SIZE, PATCH_SIZE * (2 +1),CANVAS_HEIGHT , "salmon")
        oval=canvas.create_oval ( 3* PATCH_SIZE, 0, PATCH_SIZE * (3 +1),PATCH_SIZE , "salmon")
   
    
def draw_square_patch(canvas, start_x, start_y):
    # draws a purple frame at (start_x, start_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 20
    # first draw a purple square over the entire patch
    canvas.create_rectangle(start_x, start_y, end_x, end_y, 'purple')
    # then draw a smaller white square on top
    canvas.create_rectangle(start_x+inset, start_y+inset, 
        end_x-inset, end_y-inset, 'white')
    
if __name__ == '__main__':
    main()