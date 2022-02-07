from turtle import *

speed("fastest")

# turning the turtle to face upwards
rt(-90)

# the acute angle between
# the base and branch of the Y
ANGLE = 30


# function to plot a Y
def draw_y_fractal_tree(size, level):
    if level > 0:
        colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        pencolor(0, 255 // level, 0)

        # drawing the base
        fd(size)

        rt(ANGLE)

        # recursive call for
        # the right subtree
        draw_y_fractal_tree(0.8 * size, level - 1)

        pencolor(0, 255 // level, 0)

        lt(2 * ANGLE)

        # recursive call for
        # the left subtree
        draw_y_fractal_tree(0.8 * size, level - 1)

        pencolor(0, 255 // level, 0)

        rt(ANGLE)
        fd(-size)


# tree of size 80 and level 7
draw_y_fractal_tree(80, 7)
