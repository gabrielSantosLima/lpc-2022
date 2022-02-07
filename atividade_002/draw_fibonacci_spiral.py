# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math


def draw_fibonacci_spiral(number):
    a = 0
    b = 1
    square_a = a
    square_b = b

    # Setting the colour of the plotting pen to blue
    painter.pencolor("blue")

    # Drawing the first square
    painter.forward(b * FACTOR)
    painter.left(90)
    painter.forward(b * FACTOR)
    painter.left(90)
    painter.forward(b * FACTOR)
    painter.left(90)
    painter.forward(b * FACTOR)

    # Proceeding in the Fibonacci Series
    temp = square_b
    square_b = square_b + square_a
    square_a = temp

    # Drawing the rest of the squares
    for n in range(1, number):
        painter.backward(square_a * FACTOR)
        painter.right(90)
        painter.forward(square_b * FACTOR)
        painter.left(90)
        painter.forward(square_b * FACTOR)
        painter.left(90)
        painter.forward(square_b * FACTOR)

        # Proceeding in the Fibonacci Series
        temp = square_b
        square_b = square_b + square_a
        square_a = temp

    # Bringing the pen to starting point of the spiral plot
    painter.penup()
    painter.setposition(FACTOR, 0)
    painter.seth(0)
    painter.pendown()

    # Setting the colour of the plotting pen to red
    painter.pencolor("red")

    # Fibonacci Spiral Plot
    painter.left(90)
    for _ in range(number):
        print(b)
        spiral_length = math.pi * b * FACTOR / 2
        spiral_length /= 90
        for j in range(90):
            painter.forward(spiral_length)
            painter.left(1)
        temp = a
        a = b
        b = temp + b


# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
FACTOR = 1

# Taking Input for the number of
# Iterations our Algorithm will run
number_of_iterations = int(input("Enter the number of iterations (must be > 1): "))

# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number
if number_of_iterations > 0:
    print("Fibonacci series for", number_of_iterations, "elements :")
    painter = turtle.Turtle()
    painter.speed(100)
    draw_fibonacci_spiral(number_of_iterations)
    turtle.done()
else:
    print("Number of iterations must be > 0")
