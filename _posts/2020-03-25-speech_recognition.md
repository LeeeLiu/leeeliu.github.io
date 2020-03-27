---
layout:     post
title:      Speech Recognition
subtitle:   李宏毅《深度学习人类语言处理》国语(2020)
date:       2020-03-27
author:     LT
header-img: 
catalog: true
tags:
    - 语音识别
    - 深度学习
---

>内容来自
视频(https://www.bilibili.com/video/BV1QE411p7z3)
课件(http://speech.ee.ntu.edu.tw/~tlkagk/courses/DLHLP20/ASR%20(v12).pdf)

### part 1 前置知识：token、sample
> ppt 1 ~ 15
1. ASR要识别的token
    - 音素（phoneme，比如音标）：缺点是需要lexicon。
    - 手写单位（grapheme，比如字母+标点符号）：优点是不需要lexicon，可以拼写出训练集以外的单词。
    缺点是声音和grapheme的关系对应复杂，有可能拼出不可能存在的词。
    - 单词（word）：缺点是，词汇库过于庞大。英文单词大于100K，对于中文，由于不像英文那样有分隔符，所以很难确定。对于土耳其语言，根本无法穷举出所有单词。
    - 可以传达意思的最小单位（morpheme）：可以理解为词根，单词（word）或者grapheme。。比如，unbreakable-> un + break + able。morpheme从哪里来？语言学家分析、统计方法。
    - 字节：ASR可以适应不同语言了。token大小恒等于256。
2. 声音采样
    - 假设我们取25ms的声音为一个frame，维度是400。（因为对于25ms时长，16kHz的语音，有400个采样点）
    - 把25ms作为一个窗长。10ms为一个步长。每次取frame的时候，移动10ms（有重叠）。所以，1s的话是100帧。
    - 原始声音作为特征输入，太长了（400维），可以使用39维MFCC，80维滤波器输出，如何选择取决于你的需求是什么。
3. 声学特征（acoustic feature）
    - `waveform` -DFT变换->`spectrogram` ->`filterbank output`->log-> DCT ->`MFCC`
    - 目前，最流行的是filterbank output(75%), MFCC(18%)
4. 常用数据集
    - TIMIT 4小时 相当于语音界的MNIST
    - Librispeech 960小时 免费
5. 两大类别的模型：seq-seq和HMM
    * 以下都是seq2seq模型(part2，3里介绍)
        - Listen, Attend, and Spell (LAS)   使用最广（40%）
        - Connectionist Temporal Classification (CTC)   
        - RNN Transducer (RNN-T) 
        - Neural Transducer [Jaitly, et al., NIPS’16]
        - Monotonic Chunkwise Attention (MoChA)
6. 应用：key-word spotting。找出语音中的关键词，又称作关键词唤醒。比如你对ASR提问题，必须先说出Siri这个名字，才会得到回应。一般想法是，让ASR持续倾听人的声音，这样模型就太庞大。所以，不仅仅有准确率，还要模型压缩足够小。而且，要考虑一些安全问题，比如[小孩的声音，主播的声音，意外激活了各家的Amazons-Alexa订下娃娃屋](https://www.phonearena.com/news/Amazons-Alexa-hears-anchorman-report-story-puts-in-orders-for-dollhouses_id89773)

### part2：seq2seq模型之LAS（listen，attend，spell）
> ppt 16  ~ 49
1. listen （encoder）
    - 目的：提取高层语义信息，去除噪声。
    - 方式：一个encoder，输入是声学特征x，输出一样长的表示h。
    - Encoder内部，可以是RNN，也可以是1-D的CNN。 高层的filter可以考虑更长的序列，甚至整个输入序列。实际研究工作中，CNN + RNN是常用方式。
    - encoder里面的self-attention layer，输出的每个h都能够考虑所有的x。
    - 下采样：Pyramid RNN、Pooling over time、Time-delay DNN（带洞卷积也是这个概念）、Attention in a range。
2. attend
（1）关键字Z0和encoder的`每一个输出h`做attention，就像web搜索。
attention是实现方式是match。
match的输出α，可理解为h和Z0的相似度。
softmax，输出C0。
3. spell （decoder）
（2）C0作为decoder（是RNN）的输入，输出hidden state Z1。
（3）刚才我们用Z0做attention，类似地，现在用Z1再做一次attention，得到C1。
4. greedy decoding 可能得不到最优的路径。
所以，考虑beam search：每次保留前beam size个最大概率出现的结果。
5. 训练：
    - 生成的过程是，前一个distribution的输出，参与下一个输入。但是训练（有标签的training）时候不是这样做的。如下。
    - 已知第一个字母是c 我就让输出C的概率越大越好。第一个distribution是否正确，我们先不管它。已知第二个字母是a，对于第二个distribution，我要告诉机器，a之前的字母是c。这一招称作teacher forcing。
    - Why teacher forcing？——> 由于网络内部权重是随机初始化的，如果第一个输出是错的不是c而是x，如果它送进下一个单元里，那么下一个单元就知道了“哦我看见x就输出a”。但是，当第一个单元train好了它知道输出c了，结果第二个单元就要改成“我看见c要输出a，那么之前的不就白train了吗？第一个是c不是x，你能不能先讲啊？”怎么样先讲呢？——>teacher forcing。
6. attention现在用于语音识别，真的好吗？
有Attention的seq2seq最早用于翻译，让decoder从encoder那边去学习，要decode什么词汇出来。
语音识别应该是从左到右，而不是乱跳。这样不对。
第一篇用LAS做语音识别的作者，也这样认为。所以，location-aware attention提出。观点是，每次attention的时候，考虑过去的attention。范围取一个window。
7. LAS的attention：
    - 这里没有location aware，机器竟然自己学到了，从左往右的语音识别该有的样子。
    - LAS可以学到声音和文字之间的复杂关系。——> 用于台语辩识。训练集：台语语音+中文字幕
8. LAS和传统方法的比较：
    * 识别错误率：
        - 2000 hours语音，LAS比CL-DNN+HMM的错误率高了2-3个百分点，和传统方法相比仍然有差距。
        - 12500 hours语音（2018年的icassp），LAS的错误率，比LFR低了一个百分点左右。终于超过传统方法了。
    * 大小：
        - 传统方法（LFR）需要声学模型+lexicon+语言模型＝7.2G。
        - LAS是end2end模型，只需0.4G。LAS里的decoder充当了语言模型的角色。
9. LAS的局限性
online语音辩识。LAS必须听完整个句子才能输出第一个token。


### part 3：其他一些seq2seq模型
> ppt 50 ~ end
1. CTC模型    
    - 特点
        * 只有encoder（2006年出的 用在TIMIT）
        每次吃一个输入，吐一个token。可以online  单向RNN  
        如果选双向RNN 就必须先把整个句子看完 就没有达到online的目的。
        * 每个声音信号x只有25ms，信息量很小。如果暂时无法决定它是什么，则输出的token空集符号“喏”。也许，在看到下一个acoustic feature的时候，就知道输出什么了。
        * 忽略下采样，假设输入T个声学特征，输出T个token。输出序列包括空集符号，以及重复的token。把它们merge起来。
    - 怎么训练？
    问题是，我们不知道输出的ground truth是什么。比如，输出token有四个，现在标注是“好棒”，“好”放在哪里，“棒”放在哪里，空集符号“喏”又放在哪里？**（LAS也有这个问题吗？猜测：因为LAS是有attention的，每个输出都是根据每一个输入算出来，不会存在“不知道输出什么token”的问题。理解粗浅，欢迎批评指正。）**
      * token是远小于输入acoustic feature的。怎么办？-->自己制造label。alignment（对齐）方式有很多，选择哪一个？——> 穷举所有的方式。

    - CTC效果怎么样？CTC（只有encoder）错误率30% …  比LAS（encoder+decoder）差远了
        * 一般地，用CTC需要加上language model做后期映射处理，修正结果。严格来说CTC不是end2end model…
    - CTC的问题：每个输出是相互独立的。----> 一起训练：可以认为LAS的encoder是CTC。
2. RNA模型
    - motivation    
    CTC里，相互独立的linear classifier可以看做decoder（整体来看没有decoder），它们是相互独立的。现在，我们能不能让decoder不要单独做决定，每次输出都看一看前面的。  ——>  把linear classifier 换成RNN或者LSTM，这就是RNA。(介于RNN-T和CTC之间的过渡。)
3. RNN-T模型
    - motivation：一个输入能否映射多个tokens？比如说音标θ，输出“th”。 ——> RNN-T要解决的问题。
    - 解决方法： 一直吃一个输入，直到输出让人满意为止。此时可以输出空集符号，意思是“好了，给我看下一个acoustic feature”。所以，输出里一共有T个空集符号。（语音长度是T）
    - RNN-T存在问题是：训练的时候，怎么决定在哪些位置插入T个空集符号？即，alignment问题。（这一点和CTC一样）——> 穷举（后面会讲到一个合适的演算法来做这个事）
    - 额外RNN：RNN-T不像RNA那样，不是直接把linear classifier 换成LSTM。而是另外训练一个额外RNN。额外RNN的作用：（1）只把token当做输入，作用类似language model。所以，要先把文字转成token（不需要喏），来训练这个额外RNN，先把它训好，再和encoder一起训练。（2）为了训练而设计，为了方便穷举alignment。刚才提到，要穷举所有的alignment做训练，需要合适演算法。而演算法工作的前提就是，要有一个internal的language model，是无视“喏”的。
4. Neural Transducer模型
    - 动机：不要每次只读一个acoustic feature进来，想一次性读多个。
    - 方法：Neural Transducer在RNN-T基础上，每次读一个window个feature做attention。即，重复地吃一个window的输入。输出的token是“喏”的时候，就接收下一个window输入。
5. MoChA模型
    - 在Neural Transducer基础上，使得window移动伸缩自如。
    - 怎样决定每次window移动到哪个位置？——>使用一个二元operator（只输出yes/no，表示window能不能放在这里）作为attention。另外，这里没有使用“喏”了。
