import os
import sys
import faulthandler
import platform
import sqlite3
import datetime
import cv2

# enable GPIO on ARM64 and enable debugging on x86_64
# no *BSD support yet, since no `libgpio` wrapper for python
def check_platform():
    if platform.machine() == 'ARM64':
        import RPi.GPIO as GPIO
        import time
        # Define GPIO to LCD mapping
        LCD_RS = 7
        LCD_E  = 8
        LCD_D4 = 25
        LCD_D5 = 24
        LCD_D6 = 23
        LCD_D7 = 18
    elif platform.machine() == '' or platform.machine() == 'x86_64':
        import pdb

# create or connect exist db
def db_setup():
    bucket = sqlite3.connect('bucket.db')
    cursor = bucket.cursor()
    cursor.execute('CREATE TABLE img_bucket(id string, img blob)')
    bucket.commit()

def write_db(result_image):
    bucket = sqlite3.connect('bucket.db')
    bucket.execute('INSERT INTO img_bucket VALUE(?,?)',
                   ('pattern', sqlite3.Binary(result_image)))


def diagnostic():
    return result

def show_info():
    print('-- Caramote --')
    print(f'platform: {platform.machine()}')
    print(f'python: {platform.python_version()}')
    print(f'opencv: {cv2.__version__}')

def count():
    capture = cv2.VideoCapture(0)
    while capture.isOpened():
        ret, img_input = capture.read()
        if not ret:
            # throw error and require reboot
            break
        gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 2)
        #blur = cv2.bilateralFilter(blur, 9, 15, 15)
        gray = back_sub.apply(cv2.GaussianBlur(gray, (5, 5), 2))
        canny = cv2.Canny(gray, 10, 20)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, hierarachy = cv2.findContours(thresh, cv2.RETR_TREE,
                                                cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            print(len(contours))
            if len(contours) > 1: cv2.waitKey(-1)
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            area = cv2.contourArea(c)
            x, y, w, h = cv2.boundingRect(c)
            cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
            cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
            cv2.putText(img, f'[Development]', (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1,
                        (0, 255, 0), 1)
            cv2.putText(img, datetime.datetime.now().strftime('%H:%M:%S - %m/%d/%Y'),
                        (50, 100), cv2.FONT_HERSHEY_DUPLEX, 1,
                        (0, 255, 0), 1)
            # difference between frame
            try:
                curr_val = len(contours)
                delta += curr_val - prev_val
                total += delta
                prev_val = curr_val
                cv2.putText(img, f'computer see: {total//4}', (50, 150),
                            cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 1)
            except TypeError:
                cv2.putText(img, f'computer see: {total//4}', (50, 150),
                            cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 1)

        # debugging
        if DEBUG:
            cv2.imshow('out', img)
        else:
            write_db(img)
        if cv2.waitKey(1) == ord('r'):
            curr_val = prev_val = delta = total = 0
        elif cv2.waitKey(1) == ord('q'):
            cv2.GaussianBlur(gray, (5, 5), 2)
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    check_platform()
    show_info()
    count()
