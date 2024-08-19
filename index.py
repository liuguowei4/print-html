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

urls = [] # 在此输入页面链接
for url in urls:
    driver.get(url)
    # 1.自定义代码执行，可以通过设置document.title修改名称，部分样式
    driver.execute_script(f'document.getElementById("logobg").style.display="none";document.getElementById("foot").style.display="none"')
    # 2.打印网页
    driver.execute_script('window.print();')
    # 等待html加载pdf打印，如果图片多可以加大调整
    sleep(3)
