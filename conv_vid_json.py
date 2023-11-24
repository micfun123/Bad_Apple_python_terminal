import cv2 as cv
import numpy as np
import json 

def convert_video_to_json(video_file, json_output):
    colour = {1: ' █', 0: ' '}

    with open(json_output, 'w') as jsonfile:
        jsonfile.write('[')

        cap = cv.VideoCapture(video_file)

        ret, frame = cap.read()
        while ret:
            # Convert frame to grayscale, resize, normalize, and round values
            frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            frame = cv.resize(frame, (80, 60))
            frame = frame / 255
            frame = np.round(frame)
            frame = frame.astype(int)
            frame = frame.tolist()

            jsonfile.write(json.dumps(frame))

            ret, frame = cap.read()
            if ret:
                jsonfile.write(',\n')

        jsonfile.write(']')

        cap.release()
        cv.destroyAllWindows()

# Usage: Replace 'bad_apple.mp4' and 'bad_apple.json' with your desired input and output file paths
convert_video_to_json('bad_apple.mp4', 'bad_apple.json')
