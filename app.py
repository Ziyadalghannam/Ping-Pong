#imported turtle module 
import turtle

wind = turtle.Screen() #makes a screen 
wind.title("Ping Pong By Ziyad") #sets a title 
wind.bgcolor("black") #sets bg color
wind.setup(width=800, height=600) 
wind.tracer(0) #stops the window from updating automatically 

#bar1 
bar1 = turtle.Turtle() #initialize turtle object
bar1.shape("square") #sets shape
bar1.shapesize(stretch_wid=5, stretch_len=1) #sets shape size
bar1.color ("red") #change the line color
bar1.penup() #stops drawing lines 
bar1.goto(-350,0) #sets the position of the object 

#bar2
bar2 = turtle.Turtle()
bar2.speed(0)
bar2.shape("square")
bar2.shapesize(stretch_wid=5, stretch_len=1)
bar2.color ("blue")
bar2.penup()
bar2.goto(350,0)

#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color ("white")
ball.penup()
ball.goto(0,0)
ball.dx = -2.5
ball.dy = -2.5

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color ("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1 : 0  Player 2 :0", align= "center", font=("Courier",24,"normal"))

#functions 
    #first bar function 
def bar1_up():
    y = bar1.ycor() #sets y coord 
    y += 20 #set the y to increase by 20 
    bar1.sety(y) #set the y to the new y 

def bar1_down():
    y = bar1.ycor()
    y -= 20
    bar1.sety(y)

    #second bar function 
def bar2_up():
    y = bar2.ycor()
    y += 20
    bar2.sety(y)

def bar2_down():
    y = bar2.ycor()
    y -= 20
    bar2.sety(y)

#keyboard bindings 
wind.listen() #expects the input 
wind.onkeypress(bar1_up, "w") #when pressed function is executed 
wind.onkeypress(bar1_down, "s")
wind.onkeypress(bar2_up, "Up")
wind.onkeypress(bar2_down, "Down")


#main game loop
while True: 
    wind.update()
    
    #move ball 
    ball.setx(ball.xcor() + ball.dx) #ball starts at 0 and moves on x due to ball.dx above
    ball.sety(ball.ycor() + ball.dy) #ball starts at 0 and moves on y due to ball.dy above


    #border check 
    if ball.ycor() >290:  #if ball is above top border 
        ball.sety(290) #set ball y cords 
        ball.dy *=-1 #reverse ball direction 

    if ball.ycor() <-290: #bottom border 
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 +=1
        score.clear()
        score.write("Player 1 : {}  Player 2 :{}".format(score1, score2), align= "center", font=("Courier",24,"normal"))

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 +=1
        score.clear()
        score.write("Player 1 : {}  Player 2 :{}".format(score1, score2), align= "center", font=("Courier",24,"normal"))
    
    if (ball.xcor() > 340 and ball.xcor() <350 and ball.ycor() < bar2.ycor() + 40 and ball.ycor() > bar2.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < bar1.ycor() + 40 and ball.ycor() > bar1.ycor() -40 ):
        ball.setx(-340)
        ball.dx *= -1
   
    
