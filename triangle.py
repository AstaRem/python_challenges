# Triangle

# You may remember the square of stars example. This is similar, but draws a triangle.

# Your code should have a function called triangle(size) that outputs a triangle of a given size. Ask the user what size the triangle should be and then draw it using your function.

size = int(input("How big you would like oyur triangle to be? Please enter a positive integer: "))

def triangle(size):
    star = "*"
    counter = 1
    while counter  <= size:
        print (counter * star)
        counter += 1

triangle(size)