from turtle import *
from random import *
speed(0)
map1 = [
    "WWWWWWWWWWWWWWWWWWWWWWWW",
    "W P   W     D     W  GWW",
    "W WWW W WWWWW WWW W WWWW",
    "W   W W       W      WWW",
    "WWW W WWWWW W WWW WWWW W",
    "W   W     W W     D    W",
    "W WWWWWWW W WWWWW WWWWWW",
    "W     D   W     W     WW",
    "W WWWWW WWWWW WWWWW WWWW",
    "W    W  W D     WW W   W",
    "WWW  WWWW   D   WW WW  W",
    "W  W    DWW  W W    WW W",
    "WWWWWWW  DWWWW       G W",
    "W  WG W        WWWWW  WW",
    "W  WW   WWWWWWD DW W   W",
    "W                  WWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWW",
]

map2 = [
    "WWWWWWWWWWWWWWWWWWWWWWWW",
    "W DD  WD   W          GW",
    "W  W   W   W   WWWWWW WW",
    "WD W   W   W   W  D W  W",
    "WD WW  WWWWW  WW      DW",
    "W        DW   W   WWW WW",
    "W WWWWW       W     WD W",
    "W  D  W   W   W     W  W",
    "W  WW  WW W     WWWWD DW",
    "W    W    D     WWW   GW",
    "WWWW WWW     WWWWD   DDW",
    "W   W    D  W          W",
    "W WWWW  WW  W   WWWW  WW",
    "WW    D W    WW  D    DW",
    "WWW   WWW   WWWWW   WWWW",
    "WW      P             WW",
    "WWWWWWWWWWWWWWWWWWWWWWWW",
]

map3 = [
    "WWWWWWWWWWWWWWWWWWWWWWWW",
    "WD  WWWW  GGG  WWWWW DDW",
    "W   W  WD   DW        WW",
    "WWW    WWWWWWWWWW W  DWW",
    "W   W  WWW DWW   W W   W",
    "WWWWW  W     W    WW WWW",
    "WWD   W     W D        W",
    "W   DWWWW  W     WWWWWWW",
    "W   W      WWWW  WW    W",
    "W  W   WWWW          WWW",
    "WP     WD    W   W W  DW",
    "W  W        WWWWWWD   WW",
    "WD  W   WWDW W   W  WWWW",
    "WD  WW  WW  W W  W    WW",
    "WD  WWWW W   DWW W  W GW",
    "WWW                WWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWW",
]

def write_text(x, y, size, c , text):
    penup()
    goto(x, y)
    pendown()
    color(c)
    style = ('b tabassom', size, 'bold italic')
    write(text, font=style, align='center')

def base(x, y, length, length2, color1, fill):
    speed(0)
    pensize(5)
    penup()
    goto(x, y)
    pendown()
    color(color1)
    fillcolor(fill)
    setheading(0)
    begin_fill()
    for idk in range(2):
        forward(length)
        right(90)
        forward(length2)
        right(90)
    end_fill()

def around(x, y, size, color1, fill):
    penup()
    goto(x, y)
    pendown()
    color(color1)
    fillcolor(fill)
    begin_fill()
    circle(size)
    end_fill()
base(-440, 270, 900, 550, "black", "grey40")   #<------ base drawing
base(-400, 200, 660, 430, "black", "gray80")
around(360, -120, 30, "red4", "red3")
around(360, -240, 30, "green4", "green3")
around(300, -175, 30, "yellow4", "yellow3")
around(420, -175, 30, "blue4", "blue3")
base(330, 160, 54, 160, "gray20", "grey20")
base(280, 113, 160, 54, "gray20", "grey20")
write_text(-230, 210, 30, "black", "The Forgotten Path")
map_x= -350
map_y= 170

hideturtle()
speed(0)
walls= []
line= 20
lives= 3
damage_blocks= []


