# Generalimage

[![CodeTime Badge](https://img.shields.io/endpoint?style=social&color=222&url=https%3A%2F%2Fapi.codetime.dev%2Fshield%3Fid%3D26819%26project%3Dscigetdown%26in=0)](https://codetime.dev)

[![timeashfly/scigetdown](https://gitee.com/timeashfly/scigetdown/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/timeashfly/scigetdown)

## 介绍

本项目开发一款批量下载`SciHub`文章的桌面软件。

## 软件架构

本项目基于`Pyside6`包构建一套桌面软件。
并通过在`GitHub action`设置`CI/CD`，提供自动更新功能。

## pyside6封装教程

`PyInstaller`是一款非常实用的`Python`打包工具，可以将`Python`脚本及其依赖的库、资源文件等打包成一个单独的可执行文件。
下面详细介绍`PyInstaller`的安装和使用方法。

### 1、PyInstaller的安装

首先，我们需要使用`pip`命令安装`PyInstaller`。在命令行中输入以下命令：

```bash
pip install pyinstaller
```

如果安装成功，你可以在命令行中使用pyinstaller命令。

### 2、PyInstaller的基本使用

`PyInstaller`的基本使用非常简单，只需要在命令行中输入`pyinstaller`命令，并跟上你要打包的Python脚本文件。例如，如果你要打包名为`main.py`的脚本文件，可以在命令行中输入以下命令：

```bash
pyinstaller -F main.py
```

上述命令中，-F选项表示生成一个无依赖的控制台可执行文件。PyInstaller会分析`main.py`脚本，识别出脚本中所引用的库和资源文件，然后将这些文件打包到一个单独的可执行文件中。

### 3、使用PyInstaller打包PySide6程序

使用`PyInstaller`打包`PySide6`程序时，需要注意一些特殊问题。`PySide6`是一个用于开发跨平台桌面应用程序的库，包含了许多用于创建GUI界面的类和函数。在打包`PySide6`程序时，需要确保所有必要的`PySide6`模块都被正确地导入和打包。

例如，假设你有一个名为`main.py`的`PySide6`程序，它使用了`PySide6.QtSvg`模块。在打包这个程序时，你需要使用`--hidden-import`选项将`PySide6.QtSvg`模块导入到打包过程中。你可以在命令行中输入以下命令：

```bash
pyinstaller -F --hidden-import=PySide6.QtSvg main.py
```

上述命令中，`--hidden-import`选项告诉`PyInstaller`在打包过程中导`入PySide6.QtSvg`模块。这样，打包后的可执行文件就可以正确地运行了。

#### 打包命令说明

```bash
pyinstaller --onefile --windowed --icon "app.icns" "my_app.py"

pyinstaller --noconfirm --windowed --icon "app.icns" "my_app.py"

pyinstaller --noconfirm --onefile --windowed  "C:\python\qtAutoUpdateApp\my_app.py"
```

### 4、解决打包过程中的问题

在打包过程中，有时会遇到一些问题，例如打包后的可执行文件无法正常运行，或者缺少某些依赖库等。这些问题通常可以通过查看`PyInstaller`生成的日志文件来解决。`PyInstaller`会在打包过程中生成一个名为`build.log`的日志文件，其中包含了打包过程中的详细信息。你可以打开这个日志文件，查看其中的错误信息，然后根据错误信息来解决问题。

## 安装教程

1. xxxx
2. xxxx
3. xxxx

## 使用说明

1. xxxx
2. xxxx
3. xxxx

## 参与开发

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request

## 备注

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
