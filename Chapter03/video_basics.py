#REVERSING A VIDEO FILE

import cv2



capture = cv2.VideoCapture("resources/dog.mp4")

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)

frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

fps = capture.get(cv2.CAP_PROP_FPS)

fourCC = capture.get(cv2.CAP_PROP_FOURCC)

last_frame = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1
print(fps)
print(fourCC)

def decode_fourcc_from_float(fourcc_float):
    # Convert the floating-point number to an integer
    fourcc_int = int(fourcc_float)
    
    # Convert the integer to a 4-character string
    fourcc_str = ''.join([chr((fourcc_int >> 8 * i) & 0xFF) for i in range(4)])
    
    return fourcc_str


codec= decode_fourcc_from_float(fourCC)

test = [*codec]
print(test)

fourcc = cv2.VideoWriter_fourcc(*codec)

out = cv2.VideoWriter("Chapter03/output.mov", fourcc, fps, (int(frame_width), int(frame_height)), True)

if not capture.isOpened():
    print("Error: Could not open video file or camera.")
else:
    print("Video file or camera opened successfully.")


current_frame = last_frame

while current_frame >=0:

    capture.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
    ret, frame = capture.read()
    current_frame -= 1
    if not ret:
        break  # Exit loop if no more frames or error



    #frame[0:50,0:200] = [255,0,0]
    
    cv2.imshow('Frame', frame)
    
    out.write(frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


capture.release()
out.release()
cv2.destroyAllWindows()