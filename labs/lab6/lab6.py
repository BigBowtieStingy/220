from graphics import GraphWin, Point, Rectangle, Entry, Text

"""
Alex James
lab6.py
Problem: Create a Vigenere Chiper using Python
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def vigenere():
    # Draw text and encoding button:
    win = GraphWin('Vigenere', 500, 500)
    ask_to_encode = Text(Point(100,100), "Message to Encode:")
    ask_for_key = Text(Point(100, 250), "Enter Keyword:")
    ask_to_encode.draw(win)
    ask_for_key.draw(win)
    encode_entry = Entry(Point(300, 100), 20)
    key_entry = Entry(Point(300, 250), 20)
    encode_entry.draw(win)
    key_entry.draw(win)
    encode_button = Rectangle(Point(200, 375), Point(300, 425))
    encode_button.draw(win)
    encode_button_text = Text(Point(250, 400), "Encode!")
    encode_button_text.draw(win)
    win.getMouse()
    # Get message and key after user inputs them:
    message = encode_entry.getText()
    key = key_entry.getText()
    # Make button vanish
    encode_button.undraw()

    # Remove Spaces from message and key

    message.strip()
    new_message = message.split(" ")
    message = ""
    for word in new_message:
        message = message + word

    key.strip()
    new_key = key.split(" ")
    key = ""
    for word in new_key:
        key = key + word

    # Change message and key to upper
    message = message.upper()
    key = key.upper()

    # Begin looping through each letter to encrypt it
    key_start = 0
    key_length = len(key)
    encrypted_message = ""
    for letter in message:
        # Get both the encrypted letter and key
        encrypted_letter = ord(letter) - 65
        encrypted_key = ord(key[key_start]) - 65
        # Update the key loop
        key_start = key_start + 1
        key_start = (key_start % key_length)
        # Add the characters together and put results into message
        encrypted_total = (encrypted_letter + encrypted_key) % 26
        encrypted_message = encrypted_message + chr(encrypted_total + 65)

    # Display new message and ask user to close window
    encode_button_text.setText(encrypted_message)
    encoded_message_header = Text(Point(250, 375), "Resulting Message:")
    click_to_close_message = Text(Point(250, 450), "Click Anywhere to Close")
    encoded_message_header.draw(win)
    click_to_close_message.draw(win)
    win.getMouse()
    win.close()


vigenere()