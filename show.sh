# PF_P441A  PF_P441B PF_P441C PF_P441C2 PF_TRON1A WF_TRON1A
export ROBOT_TYPE=PF_TRON1A
python ../pointfoot-mujoco-sim/simulator.py &
../pointfoot-mujoco-sim/robot-joystick/robot-joystick &
python ../rl-deploy-with-python/pointfoot_controller.py