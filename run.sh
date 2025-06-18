#!/bin/bash
python3 ./ponitfootMujoco/simulator.py &
python3 ./ponitfootMujoco/rl_controller.py &
../pointfoot-mujoco-sim/robot-joystick/robot-joystick