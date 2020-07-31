---
layout:     post
title:      Computer Systems：A Programmer's Perspective
subtitle:   深入理解计算机系统(第六章)
date:       2020-07-29
author:     LT
header-img: 
catalog: true
tags:
    - C++
    - CS:APP
---

### 第六章 存储器层次结构
1. 随机访问存储器
    - 随机访问存储器(Random Access Memory, RAM)分为两类:静态RAM(SRAM)和动态RAM(DRAM)。
    - SRAM比DRAM更快，但也贵得多。
    - SRAM用来作为高速缓存存储器，既可以在CPU芯片上，也可以在片下。
    - DRAM用来作为主存以及图形系统的帧缓冲区。
    - SRAM对诸如光/电噪声这样的干扰不敏感。
    - 典型地，一个桌面系统的SRAM不会超过几兆字节，但是DRAM却有几百或几千兆字节。
    - ![6-2](腾讯云/6-2.png)
2. SSD
    - 读SSD比写要快。
    - 要很多年ssD才会磨损坏(参考练习题6.5)
    - 