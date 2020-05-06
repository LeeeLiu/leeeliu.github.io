---
layout:     post
title:      Language model、Voice conversion
subtitle:   李宏毅《深度学习人类语言处理》国语(2020)
date:       2020-04-15
author:     LT
header-img: 
catalog: true
tags:
    - 语音识别
    - computer audition
---

>内容来自
>>[视频](https://www.bilibili.com/video/BV1QE411p7z3?p=8)
>>[课件1](http://speech.ee.ntu.edu.tw/~tlkagk/courses/DLHLP20/ASR3.pdf)
>>[课件2](http://speech.ee.ntu.edu.tw/~tlkagk/courses/DLHLP20/Voice%20Conversion%20(v3).pdf)

### 一，Language model
 1. 在语音识别里，为什么要Language model(LM)？
    - 👉估计一串token sequence出现的几率。
    在HMM中，$$ Y^{*}= arg \max_{Y} P(X|Y)P(Y) $$。其中，P(Y)就是LM。
    - 节省收集资料的成本，提高ASR准确率。
    在基于深度学习的end2end语音识别系统里，就不需要P(Y)了。但是，事实上加上P(Y)更有效。加上P(Y)我们就得到了这个奇怪的解释不通的式子。$$ Y^{*}= arg \max_{Y} P(Y|X)P(Y) $$。其中，计算P(Y|X)就必须收集成对的很多资料，这个成本很高，P(Y|X)估不准。而计算P(Y)只需文本资料，这个就很好收集，P(Y)可以估的准。所以，凡是输出为文字的，比如ASR，翻译，从文章里提炼标题，这样的任务，我们都可以加上LM。
    - 例子：一个巨大的LM：Bert，用了30亿以上个词。
 2. 怎样估计P(Y)？
    - 在DL之前，有N-gram。
    它的最大问题是数据稀疏。即，训练集里没有出现的单词组合，它就认为概率是0。这个和实际情况相悖。
    我们不要让它是0，可以给它一个小小的概率。这个小小概率是多少呢？-> LM smoothing技术。
    - 在DL之前，怎么LM smoothing？👉continuous LM
     * continuous LM是一种从推荐系统借鉴来的方法。比如，很多用户同时喜欢动画A和动画B，而用户1喜欢动画B，动画A没有打分。但我们可以推测出，用户1也是喜欢动画A的。这个补全稀疏矩阵的方法，叫做矩阵分解。
     * 迁移到LM上来，我们可以估计出没有在训练集里出现过的token-sequence概率。
    - 基于DL的LM：
     * continuous LM其实是DL的简化版👉只有一个liner hidden layer的network
     * NN-based LM。起初是为了取代N-gram，即输入几个词汇，预测下一个词汇。
     * RNN-based LM：解决“很长的history来预测下一个词汇”问题。
 3. 怎样把LM与end2end-model结合：以LAS-decoder为例
    - 按照什么时候结合来分类：trained_LM + trained_LAS；trained_LM + 没有train的LAS。
    - 按照结合方式分类：
      * 直接把LM和LAS的输出取log加一起（超参调节两者比重）
      * 把LM的hidden layer，和LAS结合。结合后的输出，再送进一个额外网络network训练。缺点是，一旦LM更换，network就要重train了。解决方法是👇
      * 把LM在softmax之前的hidden layer，和LAS结合。

### 二，Voice conversion
1. VC的应用场景
   - speaker转换：个性化定制TTS系统。
      * 机器人管家模仿父母的声音，而不是机械的声音，小孩子会更喜欢。
      * 保护隐私。声音可以透露一个人的很多信息，年龄、身体状态、心理状态等。
      比如小孩子一个人在家，外面有人按门铃。如果门铃系统上装有VC，小孩子此时用对讲机回复，外面的人听到的就是大人的声音。
   - speaking style转换
      * 情绪转换：一个说话本身温柔的人，想要表达愤怒但是别人听不出来。这个问题VC就可以解决。
      * 悄悄话转换成正常的话：比如在图书馆说话不能大声、在车上说话不想让旁边人听到。
   - 提升可懂度（Intelligibility）
      * VC把发音器官受损的人发出的声音，转换成正常的声音，使得别人听得懂。
      * 口音（accent）转换👉自己说出的不标准的英文，转换成标准的英文，在参会的时候让评委都听得懂。此外，还可以加速学习一门语言。
   - 数据增强：男女生声音相互转换；加噪和去噪。
2. implementation时的问题
   - 实际应用场景中，源语音和目标语音肯定不一样长，这样就需要用seq2seq模型。现在，为了方便研究，我们假设输入输出一样长。
   - 输入和输入往往不是语音，而是acoustic feature，比如spectrogram。这里就需要一个vocoder（Griffin-Lim、WaveNet）来将spectrogram变成语音。vocoder的引用不只是VC，还有TTS, Speech Separation等等。
3. 类别：
   - 平行数据（模型预训练、语音合成）
   - 非平行数据：从image style transfer借鉴方法
      * 特征（说话内容、说话人身份特征、情绪、口音）分离，替换。想做什么东西的转换，就替换什么东西。
         + 做法类似auto-encoder。`输入声音👉latent vector👉重构声音`，保证输入输出的声音越接近越好。和auto-encoder不同的是，这里的encoder有多个，比如有content-encoder，有speaker-encoder。问题来了，我怎么知道，输入的哪些东西喂给content-encoder，哪些东西喂给speaker-encoder？一种做法是，用one-hot来表示speaker身份，缺陷是无法合成训练集里未曾出现的speaker声音。还有的做法是，使用预训练好的speaker-encoder（speaker embedding）。
         + content-encoder没法直接换成一个完整的ASR（输出是文字不是latent，decoder那边没法用），可以用ASR中seq2seq里的encoder部分，输出是token序列的概率的那种。
         + 还有一个办法是，在content-encoder里加instance normalization（减掉均值，除以方差），从而去掉和说话人有关的信息，只关注说话内容。PS，在decoder那边就要加adaptive instance normalization，从而把speaker相关的信息加进来。
      * 直接转换

### 三，voice conversion（续）      
1. 对于处理非平行数据的特征分离方法，存在的问题和方法：
   - 问题：训练（content-encoder和speaker-encoder吃的是`同一个`语者的声音）和测试（content-encoder和speaker-encoder吃的是`不同`语者的声音）不一样导致转换后的语音音质差。
   - 方法1（行不通）：如果在训练阶段，让content-encoder和speaker-encoder吃的是`不同`语者的声音，但是我不知道ground truth，没有训练目标了（因为是非平行数据），这个方法行不通。
   - 方法2：2nd Stage Training。在decoder后面接discriminator D（作用是判断real or generated，是否像个正常人说话的声音）和speaker classifier（原有的方法中，这个就当作D）。进一步，额外train一个和decoder吃相同输入的补丁网络patcher（因为它觉得decode出来的语音质量可能不太好），patcher的输出钉在decoder的输出上，再喂给D。
2. 对于处理非平行数据，还有直接转换的方法
   - cycle-GAN
      * GAN的思路：`语者A的speech X👉（generator G）语者B的speech Y`，Discriminator D判断Y是否属于语者B。（训练集里有除了Y以外的B的多种说话内容的声音）
      * 上面的思路有一个问题：G的训练目标只有一个（骗过D让D认为speech Y是语者B的），这样G就会忽略speech X的说话内容。所以，在此基础上加以一个训练目标：cycle-consistency，即训两个G。`语者A的speech X👉语者B的speech Y👉speech X'`，X和X'越接近越好。另外，为了训练稳定性，还可以让G学会`语者B的speech Y👉一模一样的Y`。
      * Cycle-GAN还可以是双向的。即`语者B的speech Y👉语者A的speech X👉speech Y'`，Y和Y'越接近越好。
   - star-GAN
      * 考虑多对多的语音转换。如果cycle-GAN来做，需要训练n(n-1)个G。👉star-GAN来解决。
      * 两个G：`语者A的声音X + 语者B信息(one-hot或者embedding)👉B的声音Y + 语者A信息👉A的声音X'`。
      * 一个D：`声音Y + 语者B信息 👉 D判断声音Y是否属于语者B`。另外还有classifier。此处省略。
   - Blow：flow-based model for voice conversion