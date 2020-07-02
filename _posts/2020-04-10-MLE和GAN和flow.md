---
layout:     post
title:      MLE在生成模型中的应用
subtitle:   MLE直接/间接地应用于GAN/flow的目标函数优化
date:       2020-04-10
author:     LT
header-img: 
catalog: true
tags:
    - MLE
    - GAN
    - flow
    - 论文笔记
---

### 一，GAN/flow优化目标的区别
 - A，极大似然估计(MLE)思想
    1. 极大似然估计：假设真实数据分布服从$P_{data}$,生成数据服从$P_{G}$。现在，我们利用已知真实数据样本$ \{x^1,...,x^m\} \; from \; P_{data}(x) $，来反推最有可能（最大概率）导致这样结果的分布$P_{G}$的参数值θ。
    $$ θ^{*} = arg  \max_{θ} \prod_{i=1}^{m} P_{G}(x^{i};θ) $$
    2. 引入**log**，让连乘转化为连加：
    $$θ^{*} = arg  \max_{θ} \sum_{i=1}^{m} \log P_{G}(x^{i};θ) $$
 - B，MLE应用于GAN的目标函数优化(间接)
    3. 在2式基础上，可以写成期望：
    $$θ^{*} ≈ arg  \max_{θ} E_{x \sim P_{data}} [log P_{G}(x^{i};θ)] $$
    4. 在3式上加一个$P_{data}$有关的项(反正不影响)。此时，我们发现，**MLE等价于最小化$P_{data}$和$P_{G}$的KL-divergence**。
    $$θ^{*} = arg \min_{θ} KL(P_{data} || P_{G}) $$
    5. 按照这个思路，MLE 👉 $\min_{θ} KL(P_{data},P_{G})$ 👉 最小化其它的Div(比如JS-Div) 👉 GAN的generator
    6. $P_{data}$和$P_{G}$都未知，只能从这两种分布里sample。那么怎样衡量它们之间的divergence？答案是，借助discriminator。所以，GAN是以`间接`方式最小化Div的。[了解更多](https://leeeliu.github.io/2019/05/27/GAN/)
 - C，MLE应用于flow的目标函数优化(直接)
    3. 在2式上加一个负号。
    $$θ^{*} = arg  \min_{θ} [- \sum_{i=1}^{m} \log P_{G}(x^{i};θ)] $$
    4. 式3就是flow模型要优化的目标，而且是`直接`方式。未知参数有两个。其中，$P_{G}$可以构造成已知的。所以未知参数只剩θ了。
    5. MLE算得的结果，和`最小二乘法`计算结果相同（但是数据维度太高时，计算很慢）。

### 二，GAN/flow优缺点小结
1. GAN的问题是，训练稳定性差。[了解更多](https://leeeliu.github.io/2019/05/27/GAN/)
2. flow的优点是，解释直观，训练不会坏掉。缺点是，耗费资源。