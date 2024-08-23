# 应用程序部分
import tkinter as tk
from tkinter import ttk,messagebox
# 操作打印部分
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
from time import sleep

def printHtml():    
    href = input2.get("1.0","end").strip()
    if href == "":
        messagebox.showinfo("错误提示","链接不能为空")
        return
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
    title = input1.get("1.0","end").strip() # 标题
    urls = href.split(',') # 链接
    js = input3.get("1.0","end").strip() # js代码
    for url in urls:
        driver.get(url)
        if title != "":
            driver.execute_script(f'document.title="'+title+'"')
        if js != "":
            driver.execute_script(f''+js)
        # 2.打印网页
        driver.execute_script('window.print();')
        # 等待html加载pdf打印，如果图片多可以加大调整
        sleep(3)

# 创建主窗口
root = tk.Tk()
root.title("批量打印pdf")

# 设置窗口大小
root.geometry("400x460")

# 文本
label = tk.Label(root, text="请输入打印文件的名称(不填默认取网页标题)：")
label.pack()
# 输入框
input1 = tk.Text(root, height=1)
input1.pack()

# 文本
label = tk.Label(root, text="请输入页面链接(链接间用逗号隔开)：")
label.pack()
# 输入框
input2 = tk.Text(root, height=20)
input2.pack()

# 文本
label = tk.Label(root, text="js代码执行部分(如需调整特定样式)：")
label.pack()
# 输入框
input3 = tk.Text(root, height=5)
input3.pack()

# 打印按钮
btn = ttk.Button(root, text="批量打印", command=printHtml)
btn.pack(side=tk.BOTTOM)

# 启动Tkinter事件循环
root.mainloop()