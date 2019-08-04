# ColorMeSpiraled.py
# Billy Ridgeway
# Creates a colorful spiral of the user's name.

import turtle               # Import turtle graphics.
t = turtle.Pen()            # Creates a new turtle called t.
t.speed(0)                  # Set the speed of the pen to fast.
turtle.bgcolor("black")     # Set the background color to black.

# Create a list of colors to be used in the spiral.
colors = ["red", "yellow", "blue", "green"]

# Ask the user's name using turtle's text input pop-up window.
your_name = turtle.textinput("Enter your name", "What is your name?")

# Ask the user for the number of sides, default to 4, minimum 1 and maximum 8.
sides = int(turtle.numinput("Number of sides", "How many sides do you want (1-8)?", 4, 1, 8))

# Draw a spiral of the user's name on the screen, written 100 times.
for x in range (360):               # Set the variable 'x' to 360.
    t.pencolor( colors[ x % 4] )    # Cycle the pen colors through the list.
    t.penup()                       # Left the pen up.
    t.forward( x * 4 )              # Move the pen forward by the value of 'x' times 4.
    t.pendown()                     # Put the pen down so it can write.
    # Writes your name in the selected color using bold Arial font with the size set
    # to the value of x plus 4 divided by 4.
    t.write(your_name, font = ("Arial", int( (x + 4) / 4), "bold") )
    t.left(360/sides + 1)           # Turn the pen left by 360 degrees divided by the number
                                    # of sides plus 1.
    t.width( x * sides / 200)       # Set the width of the pen to the value of 'x' times
                                    # the number of sides divided by 200.
