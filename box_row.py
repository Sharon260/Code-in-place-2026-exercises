try:
    from graphics import Canvas  # type: ignore
except ImportError:
    class Canvas:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def create_rectangle(self, left_x, top_y, right_x, bottom_y, fill_color, outline_color):
            return None

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # Creates a white rectangle 
    # with a black outline
    
    top_y= CANVAS_HEIGHT-BOX_SIZE
    bottom_y= CANVAS_HEIGHT
    
    for i in range (N_BOXES):
        left_x= BOX_SIZE*i
        right_x= BOX_SIZE * (i+1)
        rect= canvas.create_rectangle(
        left_x, 
        top_y, 
        right_x, 
        bottom_y, 
        "white", 
        "black",  
        
    )  
    



    
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    