# Microbit NUCATS and FDM hackathon 2018
Micro-bit code created by one of the teams at the *Newcastle University* hackathon organised by **NUCATS** and **FDM**.

## Usage
In order to use this code, either in the MU or any other programming environment with microbit module available, firstly make sure it throws no errors regarding indentation.

The code in *controller.py* should be flashed to the microbit meant for controlling the car, whereas the code in *car.py* should be flashed to the car itself.

## Comments on the car.py
Right now, `listen_to_clicks` function has a simple functionality of switching the on/off states of the wheel. If this is a desired behaviour, there is a way to optimize this part of the code. In order to do that, first change the `self.pressed[0] = '1023'` and `self.pressed[1] = '1023'` code in *controller.py* to `self.pressed[0] = '1'` and `self.pressed[1] = '1'`, and then replace this block of code in *car.py*:
```
if pressed[0] == 1023:
    pin0.write_digital(1)
else:
    pin0.write_digital(0)
if pressed[1] == 1023:
    pin1.write_digital(1)
else:
    pin1.write_digital(0)
```
with:
```
pin0.write_digital(pressed[0])
pin1.write_digital(pressed[1])
```

However, the original reason to use 1023 instead of directly outputting 1, as done in the sample code above, is that it should be possible to use the `write_analog` function with values between 0 and 1023. This function is responsible for setting different power to the car motors, to achieve different motion. For example, this pseudo python code could be implemented to achieve much smoother turning:
```
if direction == "left"/"right":
    # For left pressed[0] = pressed[0] - 500 / pressed[0] = pressed[0]*0.5 etc.
    # For right pressed[1] = pressed[1] - 500 / pressed[1] = pressed[1]*0.5 etc.
    pin0.write_analog(pressed[0])
    pin1.write_analog(pressed[1])
```
When checking for left accelerometer rotation, it should be possible to turn one of the wheels using full power, and the second one using only half of it. Sadly, our attempts of using the `write_analog` function resulted in unexpected crashes, without any error messages to help solve the problem or at least find the bugs.
