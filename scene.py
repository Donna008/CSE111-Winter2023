# Import the functions from the Draw 2-D library
# so that they can be used in this program.

from draw2d import\
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500
    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas,scene_width,scene_height)
    draw_ground(canvas,scene_width,scene_height)
    draw_cloud(canvas,scene_width /2,scene_height)
    draw_cloud(canvas,scene_width / 1.5,scene_height)
    draw_pine_tree(canvas,250,0,250)
    draw_pine_tree(canvas,150,100,200)
    draw_pine_tree(canvas,350,100,250)
    draw_pine_tree(canvas,50,0,300)
    for x in range(100,700,100):
        draw_pine_tree(canvas,x,250,80)
    
    # Draw 100 circles, each with
    # a random location and diameter.
    import random
    half_height = round(scene_height / 2)
    min_diam = 5
    max_diam = 10
    for i in range(100):
        x = random.randint(20, scene_width - max_diam)
        y = random.randint(10, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="white")

    #draw_rectangle(canvas,500,200,100)
    draw_grid(canvas, scene_width, scene_height, 50)
   
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas,scene_width,scene_height):
    #draw the sky and all the objects in the sky.
    draw_rectangle(canvas,0,scene_height / 3,scene_width,scene_height,width=0,fill="sky blue")
    
def draw_ground(canvas, scene_width,scene_height):
    #draw the ground and all the objects on the ground.
    draw_rectangle(canvas,0,0,scene_width,scene_height / 2, width=0,fill="tan4")

def draw_cloud(canvas,scene_width,scene_height):
    #draw the cloud.
    draw_text(canvas,250,200,"ola",fill="white")
    draw_oval(canvas,50,scene_height / 1.5,130,scene_height,width= 1,outline="",fill="white")
    draw_oval(canvas,40,350,scene_width,scene_height,width= 1,outline="",fill="white")

def draw_pine_tree(canvas,center_x,bottom,height):
    #draw the trunk of the tree.
    trunk_width = height / 10
    trunk_hight = height / 8
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_hight
    draw_rectangle(canvas,left_trunk,bottom_trunk,right_trunk,trunk_top,fill="tan4")

    #draw the skirt of the tree.
    skirt_width = height / 2
    
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x +skirt_width /2 
    draw_polygon(canvas,skirt_left,skirt_bottom,peak_x,peak_y,skirt_right,skirt_bottom,fill="forestGreen")


def draw_grid(canvas, width, height,interval):
    #draw vertical lines
    label_y = 15
    for x in range(interval,width,interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x,label_y, f"{x}")

    #draw horizontal lines
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas,0,y,width,y)
        draw_text(canvas, label_x,y,f"{y}")

# Call the main function so that
# this program will start executing.
main()