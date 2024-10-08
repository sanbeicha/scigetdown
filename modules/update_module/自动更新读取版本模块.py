import re
from typing import Any

import requests


def 获取最新版本号和下载地址(project_name) -> dict[str, Any]:
    # 通过访问最新的页面 获取版本号和下载地址和更新内容
    # 镜像地址也可以自己造一个 https://quiet-boat-a038.duolabmeng.workers.dev/
    # url = f"https://ghproxy.com/https://github.com/{project_name}/releases/latest"
    # url = f"https://github.com/{project_name}/releases/latest"
    url = f"https://mirror.ghproxy.com/https://github.com/{project_name}/releases/latest"
    # print(url)
    jsondata = requests.get(url)

    return 解析网页信息(jsondata.text, project_name)


def 解析网页信息(网页, project_name) -> dict[str, Any]:
    版本号 = 网页.find('<span class="ml-1">')
    版本号 = 网页[版本号 + len('<span class="ml-1">') :]
    版本号 = 版本号[: 版本号.find("</span>")].strip()
    # print(版本号)
    # 获取更新内容
    # <div data-pjax="true" data-test-selector="body-content" data-view-component="true" class="markdown-body my-3"><h1>自动更新程序</h1>
    # <ul>
    # <li>更新了自动构建</li>
    # <li>自动获取版本</li>
    # <li>自动下载</li>
    # <li>自动替换</li>
    # </ul></div>
    # </div>

    更新内容 = 网页.find(
        '<div data-pjax="true" data-test-selector="body-content" data-view-component="true" class="markdown-body my-3">'
    )
    更新内容 = 网页[
        更新内容
        + len(
            '<div data-pjax="true" data-test-selector="body-content" data-view-component="true" class="markdown-body my-3">'
        ) :
    ]
    更新内容 = 更新内容[: 更新内容.find("</div>")]
    # print(更新内容)
    # 获取下载地址列表
    #             <a href="/duolabmeng6/qtAutoUpdateApp/releases/download/0.0.4/my_app_MacOS.zip" rel="nofollow" data-skip-pjax>
    #               <span class="px-1 text-bold">my_app_MacOS.zip</span>
    #
    #             </a>

    # 重新重新访问页面
    # url = f"https://ghproxy.com/https://github.com/{project_name}/releases/expanded_assets/{版本号}"
    # url = f"https://github.com/{project_name}/releases/expanded_assets/{版本号}"
    url = f"https://mirror.ghproxy.com/https://github.com/{project_name}/releases/expanded_assets/{版本号}"
    网页2 = requests.get(url).text

    下载地址列表 = []
    mac下载地址 = ""
    win下载地址 = ""
    pattern = re.compile(r'class="Truncate-text text-bold">(.*?)</span>')
    result = pattern.findall(网页2)
    # print(result)
    for item in result:
        # print(item)
        下载地址 = item
        # 下载地址 = f"https://ghproxy.com/https://github.com/{project_name}/releases/download/{版本号}/{下载地址}"
        # 下载地址 = f"https://github.com/{project_name}/releases/download/{版本号}/{下载地址}"
        下载地址 = f"https://mirror.ghproxy.com/https://github.com/{project_name}/releases/download/{版本号}/{下载地址}"

        文件名 = item
        if 文件名.find("Source code") != -1:
            continue

        下载地址列表.append({文件名: 下载地址})

        if 文件名.find("MacOS.zip") != -1:
            mac下载地址 = 下载地址
        if 文件名.find(".exe") != -1:
            win下载地址 = 下载地址

    # print(下载地址列表)
    # 获取发布时间
    # <relative-time datetime="2022-07-22T17:32:41Z" class="no-wrap"></relative-time>
    发布时间 = 网页2.find('<relative-time datetime="')
    发布时间 = 网页2[发布时间 + len('<relative-time datetime="') :]
    发布时间 = 发布时间[:10]
    # 去掉 t z
    # 发布时间 = 发布时间.replace("T", " ").replace("Z", "")

    # 版本号大于20个字符就清空
    if len(版本号) > 20:
        版本号 = ""
        发布时间 = ""
        更新内容 = ""

    return {
        "版本号": 版本号,
        "发布时间": 发布时间,
        "更新内容": 更新内容,
        "下载地址列表": 下载地址列表,
        "mac下载地址": mac下载地址,
        "win下载地址": win下载地址,
    }


# 测试
if __name__ == "__main__":
    data = 获取最新版本号和下载地址("sanbeicha/qtAutoUpdateApp")
    print(data)
