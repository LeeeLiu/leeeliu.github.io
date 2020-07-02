


>以前常常遇到这样的问题。直接百度，后来解决了。但是，没有深入了解原理。
#### "error LNK2019:无法解析的外部符号"解决方法总结
- 方法1：C/C++混编，编译器编译出错。解决方法：在C语言的头文件中加入以下代码：（转自[这里](https://www.cnblogs.com/hiloves/p/4678848.html)）
```
#ifdef __cplusplus
extern "C" {
#endif

	int fun(int a, int b); //这里写函数声明

#ifdef __cplusplus
}
#endif
//提示链接器这个函数是C语言的
```
- 方法2：修改后缀.cpp或者.c
- 方法3：删除debug文件夹里的.exe文件





