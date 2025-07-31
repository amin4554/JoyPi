import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

class LCDDisplay:
    def __init__(self, cols=16, rows=2, address=0x21):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.lcd = character_lcd.Character_LCD_I2C(i2c, cols, rows, address)
        self.lcd.backlight = True

    def show_message(self, line1, line2=""):
        self.lcd.clear()
        self.lcd.message = f"{line1[:16]}\n{line2[:16]}"

    def clear(self):
        self.lcd.clear()

    def shutdown(self):
        self.lcd.clear()
        self.lcd.backlight = False
