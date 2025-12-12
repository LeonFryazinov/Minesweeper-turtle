import turtle
import random
import math
import time



mines = []

tile_ammount = 18

tile_width = 32
tiles = []

first_click = True
neighbour_pos = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

def tuple_match(a,b):
    return a[0] == b[0] and a[1] == b[1]
def sum_tuple(a,b):
    return (a[0] + b[0],a[1] + b[1])

def sub_tuple(a,b):
    return (a[0] - b[0],a[1] - b[1])
def mine_pos_taken(pos):
    for mine in mines:
        if mine.match_pos(pos):
            return True
    return False
def match_pos(posA,posB):
    return posA[0] == posB[0] and posA[1] == posB[1]
def pos_in_bound(pos):
    xbound = pos[0] >= 0 and pos[0] <= tile_ammount-1
    ybound = pos[1] >= 0 and pos[1] <= tile_ammount-1
    return xbound and ybound

def delete_item_from_list(tile_list,):
    pass
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
        self.render_pos = pos[0]*tile_width-(tile_width*tile_ammount/2),pos[1]*tile_width-(tile_width*tile_ammount/2)
        self.mine = None
        self.flagged = False
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.number = 0
        self.hidden = True
    def draw_tile(self,turt):
        t.color("black","lime" if self.hidden else "#d1b06f")
        t.up()
        t.goto(sum_tuple(self.render_pos,(-self.width/2,self.height/2)))#top left corner
        t.down()
        t.begin_fill()
        t.goto(sum_tuple(self.render_pos,(self.width/2,self.height/2))) # top right corner
        t.goto(sum_tuple(self.render_pos,(self.width/2,-self.height/2))) # Bottom right corner
        t.goto(sum_tuple(self.render_pos,(-self.width/2,-self.height/2)))# Bottom Left corner
        t.goto(sum_tuple(self.render_pos,(-self.width/2,self.height/2)))#top left corner again
        t.end_fill()
        t.up()
        t.goto(sum_tuple(self.render_pos,(0,-self.height/2)))
        if (not self.hidden): 
            if self.number == -1:
                t.color("red")
                t.goto(sum_tuple(self.render_pos,(-self.width/2,self.height/2)))
                t.down()
                t.goto(sum_tuple(self.render_pos,(self.width/2,-self.height/2)))
                t.up()
                t.goto(sum_tuple(self.render_pos,(self.width/2,self.height/2)))
                t.down()
                t.goto(sum_tuple(self.render_pos,(-self.width/2,-self.height/2)))
                t.up()
                t.color("black", "lime")
            elif self.number != 0:
                t.write(str(self.number), align="center", font=("Courier", 24, "bold"))
                #t.write(str(self.pos), align="center", font=("Courier", 6, "bold"))
        if self.flagged:
            t.color("red")
            t.write("flag", align="center", font=("Courier", 8, "bold"))
            t.color("black", "lime")
        
        
    def calculate_number(self,mine_list):
        mine_count = 0
        
        for mine in mine_list:
            
            if mine.border_pos(self.pos):
                mine_count += 1
            if mine.match_pos(self.pos):
                mine_count = -1
                #print("mine added")
                break

        self.number = mine_count
        
def find_clicked_tile(x,y):
    target_tile = None
    for tile in tiles:
        u_x_bound = tile.render_pos[0] + tile.width/2
        l_x_bound = tile.render_pos[0] - tile.width/2
        u_y_bound = tile.render_pos[1] + tile.height/2
        l_y_bound = tile.render_pos[1] - tile.height/2

        in_x_bound = x < u_x_bound and x > l_x_bound
        in_y_bound = y < u_y_bound and y > l_y_bound

        if in_x_bound and in_y_bound:
            target_tile = tile
            break
    
    return target_tile

def get_tile(x,y):
    for tile in tiles:
        if match_pos(tile.pos,(x,y)):
            return tile
    
    return None

