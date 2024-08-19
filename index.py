import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
from time import sleep

save_path = os.getcwd() # 当前文件所在的文件夹路径
options = Options()
settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": ""
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,  # 另存为pdf，1 是默认打印机
    "isHeaderFooterEnabled": False,  # 勾选页眉和页脚
    "isCssBackgroundEnabled": True,  # 勾选背景图形
    "mediaSize": {
        "height_microns": 297000,
        "name": "ISO_A4",
        "width_microns": 210000,
        "custom_display_name": "A4",
    },
}
prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    'savefile.default_directory': save_path,
}

options.add_argument('--enable-print-browser')
options.add_argument('--kiosk-printing')  # 静默打印无需点击打印页面的确定按钮
options.add_experimental_option('prefs', prefs)
service = Service(executable_path="D:\chromedriver-win64\chromedriver.exe") # 谷歌浏览器驱动路径
driver = webdriver.Chrome(service=service, options=options)

urls = ["https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202103/t20210318_48374.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202102/t20210226_48309.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202101/t20210122_48239.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202012/t20201221_48125.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202011/t20201125_48045.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202011/t20201110_48002.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202009/t20200926_47839.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202009/t20200904_47758.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202007/t20200722_47623.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202006/t20200623_47540.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202005/t20200522_47383.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202005/t20200506_47349.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202003/t20200324_47237.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202002/t20200226_47139.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202001/t20200119_47067.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202001/t20200109_47033.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/201912/t20191230_46993.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/201912/t20191210_46887.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/201912/t20191210_46889.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/201910/t20191028_46648.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202212/t20221205_49911.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202211/t20221116_49888.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202211/t20221116_49887.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202211/t20221116_49886.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202207/t20220725_49766.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202206/t20220624_49704.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202205/t20220530_49686.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202204/t20220427_49650.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202203/t20220329_49583.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202203/t20220314_49545.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202201/t20220125_49461.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202112/t20211231_49400.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202111/t20211125_49299.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202111/t20211105_49117.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202109/t20210924_49003.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202108/t20210827_48937.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202107/t20210723_48845.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202107/t20210702_48769.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202105/t20210521_48628.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202104/t20210423_48518.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202407/t20240731_50806.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202407/t20240703_50774.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202405/t20240528_50730.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202404/t20240429_50705.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202403/t20240328_50654.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202403/t20240312_50598.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202401/t20240124_50555.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202312/t20231218_50510.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202312/t20231201_50486.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202311/t20231106_50453.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202310/t20231012_50432.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202308/t20230824_50366.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202308/t20230801_50332.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202306/t20230629_50255.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202305/t20230530_50162.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202305/t20230504_50112.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202303/t20230328_50032.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202303/t20230327_50030.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202301/t20230131_49951.html","https://www.cdr-adr.org.cn/ylqx_1/Medical_aqjs/Medical_aqjs_jjkx/202212/t20221229_49928.html"]
for url in urls:
    driver.get(url)
    # 1.自定义代码执行，可以通过设置document.title修改名称，部分样式
    driver.execute_script(f'document.getElementById("logobg").style.display="none";document.getElementById("foot").style.display="none"')
    # 2.打印网页
    driver.execute_script('window.print();')
    # 等待html加载pdf打印，如果图片多可以加大调整
    sleep(3)
