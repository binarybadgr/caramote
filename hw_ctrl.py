try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("privileges error, try with superuser")

GPIO.setmode(GPIO.BCM)
GPIO.setwarning(False)
GPIO.setup()

# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18


# flush and display to LCD
def display_lcd(input_data):
    display_text = str(input_data)
    print(display_text)
    pass
