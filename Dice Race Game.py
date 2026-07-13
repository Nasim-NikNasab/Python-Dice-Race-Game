import tkinter
import turtle
import random
from tkinter import *
# ==========settings and definition players=========
# ====screen settings===============================
turtle.screensize(400,400)
turtle.title("Game")
turtle.bgcolor("grey")
turtle.colormode(255)
# =============players definitions and settings and movements==================
# start step
start_step = turtle.Turtle()
start_step.fillcolor("navy")
start_step.shape("square")
start_step.shapesize(4, 2, 2)
start_step.penup()
start_step.goto(-280, -75)
start_step.pendown()
# player1 red
player1 = turtle.Turtle()
player1.color("red")
player1.shapesize(2,2,2)
player1.penup()
player1.goto(-280,-100)
player1.pendown()

# player 2 green
player2 = turtle.Turtle()
player2.color("green")
player2.shapesize(2,2,2)
player2.penup()
player2.goto(-280,-80)
player2.pendown()

# player 3 blue
player3 = turtle.Turtle()
player3.color("blue")
player3.shapesize(2,2,2)
player3.penup()
player3.goto(-280,-60)
player3.pendown()


players_Dictionaty = {
    "red" : player1,
    "green" : player2,
    "blue" : player3,
}
current_player = None
latitude = 0
longitude = 0
def player_moves(number):
    global current_player
    # Arz goghrafia
    global latitude
    # Tool goghrafia
    global longitude
    right_wall = 320
    left_wall = -280
    counts_of_steps = 0
    for item in players_Dictionaty.keys():
        if item == Chosen_player.cget("text") :
            current_player = players_Dictionaty[item]
            current_player.penup()
            longitude = current_player.xcor()
            latitude = current_player.ycor()
            # row 1  movements
            if (current_player.ycor() <= -60 and current_player.ycor() >= -100) :
                if (longitude + number * 50) > 345.0 :
                   counts_of_steps = ((320 - longitude )// 50)
                   number = ((number-1) - counts_of_steps)
                   current_player.goto(320,latitude)
                   current_player.setheading(90)
                   current_player.forward((95))
                   current_player.setheading(180)
                   current_player.forward((number * 50))
                else :
                      current_player.forward((number * 50))
            #  row 3 movements
            elif (current_player.ycor() <= 150 and current_player.ycor() >= 55) :
                if (longitude + number * 50) == 320.0 :
                    current_player.goto(320,latitude)
                    winner_name_label.config(text=str(item))
                elif (longitude + number * 50) > 345.0 :
                       current_player.pendown()
                else :
                    current_player.setheading(0)
                    current_player.forward(number *50)
            #  row 2 movements
            elif current_player.ycor() < 55 and current_player.ycor() > -60 :
                 current_player.setheading(180)
                 if (longitude - number * 50) < -280.0 :
                   counts_of_steps = abs((-280 - longitude )// 50)
                   number = ((number-1) - counts_of_steps)
                   current_player.goto(-280,latitude)
                   current_player.setheading(90)
                   current_player.forward(95)
                   current_player.setheading(0)
                   current_player.forward((number * 50))
                 else :
                   current_player.forward((number * 50))

            current_player.pendown()
#================steps definition=======================

# other steps
steps = turtle.Turtle()
steps.fillcolor("light yellow")
steps.shape("square")
steps.shapesize(4,2,2)
steps.penup()
steps.goto(-230,-75)
steps.pendown()

# row 1
step_Counter = int(1)
for i in range(12):
    c = steps.clone()
    if step_Counter % 2 == 0:
        c.fillcolor("light blue")
    step_Counter += 1
    destinaion = 50
    c.penup()
    c.goto((-230+(destinaion* i)),-75)

    c.pendown()
# rows
current_Y = -75
for i in range(2):
    for j in range(13):
        destinaion = 50
        Y_changes = 95
        c = steps.clone()
        if i == 1 and j == 12:
            c.fillcolor("light green")
        elif step_Counter % 2 == 0:
            c.fillcolor("light blue")
        step_Counter += 1
        c.penup()
        if j == 0  :
            current_Y = Y_changes + current_Y
            c.goto((-280+(destinaion* j)),current_Y)

        else:
              c.goto((-280 + (destinaion * j)), current_Y )

        c.pendown()
        c.pendown()

# ==========play ground Frame================================================
def random_number():
    number = random.randint(1,6)
    result_label.config(text=str(number))
    turn_player_adder()
# frame
play_frame = tkinter.Frame(
    bg="gray",
    pady=15,
    padx=200,
)
play_frame.pack(side="bottom" , pady=5 , padx=5)
# ====Dice button================================
Dice = tkinter.Button(
    play_frame,
    bg="white",
    text="Dice",
    fg="black",
    padx=50,
    pady=15,
    command=random_number,

)
Dice.pack(side="left", padx=30 , pady=5 )
#=================result label==================
result_label = tkinter.Label(
    play_frame,
    bg="yellow",
    fg="black",
    padx=50,
    pady=15,

)
result_label.pack(side="right", padx=30 , pady=5)

winner_frame = tkinter.Frame(
    bg="deep sky blue",
    pady=10,
    padx=200,
)
winner_frame.pack(side="top" , pady=2 , padx=2)

winner_label = tkinter.Label(
    winner_frame,
    bg="deep sky blue",
    fg="black",
    padx=100,
    pady=10,
    text="Winner : ",
)
winner_label.pack(side="left", padx=2 , pady=2)
winner_name_label = tkinter.Label(
    winner_frame,
    bg="gold",
    fg="black",
    padx=100,
    pady=10,
)
winner_name_label.pack(side="right", padx=2 , pady=2)

# ========game actions ==================================================================================
# =========Turns================================
player1_Turns = {}
player2_Turns = {}
player3_Turns = {}
Order_of_players_after_starting =[]

Last_player = None
def turn_player_adder():
    global Last_player
    if  Chosen_player.cget("text") == "red":
        if len(player1_Turns) == 0 and int(result_label.cget("text")) == 6:
             player1_Turns[0]=6
             order_of_players_adder("red")
             player_moves(int(result_label.cget("text")))
             Last_player = "red"
        elif len(player1_Turns) > 0 :
            lastTurn = list(player1_Turns)[-1]
            player1_Turns[lastTurn+1] = result_label.getint
            player_moves(int(result_label.cget("text")))
            Last_player = "red"
    if  Chosen_player.cget("text") == "green":
        if len(player2_Turns) == 0 and int(result_label.cget("text")) == 6:
             player2_Turns[0]=6
             order_of_players_adder("green")
             player_moves(int(result_label.cget("text")))
             Last_player = "green"
        elif len(player2_Turns) > 0 :
            lastTurn = list(player2_Turns)[-1]
            player2_Turns[lastTurn+1] = result_label.getint
            player_moves(int(result_label.cget("text")))
            Last_player = "green"
    if  Chosen_player.cget("text") == "blue":
        if len(player3_Turns) == 0 and int(result_label.cget("text")) == 6:
             player3_Turns[0]=6
             order_of_players_adder("blue")
             player_moves(int(result_label.cget("text")))
             Last_player = "blue"
        elif len(player3_Turns) > 0 :
            lastTurn = list(player3_Turns)[-1]
            player3_Turns[lastTurn+1] = result_label.getint
            player_moves(int(result_label.cget("text")))
            Last_player = "blue"

def order_of_players_adder(player) :
    if len(Order_of_players_after_starting) != 3 :
        Order_of_players_after_starting.append(player)

# ========PLay frame==========================
player_frame = tkinter.Frame(
    bg="gray",
    pady=15,
    padx=200,
)
player_frame.pack(side="bottom" , pady=5 , padx=5)

Players = ["blue" , "green" , "red"]
players_copy = ["blue" , "green" , "red"]
Oreder_Of_Players_before_starting = []
def starter_player_Chooser():
    global Last_player
    if len(Order_of_players_after_starting)  < 3 :

        if len(Oreder_Of_Players_before_starting) < 3 :
            player1 = random.choice(Players)
            Oreder_Of_Players_before_starting.append(player1)
            Chosen_player.config(text=player1)
            Last_player = player1
            Players.remove(player1)

        else :
            addition_player = None
            last_player_index = Oreder_Of_Players_before_starting.index(Last_player)
            if last_player_index == 2:
                last_player_index = 0
                addition_player = Oreder_Of_Players_before_starting[last_player_index]
                Chosen_player.config(text=addition_player)

            else:
                 last_player_index = last_player_index + 1
                 addition_player = Oreder_Of_Players_before_starting[last_player_index]
                 Chosen_player.config(text=addition_player)
            Last_player = addition_player

    else :
          addition_player = None
          last_player_index = Order_of_players_after_starting.index(Last_player)
          if last_player_index == 2 :
              last_player_index = 0
              addition_player = Order_of_players_after_starting[last_player_index]
              Chosen_player.config(text = addition_player)

          else :
                  addition_player = Order_of_players_after_starting[(last_player_index)+1]
                  Chosen_player.config(text = addition_player )


turn = tkinter.Button(
    player_frame,
    bg="white",
    text="Turn :",
    fg="black",
    padx=50,
    pady=15,
    command=starter_player_Chooser,
)
turn.pack(side="left", padx=30 , pady=5 )

Chosen_player = tkinter.Label(
    player_frame,
    bg="violet",
    fg="black",
    padx=50,
    pady=15,

)
Chosen_player.pack(side="right", padx=30 , pady=5)





turtle.mainloop()