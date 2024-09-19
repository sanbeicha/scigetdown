import os
import stat
from typing import Literal
import zipfile


def zip压缩2(压缩包的路径, 待压缩的文件或目录) -> Literal[True]:
    """
    递归地将指定文件或目录压缩成zip格式的文件。

    Args:
        压缩包的路径 (str): 压缩后的zip文件保存路径。
        待压缩的文件或目录 (str): 需要被压缩的文件或目录路径。

    Returns:
        Literal[True]: 压缩完成后返回True，表示压缩成功。

    """
    # 使用递归实现的压缩
    with zipfile.ZipFile(压缩包的路径, "w", compression=zipfile.ZIP_DEFLATED) as 压缩包文件:
        父目录文本长度 = len(os.path.dirname(待压缩的文件或目录))

        def 递归压缩(父目录):
            文件路径列表 = os.listdir(父目录)
            if not 文件路径列表:
                # http://www.velocityreviews.com/forums/t318840-add-empty-directory-using-zipfile.html
                根目录 = 父目录[父目录文本长度:].replace("\\", "/").lstrip("/")
                压缩包信息 = zipfile.ZipInfo(根目录 + "/")
                压缩包文件.writestr(压缩包信息, "")
            for 路径 in 文件路径列表:
                文件绝对路径 = os.path.join(父目录, 路径)
                if os.path.isdir(文件绝对路径) and not os.path.islink(文件绝对路径):
                    递归压缩(文件绝对路径)
                else:
                    根目录 = 文件绝对路径[父目录文本长度:].replace("\\", "/").lstrip("/")
                    if os.path.islink(文件绝对路径):
                        # http://www.mail-archive.com/python-list@python.org/msg34223.html
                        压缩包信息 = zipfile.ZipInfo(根目录)
                        压缩包信息.create_system = 3
                        # long type of hex val of '0xA1ED0000L',
                        # 建立软连接
                        压缩包信息.external_attr = 2716663808
                        压缩包文件.writestr(压缩包信息, os.readlink(文件绝对路径))
                    else:
                        压缩包文件.write(文件绝对路径, 根目录, zipfile.ZIP_DEFLATED)

        递归压缩(待压缩的文件或目录)
    return True


def zip解压2(压缩包的路径, 解压目录, 允许解压路径前缀=[]) -> Literal[True]:
    """
    解压zip文件，支持保持权限和软连接。

    Args:
        压缩包的路径 (str): zip文件的路径。
        解压目录 (str): 解压的目标目录。
        允许解压路径前缀 (List[str], optional): 允许解压的文件路径前缀列表。默认为空列表，表示解压所有文件。

    Returns:
        Literal[True]: 解压成功返回True。

    """
    file = zipfile.ZipFile(压缩包的路径)
    for info in file.infolist():
        # 检查 目标文件路径 是否在 允许解压路径前缀 中
        if len(允许解压路径前缀) > 0:
            允许解压 = False
            for 路径 in 允许解压路径前缀:
                if info.filename.startswith(路径):
                    允许解压 = True
            if not 允许解压:
                # print("不允许解压", info.filename)
                continue

        文件名 = info.filename
        try:
            info.filename = 文件名.encode("cp437").decode("utf-8")
        except:
            pass
        # print("解压", 文件名)
        # continue
        目标文件路径 = os.path.join(解压目录, info.filename)
        # 解压
        权限 = info.external_attr >> 16
        if stat.S_ISLNK(权限):  # 权限 == 'lrwxr-xr-x' 权限 = stat.filemode(权限)
            软连接位置 = file.open(info).read()  # 读入软连接的位置
            # 检查 目标文件路径 是否存在，如果存在就删除，防止创建失败
            if os.path.exists(目标文件路径):
                os.remove(目标文件路径)
            # ic(目标文件路径, 软连接位置)
            os.symlink(软连接位置, 目标文件路径)
        else:
            # 删除文件 重新解压
            # print("解压", 文件名)
            if os.path.exists(目标文件路径):
                # 检查是否为文件
                if os.path.isfile(目标文件路径):
                    os.remove(目标文件路径)

            file.extract(info, path=解压目录)
            # print("权限", stat.filemode(权限))
            # 文件是否存在
            if os.path.exists(目标文件路径):
                os.chmod(目标文件路径, 权限)

    return True


if __name__ == "__main__":
    压缩包的路径 = "/Users/chensuilong/Downloads/my_app.app.zip"
    解压目录 = r"/Users/chensuilong/Desktop/pythonproject/autotest/dist/"
    zip解压2(
        压缩包的路径,
        解压目录,
        允许解压路径前缀=[
            "my_app.app/Contents/",
        ],
    )
