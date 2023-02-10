import os
import platform
import cv2

def check_platform():
    if platform.machine() == 'arm':
        import gpio
    elif platform.machine() == '' or platform.machine() == 'x86_64':
        print('testing mode')

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
