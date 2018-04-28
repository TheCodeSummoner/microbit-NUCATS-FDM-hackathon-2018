from microbit import *
import radio


class Controller:

    def __init__(self):
        # Initialize the buttons' presses list
        self.pressed = [0, 0]
        # Initialize the direction
        self.direction = None
        # Turn on the radio, assign the channel and the power
        radio.on()
        radio.config(power=7, channel=10)

    # Update the list indicating which buttons are pressed
    # Format: [a, b] where a, b are 1023 for pressed (max analog value) and 0 for not pressed
    def listen_to_clicks(self):
        # Check the pressed buttons and update the list
        if button_a.is_pressed():
            self.pressed[0] = '1023'
        else:
            self.pressed[0] = '0'
        if button_b.is_pressed():
            self.pressed[1] = '1023'
        else:
            self.pressed[1] = '0'

    def run(self):
        # Run the loop
        while True:
            # Update the pressed values
            self.listen_to_clicks()
            # Update the direction
            self.get_direction()
			# Send the data to the car
            self.send_data()

    def get_direction(self):
        # Get the direction where to go
        self.direction = accelerometer.current_gesture()

    def send_data(self):
        # Initialize string to send it and add the values
        s = str(self.pressed[0]) + '.' + str(self.pressed[1])
        s = s + '.' + self.direction
        radio.send(s)


if __name__ == '__main__':
    c = Controller
    c.run()