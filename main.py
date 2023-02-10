import os
import sys
import faulthandler
import platform
import cv2

# enable GPIO on ARM64 and enable debugging on x86_64
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

def diagnostic():
    return result

def show_info():
    print('-- Caramote --')
    print(f'platform: {platform.machine()}')
    print(f'python: {platform.python_version()}')
    print(f'opencv: {cv2.__version__}')

def cv_prep():
    capture = cv2.VideoCapture(0)

def count():
    while capture.isOpened():
        ret, img_input = capture.read()
        if not ret:
            # throw error and require reboot
            break

if __name__ == '__main__':
    check_platform()
    show_info()
