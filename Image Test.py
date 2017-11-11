from PIL import Image ##Image interaction module; used to get the rgb values of the given picture
import turtle ##Imports the turtle module for the graphics part of this code; used to redraw the image
from time import clock ##Imports the clock function from the time module; used to give code runtime

im = Image.open(r"C:\Users\Dania\Downloads\Black_Cat.jpg") ##Sets variable im to the given image (Notes: must use absolute path, can be many different image formats not just .jpg)
rgb_im = im.convert('RGB') ##Converts the image in variable im to it's rgb values

x,y = im.size ##Sets variable x and y to the width and height of the image in pixels
print(str(x) + " pixels by " + str(y) + " pixels") ##Prints the width and hight of the image
x-=1 ##Acounts for the fact that lists start at 0 rather than 1 
y-=1 ##Same as above


my_turtle = turtle.Turtle() ##Generates turtle object named my_turtle (Note: Can be called anything you want)
turtle.colormode(255) ##Sets turtle colormode to rgb
my_turtle.speed(0) ##Sets turtle to maximum speed (Note: No animation, turtle acts as if it teleports from one spot to another)
turtle.getscreen().delay(0) ##Sets the delay for every turtle action to 0; doesn't pause after every move
turtle.getscreen().tracer(2000, 0) ##Disables screen loading until the 2000th move has been made, then updates the screen (Note: Second arg is for delay)
turtle.hideturtle() ##Makes the turtle invisible 
my_turtle.hideturtle() ##Makes the turtle invisible


def colorLoop(): ##Function that redraws the image
    nowX = 1 ##Sets the current x being iterated over
    nowY = 1 ##Sets the current y being iterated over
    while nowY <= y: ##Loops inner code until the current y is equal to variable y
        while nowX <= x: ##Loops inner code until the current x is equal to variable x (Note: This code is repeated for every y value)
            r, g, b = rgb_im.getpixel((nowX, nowY)) ##Sets variable r, g, b to the rgb value of the current pixel being iterated over
            my_turtle.color(r,g,b) ##Sets turtle color to the rgb value of the current pixel
            my_turtle.forward(1) ##Moves turtle to the next pixel
            nowX = nowX+1 ##Increases the current x value
        my_turtle.right(90) ##Turn the turtle so it faces down
        my_turtle.forward(1) ##Moves forward to the next y level
        nowY = nowY+1 ##Increases the current y value (See above)
        my_turtle.right(90) ##Turns the turtle so it faces to the left
        my_turtle.forward(nowX-1) #Moves the turtle to x = 1 (Back to where the turtle started but one y level down)
        nowX = 1 ##ets the current x value to one (See above)
        my_turtle.right(180) 
        
        
        
print("Beginning color process")
at = clock()
colorLoop()
et = clock()
print("Runtime: %.2f sec." % (et-at))


    


