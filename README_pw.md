###  
```
python legged_gym/scripts/train.py --task=pointfoot_rough --sim_device=cuda:0--rl_device=cuda:0 --headless
```

```
python legged_gym/scripts/play.py --task=pointfoot_rough --sim_device=cuda:0 --rl_device=cuda:0 --load_run Dec08_19-45-51_
``` 















本地看 tensorboard, 新开终端运行
```
ssh -L 16009:127.0.0.1:6009 harlab@10.20.124.227

```

```
conda activate pw_lgym
```

```
tensorboard --port=6009 --logdir=logs/pointfoot_rough/Dec14_11-13-52_ 
```

```
http://localhost:16009/
```