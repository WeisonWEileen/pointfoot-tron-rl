### competition for pointfootGym
run
```
python legged_gym/scripts/train.py --task=pointfoot_rough --rl_device=cuda
```


### Reference Project
https://github.com/SuDaxia-kai/pointfootGym.git


### directly run sim2sim with software from limx dynamics
you should always start these 3 scripts with limx sdk
mujoco:
```
python3 pointfoot-mujoco-sim/simulator.py
python3 rl-deploy-with-python/pointfoot_controller.py
python3 pointfoot-mujoco-sim/robot-joystick/robot-joystick
```

or directlry run `./run.sh`

```
./run.sh
```