---
layout:     post
title:      生成模型（1）
subtitle:   VAE、变分推断
date:       2021-01-15
author:     LT
header-img: 
catalog: true
tags:
    - 机器学习
---

### VAE、变分推断
1. 笔记图解
![AEvsVAE](https://handwrite-ml-1-1300025586.cos.ap-nanjing.myqcloud.com/AEvsVAE.png)
![variational_inference](https://handwrite-ml-1-1300025586.cos.ap-nanjing.myqcloud.com/variational_inference.png)
2. [参考视频](https://www.bilibili.com/video/BV15E411w7Pz?p=2)

### 生成模型定义
1. 生成模型只能做数据生成吗？不是
    - GMM：聚类
    - 朴素贝叶斯：判别
2. 概率角度，本质是建模 P（X）
    - 有标签Y，建模 P（X，Y）
    - 无标签，引入隐变量Z，建模 P（X，Z）
    - 自回归，建模 P（X），拆成多个条件概率的乘积

    - 逻辑回归，建模 P（Y=k|X）=？，不关心 P（X），不是生成模型

### EM算法
1. EM不是模型，属于优化算法，作用类似SGD
2. 作用：
    - 解决生成模型的learning中的参数估计问题（MLE）。
    - 由于观测数据分布复杂且未知，没用解析解，参数不能直接求
        - log P(x) = ELBO + KL  （根据贝叶斯公式推导）
    - 所以，需要EM来求。
        - 固定θ，q^ = arg max ELBO
        - 固定q，θ^ = arg max ELBO

### 变分推断
1. 背景
    - 频率派，优化问题
    - 贝叶斯派，积分问题
        - 后验P = 似然×先验
        - P=？，就是inference
            - 精确推断
            - 近似推断，比如`变分推断`