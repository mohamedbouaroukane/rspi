import RPi.GPIO as GPIO

class RelayController:
    def __init__(self, pin):
        self.pin = pin
        self.setup_gpio()

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def toggle(self):
        GPIO.output(self.pin, GPIO.HIGH - GPIO.input(self.pin))

    def cleanup(self):
        GPIO.cleanup()

if __name__ == "__main__":
    # Example usage
    relay_controller = RelayController(17)
    relay_controller.turn_on()
    # Do some other things
    relay_controller.turn_off()
    relay_controller.cleanup()