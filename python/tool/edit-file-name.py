# coding=utf-8
"""
    在windows下运行！！！
    使用当前文件请下载Python2.7的版本。
    安装Python之后，用IDLE打开当前文件，使用F5运行
    这是一个修改图片名字的小程序。
"""

import os


def rename():
    path = "C:\\Users\\lyfw2\\OneDrive\\Photos"         # 修改文件名所在的完整文件夹路径,请复制完整文件夹路径之后把有'\'的加多一个'\'
    files = os.listdir(path)                            # 获取path路径下的所有名字的列表

    for file in files:                                  # 循环获取文件名
        """
        # 这是一个修改完整的文件名的方法,如果需要请把引号去掉，再把引号下面的去掉
        if os.path.isdir(file):
            continue
        old_name = os.path.join(path, file)
        file_type = os.path.splitext(file)[1]
        name = 'XXX' + file_type
        new_name = os.path.join(path, name)
        os.rename(old_name, new_name)
        """
        # 判断这文件名前面5个字母是否与之匹配，不等于就跳过(如果要修改其他字数把5改成要修改的字数的个数)
        if file[0:5] != 'SPSCF':
            continue
        else:
            old_name = os.path.join(path, file)         # 合并文件的路径
            file_type = os.path.splitext(file)[1]       # 获取当前文件的后缀名或是扩展名
            filename = os.path.splitext(file)[0]        # 获取当前文件名
            name = 'CHD' + filename[5:] + file_type     # 需要修改的文件名（filename[5:]可以根据你要改的字数的个数修改数字5，跟判断的尾数要相同）
            new_name = os.path.join(path, name)         # 合并文件的路径
            os.rename(old_name, new_name)               # 修改名字！


# 此处不要删除。
if __name__ == '__main__':
    rename()
