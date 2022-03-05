def encode(message, key):
    # Convert each character into a number, add the key, and turn it back into a character
    encrypted_message = ""
    for character in message:
        character = ord(character) + key
        encrypted_message = encrypted_message + chr(character)
    return encrypted_message


def encode_better(message, key):
    key_length = len(key)
    key_start = 0
    encrypted_message = ""
    for letter in message:
        # Get both the encrypted letter and key, subtract by 65 to line them up with range
        encrypted_letter = ord(letter) - 65
        encrypted_key = ord(key[key_start]) - 65
        # Update the key loop
        key_start = key_start + 1
        # Restart key loop if it reaches its end
        key_start = (key_start % key_length)
        # Add the characters together and put results into message
        encrypted_total = (encrypted_letter + encrypted_key) % 58
        encrypted_message = encrypted_message + chr(encrypted_total + 65)
    return encrypted_message
