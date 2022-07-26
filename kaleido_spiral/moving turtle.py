import turtle as t 
import random as rd

def window():
    left_window = (-t.window_width()/2)+100 
    right_window = (t.window_width()/2 ) -100 
    bottom_window = (-t.window_height()/2) +100
    top_window = (t.window_height()/2) - 100 
    
    (x,y) = t.pos()
    inside = left_window < x < right_window and bottom_window<y<top_window
    return inside 

def move_turtle():
    if window():
        angle = rd.randint(0,180)
        forw = rd.randint(50,200)
        t.right(angle)
        t.forward(forw)
    else:
        t.backward(200)





t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('slow')

while True:
    move_turtle()