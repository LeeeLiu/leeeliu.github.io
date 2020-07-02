

[Mathjax与LaTex](https://www.cnblogs.com/linxd/p/4955530.html)


### 一、多行函数-对齐
（Mathjax支持）
$$p(y|x)=
\begin{cases}
f(x)    & {  for \ y=+1} \\ 
1-f(x)  & {  for \ y=-1}
\end{cases}$$

#### 二、连续等式-对齐：
>`$\begin{aligned}`[公式内容]`\end{aligned}$`，`\\`换行，需要对齐的地方之前标记&。例如：

$\begin{aligned} a &= \frac{T P}{TP + FN}  \\
  &= \frac{T N}{FP + TN}  \end{aligned}$

$\begin{aligned}
f(x) &= a+b+a \\ 
     &= 2a+b 
\end{aligned}$
**对于mathJax，将aligned换成align**

>以下代码mathJax支持
```
$$\begin{eqnarray}
\sin x & = & x -\frac{x^{3}}{3!} + \frac{x^{5}}{5!}-\\
& &-\frac{x^{7}}{7!}+{}\cdots
\end{eqnarray}$$
```

#### 公式示例
$$\begin{aligned} KL(p,q) &=H(p,q)-H(p) \\ &=\sum_{k=1}^{N} p_{k} \log _{2} \frac{1}{q_{k}}-\sum_{k=1}^{N} p_{k} \log _{2} \frac{1}{p_{k}} \\ &=\sum_{k=1}^{N} p_{k} \log _{2} \frac{p_{k}}{q_{k}} \end{aligned}$$

>换成align:
```
$$\begin{align} KL(p,q) &=H(p,q)-H(p) \\ 
&=\sum_{k=1}^{N} p_{k} \log _{2} \frac{1}{q_{k}}-\sum_{k=1}^{N} p_{k} \log _{2} \frac{1}{p_{k}} \\ 
&=\sum_{k=1}^{N} p_{k} \log _{2} \frac{p_{k}}{q_{k}} \end{align}$$
```
$\operatorname{LSB} \operatorname{fip}(x) = \left\{\begin{array}{ll}{x+1} & {(x\ is\ even)} \\ {x-1} & {(x\ is\ odd)}\end{array}\right.$
$\begin{aligned} & \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ =x+1-2(x \bmod 2) \\ & \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ =x+(-1)^{x} \end{aligned}$

$P_{\mathrm{E}}= \frac{1}{2}\left(P_{\mathrm{MD}}+P_{\mathrm{FA}}\right)$

$\begin{aligned} TPR &= \frac{T P}{TP + FN}  \\
 TNR &= \frac{T N}{FP + TN}  \end{aligned}$