def find_neighbours(start_pos):
    start_tile = get_tile(start_pos[0],start_pos[1])
    neighbours_list = [start_tile]
    start_exists = start_tile != None
    if start_exists:
        start_zero = start_tile.number == 0   
    else:
        return None
    
    
    if start_zero:
        search_list = []
        
        for direction in neighbour_pos:
            pot_pos = sum_tuple(start_pos,direction)
            if pos_in_bound(pot_pos):
                new_tile = get_tile(pot_pos[0],pot_pos[1])
                if new_tile != None:
                    search_list.append(new_tile)
                    

        while len(search_list) > 0:
            #print(search_list)
            for tile in search_list:
                search_list.remove(tile)
                #print(len(search_list))
                if not tile in neighbours_list:
                    neighbours_list.append(tile)
                    
                    if tile.number == 0:
                        #add neighbouring tiles to the search list
                        for direction in neighbour_pos:
                            pot_pos = sum_tuple(tile.pos,direction)
                            if pos_in_bound(pot_pos):
                                new_tile = get_tile(pot_pos[0],pot_pos[1])
                                if new_tile != None:
                                    search_list.append(new_tile)
                                    #print(f"added new tile to search at coordinate: {pot_pos}")
                                    


            
            
                                    
                                    

    return neighbours_list
        
    

    



screen = turtle.Screen()
t = turtle.Turtle()
t.color("black", "lime")
t.ht()
t.pensize(2)
t.speed(0)
screen.tracer(0)

def redraw(t):
    for tile in tiles:
        t.clear
        tile.draw_tile(t)
    screen.update()

def click_handler(x,y):
    #print(f"X:{x} and Y: {y}")
    target_tile = find_clicked_tile(x,y)
    if target_tile == None:
        print("no tile clicked")
    else:
        if target_tile.number == -1:
            if target_tile.flagged:
                target_tile.flagged = False
            else:
                #print("clicked mine")
                target_tile.hidden = False
            redraw(t)
        else:
            #print("pressed safe")
            tile_pos = target_tile.pos
            unhidden_list = find_neighbours(tile_pos)
            for tile in unhidden_list:
                tile.hidden = False
                tile.flagged = False
            
            redraw(t)



def right_click_handler(x,y):
    init_time = time.time()
    #print(f"right click X:{x} and Y: {y}")
    target_tile = find_clicked_tile(x,y)
    if target_tile == None:
        print("no tile clicked")
    else:
        print(f"done tile finding in {time.time()-init_time}")
        target_tile.flagged = True if not target_tile.flagged else False
        new_init_time = time.time()
        redraw(t)
        print(f"flagging and redrawing done in {time.time()-new_init_time}")
            



for x in range(tile_ammount):
    for y in range(tile_ammount):
        tiles.append(Tile((x,y),(tile_width,tile_width)))

mine_count = 35


for i in range(mine_count):
    
    new_x = random.randint(0,tile_ammount-1)
    new_y = random.randint(0,tile_ammount-1)
    pos_taken = mine_pos_taken((new_x,new_y))
    if not pos_taken:
        new_mine = Mine((new_x,new_y))
        mines.append(new_mine)
    else:
        while pos_taken:
            new_x = random.randint(0,tile_ammount-1)
            new_y = random.randint(0,tile_ammount-1)
            pos_taken = mine_pos_taken((new_x,new_y))
            new_mine = Mine((new_x,new_y))
            
            #print("stuck finding a mine place")
        mines.append(new_mine)
    #print(f"x:{new_x},y:{new_y}")



t.clear()
#print(mines)
for tile in tiles:
    tile.calculate_number(mines)
    tile.draw_tile(t)
screen.update()
print(len(mines))
screen.onscreenclick(click_handler)
screen.onscreenclick(fun=right_click_handler,btn=3)
screen.mainloop()


#tile_list = []
#for x in range(10):
#    for y in range(10):
#        tile_list.append(Tile((x,y)))
#

