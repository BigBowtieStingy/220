from graphics import Point, GraphWin, Text, Polygon
import time

"""
Alex James
lab4.py
Problem: Create a valentine's day greeting card.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def greeting_card():
    card = GraphWin("Greeting_Card", 700, 700)
    card.setCoords(0, 0, 10, 10)
    # left lobe of heart
    ll1 = Point(0, 8)
    ll2 = Point(1, 9.5)
    ll3 = Point(3, 9.5)
    ll4 = Point(4, 9)
    ll5 = Point (5, 7)
    # right lobe of heart
    rl1 = Point(5, 7)
    rl2 = Point(6, 9)
    rl3 = Point(7, 9.5)
    rl4 = Point(9, 9.5)
    rl5 = Point(10, 8)
    # bottom curve
    bc1 = Point(9.5, 6)
    bc2 = Point(5, .5)
    bc3 = Point(.5, 6)
    heart = Polygon(ll1, ll2, ll3, ll4, ll5, rl1, rl2, rl3, rl4, rl5, rl5, bc1, bc2, bc3)
    heart.setFill("Red")
    heart.setWidth(5)
    heart.draw(card)
    # Create Text
    card_message = Text(Point(5, 5), "Happy Valentine’s Day!")
    card_message.setTextColor("White")
    card_message.setSize(25)
    card_message.draw(card)
    # Create Arrow Tip
    arwtip1 = Point(2, 2)
    arwtip2 = Point(1, 2)
    arwtip3 = Point(2, 1)
    arrow_tip = Polygon(arwtip1, arwtip2, arwtip3)
    arrow_tip.draw(card)
    arrow_tip.setFill("Gray")
    # Create Arrow Shaft
    arwshft1 = Point(0, 0)
    arwshft2 = Point(1.5, 1.5)
    arwshft3 = Point(1.5, 1.5)
    arrow_shaft = Polygon(arwshft1, arwshft2, arwshft3)
    arrow_shaft.draw(card)
    # Move arrow
    for i in range(0, 75, 1):
        arrow_shaft.move(i * .015, i * .015)
        arrow_tip.move(i * .015, i * .015)
        time.sleep(.05)
    # Close card when arrow finishes
    card_message.setText("Click to Close")
    card.getMouse()
    card.close()


greeting_card()