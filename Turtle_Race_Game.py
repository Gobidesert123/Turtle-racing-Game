from turtle import Turtle, Screen
import random

# creating objects/ setting the screen up / Creating variables that hold values.
screen = Screen()
screen.setup(width=500, height=400)
# The user gets to place a bet on which color turtle will win the race.
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'gold', 'blue', 'purple', 'violet']
location_y = [-100, -60, -20, 20, 60, 100]
next_turtle = []
race_on = True

'''
This uses the above y axis locations to have the turtles start at specific locations 
on the start line. 
'''
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x = -230, y = location_y[i])
    next_turtle.append(new_turtle)


while race_on:
    for turt in next_turtle:
        if turt.xcor() >= 230:
            winner = turt.pencolor()
            # checking if the winner has chosen correctly
            if winner == user_bet:
                print(f'You won the race!, Winner: {winner}!') # This returns the color that won
            else:
                print(f'You lost the race!, Winner: {winner}! ') # This returns the color that won
            # The while loop ends
            race_on = False
            # This is to break out of for loop and not do next lines of code.
            break
        distance = random.randint(5, 10)
        turt.forward(distance)

screen.exitonclick()