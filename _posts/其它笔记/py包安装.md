

* timeout原因：连接校园网常规操作，换个时间再试（服务器维护）

### python包安装
1. pycharm里面装
2. 下载.whl安装
    在 (https://pypi.org/project/)  或者
    [python库](https://www.lfd.uci.edu/~gohlke/pythonlibs/)下载.whl文件，
   cmd打开.whl文件所在目录，pip install xxx.whl

3. GitHub上，下载python包的源码，打开setup.py对应的文件夹，鼠标右键git bash here，输入“pip install .”即可。
4. >pip install --index-url  xxx [包的名字，如tensorflow]
（xxx如https://pypi.douban.com/simple）
>pip install [包的名字] -i [URL]
5. 一些pip源
阿里云	http://mirrors.aliyun.com/pypi/simple/
豆瓣 	http://pypi.douban.com/simple/ 
清华大学		https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学	https://pypi.mirrors.ustc.edu.cn/simple/ 
6. 使用方法：直接 -i 加 url 即可。如：
pip install web.py -i http://pypi.douban.com/simple
如果报错，换成
pip install web.py -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
