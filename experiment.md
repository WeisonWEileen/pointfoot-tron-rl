### model structure

input dim: 27 dim proprioception

output dim: 6 dim action 

<img src="./assets/image-20241208114321449.png" alt="image-20241208114321449" style="zoom:50%;" />

### specified ```is_sim=True``` when deploy in simulation

```
robot = Robot(RobotType.PointFoot, is_sim=True)
```
###  rewards which exist in ```legged_gym``` but not exist in the repo that TA offer
![image-20241208102741868](./assets/image-20241208102741868.png)
# experiment after adding ```lin_vel_z``` to the reward function
### Mean episode length reach 270 after adding ```lin_vel_z```
![image-20241208102916680](./assets/image-20241208102916680.png)

checkpoint of ```model_36000.pt```
![video](./assets/35000_checkpoint.mp4)

