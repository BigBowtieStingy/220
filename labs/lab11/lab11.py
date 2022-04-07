from graphics import Point, Rectangle, Text, GraphWin, color_rgb
from labs.lab10.button import Button
from labs.lab10.door import Door
from random import randint
"""
Alex James
lab11.py
Problem: Create a 3 door game using a Button and Door class.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def three_door_game():
    win_times = 0
    lose_times = 0
    # Create graphics for the game
    win = GraphWin("Three Door Game", 500, 500)
    wins_frame = Rectangle(Point(25, 50), Point(75, 100))
    wins_text = Text(Point(50, 25), "Wins")
    wins_count = Text(Point(50, 75), str(win_times))
    loses_frame = Rectangle(Point(100, 50), Point(150, 100))
    loses_text = Text(Point(125, 25), "Loses")
    loses_count = Text(Point(125, 75), str(lose_times))
    quit_button = Button(Rectangle(Point(425, 25), Point(475, 75)), "Quit")
    prompt_text = Text(Point(250, 125), "I have a secret door.")
    door_1 = Door(Rectangle(Point(100, 175), Point(175, 375)), "Door 1")
    door_2 = Door(Rectangle(Point(200, 175), Point(275, 375)), "Door 2")
    door_3 = Door(Rectangle(Point(300, 175), Point(375, 375)), "Door 3")
    click_prompt = Text(Point(250, 400), "Click to guess which is the secret door.")
    window_graphics = [wins_frame, wins_text, loses_frame, loses_text, quit_button, prompt_text,
                       click_prompt, wins_count, loses_count, door_1, door_2, door_3]
    door_colors = [color_rgb(145, 42, 42), color_rgb(10, 200, 50), color_rgb(225, 35, 35)]
    doors = [door_1, door_2, door_3]
    playing = True
    # Draw the graphics put into a table
    for graphic in window_graphics:
        graphic.draw(win)
    while playing:
        # Reset the doors and create a secret door
        for door in doors:
            door.color_door(door_colors[0])
        secret_door = doors[randint(0, 2)]
        # Remove the secret door from the door list
        doors.remove(secret_door)
        waiting_for_click = True
        # Second while loop that waits for the user to click one of the 3 doors or the quit button
        while waiting_for_click:
            click_point = win.getMouse()
            waiting_for_click = False
            if secret_door.is_clicked(click_point):
                win_times += 1
                prompt_text.setText("You win!")
            # Since the secret door isn't in the door list, both entries in that list are the wrong door
            elif doors[0].is_clicked(click_point):
                lose_times += 1
                prompt_text.setText("Sorry, incorrect.")
                doors[0].color_door(door_colors[2])
            elif doors[1].is_clicked(click_point):
                lose_times += 1
                prompt_text.setText("Sorry, incorrect.")
                doors[1].color_door(door_colors[2])
            elif quit_button.is_clicked(click_point):
                # If the user clicks the quit button, it will exit the while loop when it reaches top
                playing = False
            else:
                # If nothing is clicked, wait again for the user to click something
                waiting_for_click = True
            # Once a door is clicked, color the correct door green and update the win/lose counters
            if not waiting_for_click and playing:
                click_prompt.setText("Click anywhere to play again.")
                wins_count.setText(str(win_times))
                loses_count.setText(str(lose_times))
                secret_door.color_door(door_colors[1])
                # Add the secret door back to the door list
                doors.append(secret_door)
                win.getMouse()
                # Reset text after the user clicks the screen again
                click_prompt.setText("Click to guess which is the secret door.")
                prompt_text.setText("I have a secret door.")
    win.close()
