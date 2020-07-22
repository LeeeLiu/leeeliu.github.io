---
layout:     post
title:      Computer Systems：A Programmer's Perspective
subtitle:   深入理解计算机系统(第四章)
date:       2020-07-21
author:     LT
header-img: 
catalog: true
tags:
    - 理论篇
    - C++
    - CS:APP
---

>本章略读
## 第四章 处理器体系结构
1. 不允许从一个内存地址直接传送到另一个内存地址。另外，也不允许将立即数传送到内存。
1. 流水线
    ![](https://cs-app-1300025586.cos.ap-nanjing.myqcloud.com/not-streamlined.png)
    ![](https://cs-app-1300025586.cos.ap-nanjing.myqcloud.com/streamlined.png)
2. 流水线的局限性(4.4.3)
    - 不一致的划分：运行时钟的速率是由最慢的阶段的延迟限制的。
    ![](https://cs-app-1300025586.cos.ap-nanjing.myqcloud.com/limitations.png)
    - 流水线过深，收益反而下降
