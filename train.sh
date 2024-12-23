export ROBOT_TYPE=PF_TRON1A
# export CUDA_VISIBLE_DEVICES=2
python legged_gym/scripts/train.py --task=pointfoot_rough --sim_device=cuda:2 --headless 