def wall(x, y):
    walls.append((x, y))
    penup()
    goto(x, y)
    
    half= line// 2
    backward(half)
    right(90)
    forward(half)
    left(90)
    
    pendown()
    color("grey")
    fillcolor("grey")
    begin_fill()
    for a in range(4):
        forward(line)
        left(90)
    end_fill()

    penup()
    goto(x, y)
    setheading(0)
player=Turtle()
player.shape("square")
player.color("lavender")
player.penup()
player.goto(0, 0)
player.shapesize(1)
screen=Screen()

goal= None
goal_pos= []
def draw_goal(x, y):
    goal_pos.append((x, y))
    win_turtle = Turtle()
    win_turtle.shape("square")
    win_turtle.shapesize(1)
    win_turtle.color("gold")
    win_turtle.penup()
    win_turtle.goto(x, y)

def win_game():
    screen.clear()
    screen.bgcolor("black")

    msg=Turtle()
    msg.hideturtle()
    msg.color("gold")
    msg.penup()
    msg.write("YOU WON!! :D" , align="center", font=("Arial", 50, "bold"))

def damage_block(x, y):
    damage_blocks.append((x, y))
    penup()
    goto(x, y)
    half = line//2
    backward(half)
    right(90)
    forward(half)
    left(90)

    pendown()
    color("red")
    fillcolor("red")
    begin_fill()
    for block in range(4):
        forward(line)
        left(90)
    end_fill()
    penup()
    goto(x, y)
    setheading(0)
    
health_painter = Turtle()
health_painter.hideturtle()
health_painter.penup()
    
def draw_hearts():
    health_painter.clear()
    health_painter.goto(250, 200)
    health_painter.color("red")
    heart_string = "<3" * lives
    health_painter.write(heart_string, align= "left", font=("Arial", 40, "bold"))
def game_over():
    screen.clear()
    screen.bgcolor("black")

    msg=Turtle()
    msg.hideturtle()
    msg.color("red")
    msg.penup()
    msg.write("YOU LOST!! :(" , align="center", font=("Arial", 50, "bold"))
    
def build_map(map_data):
    global player_col, player_row
    for row in range(len(map_data)):
        for col in range(len(map_data[row])):
            tile= map_data[row][col]
            x=col * line + map_x
            y= -row * line + map_y
            if tile == "W":
                walls.append((col, row))
                wall(x, y)
            if tile == "P":
                player_col = col
                player_row = row
                player.goto(x, y)
            if tile== "D":
                damage_blocks.append((col, row))
                damage_block(x, y)
            if tile == "G":
                goal_pos.append((col, row))
                draw_goal(x, y)
def grid(col, row):
    return (col * line + map_x, -row * line + map_y)
player_col =0
player_row =0
    
def go_up():
    global lives, player_row

    new = (player_col, player_row - 1)

    if new in walls:
        return

    player_row -= 1
    player.goto(grid(player_col, player_row))

    if new in damage_blocks:
        lives -= 1
        draw_hearts()
        if lives <= 0:
            game_over()

    if new in goal_pos:
        win_game()

def go_down():
    global lives, player_row

    new = (player_col, player_row + 1)

    if new in walls:
        return

    player_row += 1
    player.goto(grid(player_col, player_row))

    if new in damage_blocks:
        lives -= 1
        draw_hearts()
        if lives <= 0:
            game_over()

    if new in goal_pos:
        win_game()

def go_left():
    global lives, player_col

    new = (player_col - 1, player_row)

    if new in walls:
        return

    player_col -= 1
    player.goto(grid(player_col, player_row))

    if new in damage_blocks:
        lives -= 1
        draw_hearts()
        if lives <= 0:
            game_over()

    if new in goal_pos:
        win_game()
        
def go_right():
    global lives, player_col

    new = (player_col + 1, player_row)

    if new in walls:
        return

    player_col += 1
    player.goto(grid(player_col, player_row))

    if new in damage_blocks:
        lives -= 1
        draw_hearts()
        if lives <= 0:
            game_over()

    if new in goal_pos:
        win_game()

screen= Screen()
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
draw_hearts()
build_map(map1)


          
