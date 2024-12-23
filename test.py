import torch

class TorqueRewardCalculator:
    def __init__(self, torques):
        """
        初始化类
        :param torques: 一个 2D Tensor，表示每个样本的关节力矩
        """
        self.torques = torques

    def _reward_torques(self):
        """
        计算每个样本的力矩惩罚（平方和）
        :return: 每个样本的力矩平方和，形状为 (batch_size,)
        """
        # return torch.sum(torch.square(self.torques), dim=1)
        return torch.sum(torch.square(self.torques))

if __name__ == "__main__":
    # 创建示例力矩数据 (batch_size=3, num_joints=4)
    torques = torch.tensor([
        [1.0, 2.0, 3.0, 4.0],  # 样本 1 的关节力矩
        [0.5, 1.5, 2.5, 3.5],  # 样本 2 的关节力矩
        [0.0, 0.0, 0.0, 0.0]   # 样本 3 的关节力矩
    ])

    # 实例化计算器
    calculator = TorqueRewardCalculator(torques)

    # 计算力矩惩罚
    rewards = calculator._reward_torques()

    # 打印结果
    print("Torques:")
    print(torques)
    print("\nReward Torques (penalty):")
    print(rewards)
