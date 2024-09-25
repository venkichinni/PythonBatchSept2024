"""
    telugu unicode characters
"""

def print_telugu_chars():
    start, end = 0x0C00, 0x0C7F  # Telugu Unicode block range
    for codepoint in range(start, end + 1):
        char = chr(codepoint)
        print(char, end=" ")

print_telugu_chars()
