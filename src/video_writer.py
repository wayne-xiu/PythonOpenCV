import sys
import numpy as np
import cv2 as cv

def main():
    frame_size = (320, 240)
    fps = 25
    fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')

    writer = cv.VideoWriter('data/output.avi', fourcc, fps, frame_size)
    if writer.isOpened() is False:
        print('Error creating video writer.')
        sys.exit(1)
    for i in range(0, 100):
        im = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)
        cv.putText(im, str(i), (int(frame_size[0]/3), int(frame_size[1]*2/3)), 
                   cv.FONT_HERSHEY_SIMPLEX, 3.0, (255, 255, 255), 3)
        writer.write(im)
    writer.release()

if __name__ == '__main__':
    main()