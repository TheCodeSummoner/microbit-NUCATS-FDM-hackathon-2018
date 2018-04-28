from microbit import *
import radio


class Car:

    def __init__(self):
        # Turn on the radio, assign the channel and the power
        radio.on()
        radio.config(power=7, channel=10)

    def drive(self, pressed, direction):
		# View the readme on git to understand/optimize/improve this code
        if pressed[0] == 1023:
            pin0.write_digital(1)
        else:
            pin0.write_digital(0)
        if pressed[1] == 1023:
            pin1.write_digital(1)
        else:
            pin1.write_digital(0)

    def receive_data(self):
		# Receive the data from the controller
        return radio.receive()

    def run(self):
        # Run the loop
        while True:
            # Receive the data
            data = self.receive_data()
            if data is not None:
				# Split the data to get specific values
                data = data.split(".")
                # Initialize an array to store the values
                pressed = []
                # Retrieve the buttons' values from received data
                pressed.append(int(data[0]))
                pressed.append(int(data[1]))
                # Retrieve the direction data from the accelerometer
                direction = data[2]
                # Drive the car
                self.drive(pressed, direction)


if __name__ == '__main__':
    c = Car()
    c.run()