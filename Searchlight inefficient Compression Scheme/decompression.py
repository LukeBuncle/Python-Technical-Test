"""
This script decompresses text that was compressed by replacing characters with hex values.
The script uses a key stored in a JSON file to map the hex values back to their original characters.
"""
import json

# Read the compressed text from a text file
with open("compressed_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Read the JSON file holding the key dictionary
with open("key.json", "r", encoding="utf-8") as file:
    key = json.load(file)


# Reverse the dictionary
value_dict = {hex_value: character for character, hex_value in key.items()}

# Initialise the hex value list and the string which holds the current segment
hex_values = []
current_segment = ""

# Split the compressed text into a list of hex values
for char in text:
    current_segment += char
    if char != "f":
        hex_values.append(current_segment)
        current_segment = ""

# Append the last segment if it exists (which it shouldn't)
if current_segment:
    hex_values.append(current_segment)

# Initialise the output text string
new_text = ""

# Replace every hex value in the input text with its corresponding character
for char in hex_values:
    new_text += value_dict[char]

# Print the output text
print(new_text)
