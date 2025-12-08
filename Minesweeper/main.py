import turtle
import random
import math



mines = []


def click_handler():
    return "yes"
 
def sum_tuple(a,b):
    return (a[0] + b[0],a[1] + b[1])

def sub_tuple(a,b):
    return (a[0] - b[0],a[1] - b[1])

class Mine:
    def __init__(self,pos):
        self.pos = pos
    def match_pos(self,pos):
        if pos[0] == self.pos[0] and pos[1] == self.pos[1]:
            return True
        else:
            return False
    
    def border_pos(self,position):
        diff = sub_tuple(self.pos,position)
        is_border_x = diff[0] in [-1,0,1]
        is_border_y = diff[1] in [-1,0,1]
        if is_border_x and is_border_y:
            return True
class Tile:
    def __init__(self,pos,dimensions):
        self.pos = pos
        self.mine = None
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.number = 0
    def draw_tile(self,turt):
        t.up()
        t.goto(sum_tuple(self.pos,(-self.width/2,self.height/2)))#top left corner
        t.down()
        t.begin_fill()
        t.goto(sum_tuple(self.pos,(self.width/2,self.height/2))) # top right corner
        t.goto(sum_tuple(self.pos,(self.width/2,-self.height/2))) # Bottom right corner
        t.goto(sum_tuple(self.pos,(-self.width/2,-self.height/2)))# Bottom Left corner
        t.goto(sum_tuple(self.pos,(-self.width/2,self.height/2)))#top left corner again
        t.end_fill()
        t.up()
        t.goto(sum_tuple(self.pos,(0,-self.height/2)))
        
        t.write(str(self.number), align="center", font=("Courier", 16, "bold"))
        
        
    def calculate_number(self,mine_list):
        mine_count = 0
        for mine in mine_list:
            if mine.border_pos(self.pos):
                mine_count += 1
            if mine.match_pos(self.pos):
                mine_count = -1
                break

        self.number = mine_count
        
        
tile_1 = Tile((0,0),(50,50))
tile_2 = Tile((0,1),(50,50))


screen = turtle.Screen()
t = turtle.Turtle()
t.color("black", "lime")
t.ht()
t.pensize(1)
t.speed(0)

tile_1 = Tile((0,0),(32,32))
tile_1.draw_tile(t)
#t.write("3", align="center", font=("Courier", 16, "bold"))
screen.onscreenclick(click_handler)

screen.mainloop()


#tile_list = []
#for x in range(10):
#    for y in range(10):
#        tile_list.append(Tile((x,y)))
#

