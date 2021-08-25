# Her Code Camp Mentorship programm
# Smarties Group Project - game
# 2021 August 12th ~ August 25th

# Imports turtle library
import turtle

#Imports the random module
import random

#import time module
import time 

# Imports the audio
from replit import audio

scene = 1

while True:

  #  Assign the turtle to a variable, "t". 
  t = turtle.Turtle()

  # Makes the turtle an arrow shape.
  t.shape('arrow')

  # Changes speed of the turtle
  t.speed(0)

  # Changes the background of the screen.
  background = t.getscreen()
  background.bgcolor("sky blue")

  t.speed(0)
  t.hideturtle()
  t.speed(0)
  t.up()
  t.hideturtle()
  # Grass
  t.penup()
  t.goto(-400,-100)
  t.pendown()
  t.color("lime green")
  t.begin_fill()
  for i in range(2): 
    t.forward(800)
    t.right(90)
    t.forward(400)
    t.right(90)
  t.end_fill()

  # Left Mountain
  t.penup()
  t.goto(-400, -100)
  t.pendown()
  t.color("dim gray")
  t.begin_fill()
  for i in range(3):
    t.forward(300)
    t.left(120)
  t.end_fill()

  # Right Mountain
  t.penup()
  t.goto(100, -100)
  t.pendown()
  t.begin_fill()
  for i in range(3):
    t.forward(300)
    t.left(120)
  t.end_fill()

  # Middle Mountain
  t.penup()
  t.goto(-160, -100)
  t.pendown()
  t.color("gray")
  t.begin_fill()
  for i in range(3):
    t.forward(400)
    t.left(120)
  t.end_fill()

  # Middle Mountain Ice cap
  t.penup()
  t.goto(-35,120)
  t.pendown()
  t.color("White")
  t.begin_fill()
  t.left(35)
  t.forward(60)
  t.right(90)
  t.forward(30)
  t.left(100)
  t.forward(45)
  t.right(85)
  t.forward(65)
  t.left(160)
  t.forward(150)
  t.end_fill()

  # Left Mountain Ice Cap
  t.penup()
  t.goto(-215, 100)
  t.pendown()
  t.color("snow")
  t.begin_fill()
  t.forward(70)
  t.left(120)
  t.forward(75)
  t.left(150)
  t.forward(45)
  t.right(90)
  t.forward(45)
  t.left(120)
  t.end_fill()

  # Right Mountain Ice Cap
  t.penup()
  t.goto(203, 80)
  t.pendown()
  t.begin_fill()
  t.forward(95)
  t.right(120)
  t.forward(80)
  t.right(150)
  t.forward(50)
  t.left(70)
  t.end_fill()
  t.left(50)

  # Tree
  def tree():
    # Tree trunk
    t.color("saddlebrown")
    t.begin_fill()
    for i in range(2):
      t.forward(40)
      t.left(90)
      t.forward(10)
      t.left(90)
    t.end_fill()
    
    # Turn the turtle around
    t.forward(10)
    t.left(90)
    t.forward(5)
    
    # Leaves on tree
    t.color("forestgreen")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.right(90)

  # Plant the first tree
  t.penup()
  t.goto(-25,-200)
  t.pendown()
  tree()
      
  # Plant the second tree
  t.penup()
  t.goto(200,-150)
  t.pendown()
  tree()

  # Plant the third tree
  t.penup()
  t.goto(300,-250)
  t.pendown()
  tree()

  # Plant the fourth tree
  t.penup()
  t.goto(-300,-250)
  t.pendown()
  tree()

  # Plant the fifth tree
  t.penup()
  t.goto(-200,-100)
  t.pendown()
  tree()

  # first page
  if scene == 1:
    begin = turtle.Turtle()
    begin.hideturtle()
    begin.penup()
    begin.goto(15,30)
    begin.color("orange")
    begin.write("SpongeBob Food Rush",align = "center", font = ("Times New Roman", 20,"bold"))

    begin.goto(15, 0)
    begin.write("By: Cathay & Maleeha",align = "center", font = ("Times New Roman", 10,"bold"))

    begin.goto(15, -40)
    begin.color("black")
    begin.write("Please press the \"enter\" key to play.",align = "center", font = ("Times New Roman", 10,"bold"))

    #goto scene 2
    text = input("Please press the \"enter\" key to play.")  
    if scene == 1 and text == "":
      begin.clear()
      scene = 2
  
    
  # second page (instructions)
  if scene == 2: 
    instructions = turtle.Screen()
    instructions.addshape("Instructions.gif")

    instructpage = turtle.Turtle()
    instructpage.speed(0)
    instructpage.shape("Instructions.gif")
    instructpage.penup()
    instructpage.goto(0,0)
    
    text = input("Please press the \"enter\" key to continue.")  
    if scene ==2 and text == "": 
      play_music = False
      begin.clear()
      scene = 3

    
  #third page / game
  if scene == 3:
    # clean the screen
    begin.clear()
    instructpage.hideturtle()

    #timer
    timer = turtle.Turtle()
    start = time.time()

    # Displays rounded rectangles
    rectangle = turtle.Turtle()
    rectangle.speed(0)
    rectangle.hideturtle()
    rectangle.speed(0)
    rectangle.up()
    rectangle.hideturtle()

    def round_rectangle(color,center_x,center_y,width,height,cornersize):
      rectangle.color("white",color)
      rectangle.begin_fill()
      rectangle.up()
      rectangle.goto(center_x-width/2+cornersize,center_y-height/2)
      rectangle.down()
      for _ in range(2):
        rectangle.fd(width-2*cornersize)
        rectangle.circle(cornersize,90)
        rectangle.fd(height-2*cornersize)
        rectangle.circle(cornersize,90)
      rectangle.end_fill()

    round_rectangle("deep sky blue",-125,130,150,60,10) 
    round_rectangle("orange red",180,130,150,60,10) 
    score = 0
    lives = 3

    # Create a variable 'screen', a Screen() object, that will handle keys.
    wn = turtle.Screen()
    wn.title("Spongebob Food Rush")
    wn.tracer(0)

    # Sets the shape of a turtle (Spongebob)and translates it to the grass area.
    wn.addshape("funspongebob1.gif")
    wn.addshape("hamburger.gif")
    wn.addshape("fries.gif")
    wn.addshape("sundae.gif")
    wn.addshape("bomb.gif")

    # Add the player: Spongebob
    spongebob = turtle.Turtle()
    spongebob.speed(0)
    spongebob.shape("funspongebob1.gif")
    spongebob.penup()
    spongebob.goto(5,-120)

    # Defines how fast Spongebob moves right and left.
    move_speed = 30

    # These definitions control the movement of Spongebob.
    def forward():
      spongebob.forward(move_speed)

    def backward():
      spongebob.backward(move_speed)

    spongebob.penup()
    spongebob.speed(0)
    
    # Associates the defintions from above with the right and left arrow keys on the keyboard.
    wn.onkey(forward, "Right")
    wn.onkey(backward, "Left")
    wn.listen()

    # Create a list of hamburgers
    hamburgers = []

    # Add the hamburger
    for i in range(5):
      hamburger = turtle.Turtle()
      hamburger.speed(0)
      hamburger.shape("hamburger.gif")
      hamburger.penup()
      hamburger.goto(-100,300)
      hamburger.speed = random.randint(2,4)
      hamburgers.append(hamburger)

    # Create a list of fries packs
    fries_pack = []

    # Add the fries
    for i in range(4):
      fries = turtle.Turtle()
      fries.speed(0)
      fries.shape("fries.gif")
      fries.penup()
      fries.goto(100,300)
      fries.speed = random.randint(2,4)
      fries_pack.append(fries)

    # Create a list of sundaes
    sundaes = []

    # Add the sundae
    for i in range(1):
      sundae = turtle.Turtle()
      sundae.speed(0)
      sundae.shape("sundae.gif")
      sundae.penup()
      sundae.goto(0,300)
      sundae.speed = random.randint(2,4)
      sundaes.append(sundae)

    # Create a list of bombs
    bombs = []

    # Add the bomb
    for i in range(2):
      bomb = turtle.Turtle()
      bomb.speed(0)
      bomb.shape("bomb.gif")
      bomb.penup()
      bomb.goto(25,300)
      bomb.speed = random.randint(2,4)
      bombs.append(bomb)

    # Make the pen (score text)
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.goto(15,120)
    pen.write(f'{"Score: {}":<23} {"Lives: {}":>20}'.format(score, lives), align = "center",font = ("Arial",15, "bold"))

    # Adds the countdown text
    pen2 = turtle.Turtle()
    pen2.hideturtle()
    pen2.speed(0)
    pen2.color("white")
    pen2.penup()
    pen2.goto(35,65)
    pen2.write("Countdown:", align = "center",font = ("Arial",17, "bold"))

    n = 0
    # Game loop 
    while True: 
      # Updates the screen
      wn.update()

      # Moves the hamburgers
      for hamburger in hamburgers:
        y = hamburger.ycor()
        y-= hamburger.speed
        hamburger.sety(y)

        if y <-300:
          x = random.randint(-380,380)
          y = random.randint(300,400)
          hamburger.goto(x,y)

        # Detects the collision
        if hamburger.distance(spongebob) <30: 
          source = audio.play_file("smallhit.wav")
          x = random.randint(-380,380)
          y = random.randint(300,400)
          hamburger.goto(x,y)
          score += 3
          pen.clear()
          pen.write(f'{"Score: {}":<23} {"Lives: {}":>20}'.format(score, lives), align = "center",font = ("Arial",15, "bold"))

      # Moves the fries
      for fries in fries_pack:
        y = fries.ycor()
        y-= fries.speed
        fries.sety(y)

        if y <-300:
          x = random.randint(-380,380)
          y = random.randint(300,400)
          fries.goto(x,y)

        # Detects the collision
        if fries.distance(spongebob) <30: 
          source = audio.play_file("smallhit.wav") 
          x = random.randint(-380,380)
          y = random.randint(300,400)
          fries.goto(x,y)
          score += 5
          pen.clear()
          pen.write(f'{"Score: {}":<23} {"Lives: {}":>20}'.format(score, lives), align = "center",font = ("Arial",15, "bold"))

      # Moves the sundaes
      for sundae in sundaes:
        y = sundae.ycor()
        y-= sundae.speed
        sundae.sety(y)

        if y <-300:
          x = random.randint(-380,380)
          y = random.randint(300,400)
          sundae.goto(x,y)

        # Detects the collision
        if sundae.distance(spongebob) <30: 
          source = audio.play_file("extrabonus.wav")
          x = random.randint(-380,380)
          y = random.randint(300,400)
          sundae.goto(x,y)
          n += 6
          pen.clear()
          pen.write(f'{"Score: {}":<23} {"Lives: {}":>20}'.format(score, lives), align = "center",font = ("Arial",15, "bold"))

      # Moves the bombs
      for bomb in bombs:
        y = bomb.ycor()
        y-= bomb.speed
        bomb.sety(y)

        if y <-300:
          x = random.randint(-380,380)
          y = random.randint(300,400)
          bomb.goto(x,y)

        # Detects the collision
        if bomb.distance(spongebob) <30:  
          source = audio.play_file("Explosion.wav")
          x = random.randint(-380,380)
          y = random.randint(300,400)
          bomb.goto(x,y)
          score -= 4
          lives -= 1
          pen.clear()
          pen.write(f'{"Score: {}":<23} {"Lives: {}":>20}'.format(score, lives), align = "center",font = ("Arial",15, "bold"))


        # Display the timer
      timer.hideturtle()
      timer.goto(0,0)
      timer.color("white")
      timer.clear()
      time1 =int(time.time() - start)
      time2 =(30+n) - time1
      timer.write(time2, align = "left", font = ("Arial",30, "bold"))
        
      #goto page 4
      if scene == 3 and lives == 0:
        scene = 4
        break
        
      #goto page 5
      if scene == 3 and time2 <= 0:
        scene = 5
        break

  # page 4
  if scene == 4:
    
    # clear the screen
    wn.clear()
    pen.clear
    source = audio.play_file("playerlose.wav")
    youlose = turtle.Screen()
    youlose.addshape("YouLose.gif")

    youlose = turtle.Turtle()
    youlose.speed(0)
    youlose.shape("YouLose.gif")
    youlose.penup()
    youlose.goto(0,0)


    begin.color("white")
    begin.penup()
    begin.goto(-200,-10)
    begin.write("Final Score: {}".format(score), font = ("Arial", 10,"bold"))

    begin.goto(-200,-60)
    begin.write("Remaining lives: {}".format(lives), font = ("Arial", 10,"bold"))

    begin.goto(-200,-110)
    begin.write("Game Time: {}s".format(time2), font = ("Arial", 10,"bold"))
  
    #replay the game
    text = input("Please press the \"enter\" key to play again.")  
    if scene == 4 and text == "":
      scene = 3
      wn.clear()
  

  # page 5
  if scene == 5:
    
    # clear the screen
    wn.clear()
    pen.clear()

    source = audio.play_file("smallcrowd.wav")
    youwin = turtle.Screen()
    youwin.addshape("YouWin.gif")

    youwin = turtle.Turtle()
    youwin.speed(0)
    youwin.shape("YouWin.gif")
    youwin.penup()
    youwin.goto(0,0)


    begin.color("white")
    begin.penup()
    begin.goto(-200,-10)
    begin.write("Final Score: {}".format(score), font = ("Arial", 10,"bold"))
  
    begin.goto(-200,-60)
    begin.write("Remaining lives: {}".format(lives), font = ("Arial", 10,"bold"))

    begin.goto(-200,-110)
    begin.write("Game Time: {}s".format(time2), font = ("Arial", 10,"bold"))

    #replay the game
    text = input("Please press the \"enter\" key to play again.")  
    if scene == 5 and text == "":
      scene = 3
      wn.clear()

wn.mainloop()

