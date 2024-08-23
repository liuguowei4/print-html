# 页面打印为PDF文件
<blockquote>应产品部的老大提的需求，搞了一个能把页面打印成pdf的小工具，方便他们当素材。详情可以去看我的博客https://blog.csdn.net/liuguowei14/article/details/141320709?spm=1001.2014.3001.5501
</blockquote>

## url获取
将页面获取的url，复制到文件**index.py**的中**url**变量即可。如果你获取页面链接方式困难，比如需求是那种要第几页到第几页所有打开页面链接的这种需求的，可以看看我的博客的[示例](https://blog.csdn.net/liuguowei14/article/details/141320709?spm=1001.2014.3001.5502)。

## 驱动安装
使用代码前，需要安装一个谷歌浏览器的驱动，方便python操作，具体链接：https://googlechromelabs.github.io/chrome-for-testing/

## 使用方法
### 直接运行
在 **dist/index.exe** 双击应用即可运行，按照弹窗提示输入对应内容即可。**注：除了页面链接其他都是非必填项**

![image](https://github.com/user-attachments/assets/01f1784b-f8c1-4855-ab61-f4a86a64e0c8)

### 开发运行
根据你的需求在 **index.py** 处修改对应代码，修改完成后执行 **pyinstaller --onefile index.py** 即可重新打包。
