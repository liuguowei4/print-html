# 页面打印为PDF文件
<blockquote>应产品部的老大提的需求，搞了一个能把页面打印成pdf的小工具，方便他们当素材。详情可以去看我的博客https://blog.csdn.net/liuguowei14/article/details/141320709?spm=1001.2014.3001.5501
</blockquote>

## url获取
将页面获取的url，复制到文件**index.py**的中**url**变量即可。如果你获取页面链接方式困难，比如需求是那种要第几页到第几页所有打开页面链接的这种需求的，可以参考我博客的示例。

## 驱动安装
使用代码前，需要安装一个谷歌浏览器的驱动，方便python操作，具体链接：https://googlechromelabs.github.io/chrome-for-testing/

## 使用方法
### 样式调整
如果有样式方面的调整，比如要在打印时隐藏某些东西，或者控制打印标题，可在文件**index.py**中**driver.execute_script**部分输入，比如我要把标题变成"测试打印"，并且隐藏一个id为a的表格
<code>
index.py
……
    driver.execute_script(f'document.title="测试打印";document.getElementById("a").style.display="none";')
……
</code>
### 运行代码
<code>python index.py</code>
