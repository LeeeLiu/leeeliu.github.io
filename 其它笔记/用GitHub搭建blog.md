


### 修改站点ico
- 将`/img`下的`favicon.ico`换掉，并换一个名字。在`/_includes/head.html`里的`favicon.ico`换掉。（位置在`<!-- Favicon -->`标签下）

### gitalk评论系统
1. 申请GitHub OAuth application，[点击](https://github.com/settings/applications/new)。获取clientID，clientSecret，修改conf.yml里的参数。
1. 在仓库的setting里勾选issues
2. 点击“使用GitHub登陆”，刷新页面。
[参见](https://www.jianshu.com/p/78c64d07124d)