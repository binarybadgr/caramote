try:
    import RPi.GPIO as GPIO
    import smbus
except RuntimeError:
    print("privileges error, try with superuser")

# 16x2 LCD with i2c protocol
DEVICE_ADDR = 0x3f
DEVICE_BUS = 1
bus = smbus.SMBus(DEVICE_BUS)

# RPi GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarning(False)
GPIO.setup()


# flush and display to LCD
def display_lcd(input_data):
    display_text = str(input_data)
    bus.write_byte_data(DEVICE_ADDR, display_text, 0x01)
