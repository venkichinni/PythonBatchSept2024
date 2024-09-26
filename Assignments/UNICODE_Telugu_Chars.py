"""
    telugu unicode characters
"""

# def print_telugu_chars():
#     start, end = 0x0C00, 0x0C7F  # Telugu Unicode block range
#     for codepoint in range(start, end + 1):
#         char = chr(codepoint)
#         print(char, end=" ")

# print_telugu_chars()



telugu_characters = [
    "\u0C05",  # అ (Telugu Letter A)
    "\u0C06",  # ఆ (Telugu Letter AA)
    "\u0C07",  # ఇ (Telugu Letter I)
    "\u0C08",  # ఈ (Telugu Letter II)
    "\u0C09",  # ఉ (Telugu Letter U)
    "\u0C0A",  # ఊ (Telugu Letter UU)
    "\u0C2A",  # ప (Telugu Letter PA)
    "\u0C2B",  # ఫ (Telugu Letter PHA)
    "\u0C2C",  # బ (Telugu Letter BA)
    "\u0C2D",  # భ (Telugu Letter BHA)
    "\u0C32",  # ల (Telugu Letter LA)
]

# Printing Telugu characters
for char in telugu_characters:
    print(char)