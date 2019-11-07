# a122_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random 
import leaderboard as lb 

#-----game configuration----
shape = "turtle"
size = 2
color = "darkred"
score = 0 

font_setup = ("impact", 30, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#leaderboard varibles
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name: ")

#-----initialize turtle-----
oni = trtl.Turtle(shape = shape)
oni.color(color)
oni.shapesize(size)
oni.speed(-3)

score_writer = trtl.Turtle()
score_writer.ht()
score_writer.penup()
score_writer.goto(-390, 290)
font = ("impact", 21, "normal")
score_writer.write(score, font=font)

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(294, -293)



#-----game functions--------
def turtle_clicked(x,y):  
    print("oni was clicked D:")
    change_position()
    score_counter()


def change_position():
    oni.penup()
    oni.ht()
    new_xpos = random.randint(-400, 400)
    new_ypos = random.randint(-300, 300)
    oni.goto(new_xpos, new_ypos)
    oni.st()

def score_counter():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.speed(0)
    score_writer.write(score, font=font)


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    gameover()
    counter.write("GG Go again", font=font_setup)
    timer_up = True
    manage_leaderboard() 
    
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


def gameover():
    wn.bgcolor("teal") #change the BG color

    oni.ht()
    oni.goto(100, 1400)
    counter.goto(0, 0)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global oni

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, oni, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, oni, score)



#-----events----------------
oni.onclick(turtle_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.bgcolor("lightblue")
wn.mainloop()