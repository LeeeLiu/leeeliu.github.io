

### 在lt_baseTwo环境下安装包的方法
>先激活环境
1. conda install xxx
2. pip install xxx
    - pip install --upgrade xxx
3. `/dat01/liuting/env/anaconda3/bin/pip install horovod==0.16.1`


### 检查当前的包，是哪个版本
 pip uninstall tensorflow==

### 启动anaconda可视化界面
anaconda navigator
### 查看GPU
nvidia-smi
### 新建环境
conda create --name lt_baseTwo python=3.6
### 激活环境
source activate lt_baseTwo

### 在指定anaconda环境下安装package
conda install ...      (CUDA 9.0)

`conda install pytorch torchvision cudatoolkit=10.1 -c pytorch`
>conda install pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=9.0 -c pytorch
>conda install pytorch torchvision cpuonly -c pytorch

### 查看当前系统所有的conda环境
conda env list
### 某个环境下，安装了哪些包
>source activate lt_root
>conda list

### 复制环境
conda create -n new_base --clone base  python=3.6


### 退出当前环境
`source deactivate`，默认回到base 环境
`conda deactivate`

### 在anaconda下改变python的版本
conda create -n py36 python=3.6

### 删除环境
conda remove --name lt_baseTwo --all


## torch

### torch学习链接
[官网](https://pytorch.org/)
[手册](https://github.com/MorvanZhou/PyTorch-Tutorial)
[deeplizard](https://deeplizard.com/learn/video/v5cngxo4mIg)
25 26 CNN示例
[学习率衰减](https://www.jianshu.com/p/9643cba47655)

torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros')


BatchNorm2d、leakyRelu: 尺寸不变
VALID means no padding.

### pytorch
1. Rank-n：n维度、n个轴(axes)、访问某个元素需要n个索引(indexes)、shape的长度
2. 轴(axes)：一个特定维度
3. 
>copy their input data：torch.Tensor() and torch.tensor() 
 share their input data in memory：(win)torch.as_tensor() and torch.from_numpy() 
4. two ways to get the shape: 
> t.size()
torch.Size([3, 4])
> t.shape
torch.Size([3, 4])
5. view()、reshape()作用一样。
6. flatten把整个tensor压成一维，squeeze是去掉值为1的维度。
7. row-wise(dim=0)、column-wise(dim=1)
8. flatten中的t = t.reshape(1, -1)（Since the argument t can be any tensor, we pass -1 as the second argument to the reshape() function.）
9. flatten only part of the tensor：t.flatten(start_dim=1)
10. all of these mean the same thing: 
Element-wise 
Component-wise 
Point-wise
11. Each layer in a neural network has two primary components: 
A transformation (code) 
A collection of weights (data) 
12. kernel/filter --> out_channels/feature maps --> out_features
13. weight的shape：(filter个数，input_channels个数，filter的h和w)
14. y = Ax + b
y：output tensor
A：weight matrix tensor
x：input tensor
b：bias tensor
15. 网络的输入、输出在forward里体现
16. output layer中，一个输出用sigmoid，多个输出用softmax。
17. 数据准备：dataset-->dataloader(传入batch_size)
>train_set = torchvision.datasets.FashionMNIST(
    ...
)
>train_loader = torch.utils.data.DataLoader(
    train_set
    ,batch_size=1000
    ,shuffle=True)
18. 1个epoch时期等于用训练集里全部样本训练一次，一个iteration(step)等于从训练集中取batch_size个样本训练一次。
19. loss.backward()计算梯度， optimizer.step() 更新权重
20. torch.unsqueeze(index)可以为Tensor增加一个维度，增加的这一个维度的位置由我们自己定义
21. 维度交换：
a = torch.rand(4, 3, 6, 7)
print(a.permute(0, 2, 3, 1).shape)
输出结果：
torch.Size([4, 6, 7, 3])
22. 形状
    - a是torch tensor，则
    - a.shape
    - a.size()
    - np.asarray((a.shape)).prod()
23. 读写图像，注意
    - 读写图像时候，注意，1维度问题，2映射到CPU上，3转化为numpy-tensor
    `imageio.imwrite(path, img.squeeze().permute(1, 2, 0).cpu().numpy())`