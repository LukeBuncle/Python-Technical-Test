"""
This script reads a text file, counts the frequency of each character, and assigns a unique hex
value to each character based on its frequency. It then replaces each character in the text with
its corresponding hex value to generate a compressed version of the text. The compressed text
and the dictionary mapping characters to hex values (used as a key for decompression) are saved
to separate files.
"""

from collections import Counter
import json

# Read the input text from a text file
with open("a_christmas_carol.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Replace new lines with spaces
text = content.replace("\n", " ")

# Count the number of times each character appears and order them based on frequency
character_count = sorted(Counter(text).items(), key=lambda x: x[1], reverse=True)

# Initialise hex value dictionary
value_dict = {}

# Based on frequency, pair each unique character with a hex value and add the pair to a dictionary
for i, (character, count) in enumerate(character_count):
    hex_string = ""
    quotient, remainder = divmod(i, 15)

    for j in range(quotient):
        hex_string += "f"

    hex_string += hex(remainder)[2:]

    value_dict[character] = hex_string

# Initialise the output text string
new_text = ""

# Replace every character in the input text with its corresponding hex value
for char in text:
    new_text += value_dict[char]

# Print the output text
print(new_text)

# Store the output text
with open("compressed_text.txt", "w", encoding="utf-8") as file:
    file.write(new_text)

# Store the hex value dictionary to be used as a key when decompressing
with open("key.json", "w", encoding="utf-8") as file:
    json.dump(value_dict, file)
