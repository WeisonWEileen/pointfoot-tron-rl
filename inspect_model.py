import torch
from torchsummary import summary

# 假设你的模型文件名为 'model.pt'
model_path = '/home/weison/pointfootGym/logs/pointfoot_rough/Dec05_21-32-19_/model_35000.pt'

# 加载模型
model = torch.load(model_path, map_location=torch.device('cpu'))

summary(model, input_size=(1,27))