import json
import sys
import time

colour = {
    1: '█',
    0: ' '
}

jsonfile = open('rick.json', 'r')
frames = json.loads(jsonfile.read())
jsonfile.close()

# Determine terminal height and adjust the number of empty lines
# to hide the control characters from the top and bottom
terminal_height = 25  # Change this according to your terminal height
empty_lines = int((terminal_height - len(frames[0])) / 2)

# Generate empty lines to hide the top control characters
top_lines = '\n' * empty_lines

for frame in frames:
    output = ''
    for row in frame:
        for pixel in row:
            output += colour[pixel]
        output += '\n'

    # Generate empty lines to hide the bottom control characters
    bottom_lines = '\n' * (terminal_height - len(frames[0]) - empty_lines)

    # Print the frame with top and bottom empty lines
    sys.stdout.write(top_lines)
    sys.stdout.write(output)
    sys.stdout.write(bottom_lines)
    sys.stdout.flush()

    time.sleep(0.03)  # Adjust the delay between frames (in seconds)
