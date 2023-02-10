import cv2
import os

os.getcwd()

i = 1
wait = 0

video = cv2.VideoCapture(0)


def record():
    os.system(
        f"""ffmpeg -i /dev/video0 out.mp4""")


while True:
    ret, img = video.read()
    cv2.imshow('live video', img)
    key = cv2.waitKey(100)
    wait = wait + 100
    if key == ord('q'):
        break

    if key == ord('s'):
        filename = 'Frame_' + str(i) + '.jpg'
        cv2.imwrite(filename, img)
        i = i + 1
        wait = 0

    if key == ord('r'):
        record()

video.release()

cv2.destroyAllWindows()
