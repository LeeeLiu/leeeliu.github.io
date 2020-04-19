---
layout:     post
title:      Self-attention
subtitle:   Transformer：seq2seq model with self-attention
date:       2020-04-19
author:     LT
header-img: 
catalog: true
tags:
    - seq2seq
    - 
---

>内容来自
>>[李宏毅机器学习2019-视频](https://www.bilibili.com/video/BV14J411W7hw?p=60)
>>[课件](http://speech.ee.ntu.edu.tw/~tlkagk/courses/ML_2019/Lecture/Transformer%20(v5).pdf)

### 概念简介
1. transformer:  一个有self-attention的seq2seq model
2. bert:  无监督的训练的transformer

### 一，attention想要解决的是什么？
1. 我们要处理一个seq，自然想到RNN。而attention是一种代替RNN的做法。
2. RNN的问题以及解决问题的探索：
    - RNN不容易被平行化。比如，我要想输出b4, 我就要先看a1,再看a2,再看a3,再看a4,才能输出b4。所以👉用CNN代替RNN。
    - CNN优点是，可以平行。图中每个三角形filter都是可以同时操作的。当然，CNN缺点是一个filter只能看到自己视野范围内的信息。为了让它看到input里更长的信息，就必须多叠几层。
    - 现在，问题是，只有上层一些的filter才能看到更多信息。我们想让第一层的每个filter就看到更多信息，怎么办？👉**self-attention！**
3. self-attention凭什么代替RNN？
    - self-attention和双向RNN有相同的能力，即，每个输出bi都看过了整个input seq。不同之处是，attention是**可以并行**的。即b1到b4可以同时计算！
    - 为什么可以并行？虽然self-attention既不是CNN也不是RNN（不知道理解的对不对。欢迎批评指正），但是这里面有一堆矩阵乘法，矩阵相乘是容易用GPU加速的。

### 二，attention具体做法
   - input seq中其中一个x通过embedding变成a。a通过不同的match得到三个向量q, k, v。
   - 拿每个q去对每个k做attention（dot product）。其中，q和k的维度一样。其中，attention做的事情是，吃两个向量，output一个分数，表示这两个向量有多么匹配。
   - 举个例子。拿q1对k1的attention输出是α11，q1对k2得到α12，q1对k3得到α13，q1对k4得到α14。把这四个α送进softmax层，得到四个α_hat。把每个α1i_hat和vi相乘，得到四个值，再累加，得到第一个输出b1。这时它考虑了input里x1到x4的所有信息。
   - 如果不想考虑global的信息只想考虑local信息，那么我让某一个α-hat是0就好了。
   - self-attention的变形:
       * multi-head  self-attention：不同的head关注点不一样，有点想看local信息，有点想看global的。

### 三，存在的问题和方法：positional encoding
   - self-attention没有考虑位置信息。——> 手工设计和ai同维度的ei（positional encoding），和ai加起来。

### 四，self-attention在seq2seq里的应用
- seq2seq里，encoder和decoder分别用self-attention取代 👉transformer。
- 我们熟知的batch normalization是，同一个维度上的不同data做归一化（使得均值为0方差为1）
- 这里面用到layer normalization，意思是，对同一笔data的不同维度的值归一化。layer归一化一般搭配RNN使用。而transformer很像RNN，这可能是transformer用layer normalization的理由。
- 应用举例：
    * 输入很多文章，输出摘要。。
    * 对于句子`the dog didn't cross the street because it was too tired`，attention能学出`it`指代的对象是`dog`。而对于句子`the dog didn't cross the street because it was too wide`，attention能学出`it`指代的对象是`street`。
