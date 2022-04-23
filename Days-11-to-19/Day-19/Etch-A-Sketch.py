import turtle as t

tim = t.Turtle()
screen = t.Screen()
screen.listen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def clockwise():
    tim.right(5)

def counter_clockwise():
    tim.left(5)

def clear_screen():
    tim.reset()


screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=clear_screen)












screen.exitonclick()