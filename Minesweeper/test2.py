import turtle

def sum_tuple(a,b):
    return (a[0] + b[0],a[1] + b[1])

def sign(x):
    return int(x/abs(x))
points = []

def click_handler(x, y):
    points.append((x,y))
    my_turtle.penup()
    my_turtle.goto((x,y))
    my_turtle.pendown()
    my_turtle.goto((x+0.1,y))
    my_turtle.penup()
    
    if len(points) == 2:
        init_point = points[0]
        final_point = points[1]

        delta_x = final_point[0] - init_point[0]
        delta_y = final_point[1] - init_point[1]
        if abs(delta_x) != abs(delta_y):
            print("NOT UNIFORM, MAKING UNIFORM")
            new_final = sum_tuple(init_point,(final_point[0],init_point[1]+(sign(delta_y)*abs(delta_x))))
            final_point = new_final
            delta_y = (sign(delta_y)*abs(delta_x))

        sign_x = sign(delta_x)
        sign_y = sign(delta_y)
        anchor_point = 
        if sign_x == 1 or sign_x == 0:
            
        else:
            


screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.color("black")
my_turtle.pensize(5)

screen.onscreenclick(click_handler)

screen.mainloop()
