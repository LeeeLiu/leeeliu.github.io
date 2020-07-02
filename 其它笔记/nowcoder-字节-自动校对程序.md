

### 字节跳动-笔试：万万没想到之聪明的编辑

#### 一、题目描述
[来自](https://www.nowcoder.com/questionTerminal/42852fd7045c442192fa89404ab42e92)
>描述: 实现一个检查拼写错误的校对程序
    1. 三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello 
    2. 两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello   
    3. 上面的规则优先“从左到右”匹配，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该优先考虑修复AABB，结果为AABCC   

>输入描述:第一行包括一个数字N，表示本次用例包括多少个待校验的字符串。后面跟随N行，每行为一个待校验的字符串。
输出描述:N行，每行包括一个被修复后的字符串。
示例输入
2
helloo
wooooooow
示例输出
hello
woow

#### 二、思路
校对程序规则总结如下。
- AA**型。以下两种类型矫正完毕，遍历，步长是2，continue
    - AAA --> AA 矫正一次，continue
    - AABB --> AB 矫正一次，continue
- AB**型。直接遍历，步长是1。

#### 三、实现
```
#include<vector>
#include<string>
#include<iostream>
using namespace std;

int main()
{
    int n, i, j;
    vector<string> res;
    string str;
    cin>>n;
    for(i=0; i<n; i++)        
    {
        cin>>str;
        res.push_back(str);
    }
    
    for(i=0; i<n; i++)
    {
    if(res[i].size()>2)
        for(j=0; j<res[i].size(); )
        {   
            // AA*
            if(j+1<res[i].size() && res[i][j]==res[i][j+1])
            {
                // AAA*
                if(j+2<res[i].size() && res[i][j+1]==res[i][j+2])
                {
                    res[i].erase(j+2, 1);
                    //res[i].erase(res[i].begin()+j+2);
                    continue;
                } 
                // AABB*
                if( j+3<res[i].size() && res[i][j+2]==res[i][j+3])
                {
                    res[i].erase(j+3, 1);
                    //res[i].erase(res[i].begin()+j+3);
                    continue;
                } 
                j = j+2;
                continue;
            }                                                                 
            // AB
            j++;
        }
    }
    for(i=0; i<n; i++)
        cout<<res[i]<<endl;
    return 0;
}
```
