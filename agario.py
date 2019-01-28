from turtle import*
import turtle
import time
import random
import math
from ball import Ball

turtle.colormode(1)

turtle.tracer(0)
turtle.hideturtle()
running = True
screen_width= turtle.getcanvas().winfo_width()/2
screen_height= turtle.getcanvas().winfo_height()/2
my_ball=Ball(100,50,3,3,50,"red")
number_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5

Balls=[]

for i in range(number_of_balls):
	x=random.randint(-screen_width+maximum_ball_radius,screen_width-maximum_ball_radius)
	y=random.randint(-screen_height + maximum_ball_radius, 
	screen_height - maximum_ball_radius)
	dx=random.randint( minimum_ball_dx, maximum_ball_dx)
	dy=random.randint( minimum_ball_dy, maximum_ball_dy)
	r=random.randint(minimum_ball_radius , maximum_ball_radius)
	color=random.random(), random.random(), random.random()
	ball1 = Ball(x,y,dx,dy,r,color)
	Balls.append(ball1)



def move_all_balls():
	for j in Balls:
		j.move(screen_width,screen_height)

def collide(ball_a,ball_b):
	if (ball_a == ball_b):
		return False
	distance = math.sqrt(math.pow(ball_b.pos()[0]-ball_a.pos()[0],2)+math.pow(ball_a.pos()[1]-ball_b.pos()[1],2))
        if (distance<=ball_a.r+ball_b.r):
             return True
        else:
			return False

def check_all_balls_collisions():
	global running
	all_balls=[]
	all_balls.append(my_ball)
	for ball in Balls:
		all_balls.append(ball)

	for ball_a in all_balls:
		for ball_b in all_balls:
			if collide(ball_a,ball_b):
				r1=ball_a.r
				r2=ball_b.r
				x=random.randint(-screen_width+maximum_ball_radius,screen_width-maximum_ball_radius)
				y=random.randint(-screen_height + maximum_ball_radius, 
				screen_height - maximum_ball_radius)
				dx=0
				while(dx == 0):
					dx=random.randint( minimum_ball_dx, maximum_ball_dx)
				dy=0
				while(dy==0):
					dy=random.randint( minimum_ball_dy, maximum_ball_dy)

				r=random.randint(minimum_ball_radius , maximum_ball_radius)
				color= (random.random(), random.random(), random.random())
				if r1 < r2:
					small_ball = ball_a
					big_ball = ball_b
				else:
					small_ball = ball_b
					big_ball = ball_a

				if my_ball==small_ball:
					turtle.write("F",move=False,align="center",font=("Arial",150,"normal"))
					running=False
				small_ball.new_Ball(x, y, dx,dy,r,color)
				big_ball.r+=4
				big_ball.shapesize(big_ball.r/10)
				if small_ball== my_ball:
					running = False



def movearound():
	my_ball.goto(turtle.getcanvas().winfo_pointerx() - screen_width*2 , 1.4*screen_height - turtle.getcanvas().winfo_pointery())

while running == True :
	screen_width= turtle.getcanvas().winfo_width()/2
	screen_height= turtle.getcanvas().winfo_height()/2

	movearound() 
	move_all_balls()
	check_all_balls_collisions()
	turtle.update()
	time.sleep(.1)

turtle.mainloop() 


        

















