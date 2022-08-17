from time import sleep
from turtle import Turtle, Screen
import random

import tkinter as tk
from tkinter import simpledialog, messagebox

red_t = Turtle()
green_t = Turtle()
blue_t = Turtle()
pink_t = Turtle()
goal = Turtle()
screen = Screen()
screen.setup(width=.75, height=0.80, startx=None, starty=None)
turtles = [red_t, green_t, blue_t, pink_t]
turtle_colors = ["red", "green", "blue", "pink"]
position_start = [400, 200, 0, -200]


def start_of_race():
    """Aligns Turtles for Start of Race"""
    start = 400

    for num, turtle in enumerate(turtles):
        turtle.color(turtle_colors[num])
        turtle.shape("turtle")
        turtle.shapesize(2, 2, 1)
        turtle.penup()

        turtle.goto(-600, start)
        start -= 200


def race():
    """Determines the Winner of The Race and Returns Winner"""
    global winning_turtle
    finish_line = True
    while finish_line:
        for start, turtle in enumerate(turtles):
            if turtle.pos() >= (500, position_start[start]):
                winning_turtle = turtles[start]
                winning_turtle = turtle.color()[0]
                return winning_turtle

            turtle.forward(random.choice(range(0, 101, 10)))


def goal_line():
    """Draws the Finish Line for the Race"""
    goal.hideturtle()
    goal.shape("classic")
    goal.penup()
    goal.goto(500, 500)
    goal.pendown()
    goal.goto(500, -500)
    goal.penup()


# Main Function
def main():
    """Main function for the Turtle Race"""
    goal_line()
    start_of_race()
    race()


ROOT = tk.Tk()
# ROOT.geometry("2000x1000")
ROOT.withdraw()

# the input dialog to pick a turtle
selecting_turtle = True
while selecting_turtle:
    try:
        user_choice = simpledialog.askstring(title="Start of Race",
                                             prompt="Who do you think will win the 'Turtle Race'?"
                                                    "\n- Red\n- Blue\n- Green\n- Pink").lower().strip()
        if user_choice in turtle_colors:
            selecting_turtle = False
        else:
            messagebox.showwarning("No Racer.", "That's not a color selection.")
    except KeyError:
        messagebox.showerror("Incorrect Selection", "That's not a selection.")
    except AttributeError:
        messagebox.showinfo("Exiting Game.", "Goodbye...")
        sleep(1)
        exit()

# Winner of Race Variable
winning_turtle = ""

# Starts Program
main()

# Gives the user the results of the Race
if winning_turtle.lower() == user_choice:
    winner = tk.messagebox.showinfo("Results", f"The Winner is the {winning_turtle.title()} Turtle! You Won! :)")
else:
    winner = tk.messagebox.showinfo("Results", f"The Winner is the {winning_turtle.title()} Turtle! You Lost.. :(")

# screen.screensize(1000, 600)
screen.exitonclick()
