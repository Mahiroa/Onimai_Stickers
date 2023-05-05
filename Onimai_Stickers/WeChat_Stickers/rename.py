"""对文件按 1, 2, 3, 4, 5... 的顺序重命名的功能"""

import os

path = r"D:\img_512"


def suffix_name():
    suffix_dict = {}
    error_suffix_dict = {}
    for filename in os.listdir(path):
        if filename.count('.') == 1:
            suffix = filename.split('.')[-1].lower()
            suffix_dict[suffix] = suffix_dict.get(suffix, 0) + 1
        else:
            error_suffix_dict[filename] = error_suffix_dict.get(filename, 0) + 1
    return suffix_dict, error_suffix_dict


def show(suffix_tuple: tuple):
    st0 = suffix_tuple[0]
    print("---------------------------可用改名文件---------------------------")
    for key, value in st0.items():
        print(f"后缀名：{key}\t计数：{value}")
    st1 = suffix_tuple[1]
    print("--------------------------不可用改名文件--------------------------")
    for key, value in st1.items():
        print(f"后缀名：{key}\t计数：{value}")


# 改名函数
def name_change(suffix: str):
    count = 0
    # 遍历目录下所有文件
    for filename in os.listdir(path):
        # print(filename)
        # 判断文件是否为要更改的类型
        if filename.endswith('.' + suffix):
            count += 1
            # 对旧文件名进行处理
            new_name = str(count) + "." + suffix
            # 重命名文件，即更改文件名
            os.rename(os.path.join(path, filename), os.path.join(path, new_name))


def main():
    st = suffix_name()
    show_bool = input('文件名已统计完成，是否要查看（Y/N）：')
    if show_bool == 'Y' or show_bool == '' or show_bool == 'y':
        show(st)
        while True:
            data = input("请输入要改名的文件后缀名（输入 quit() 退出）：\n")
            if data != 'quit()':
                name_change(suffix=data)
            else:
                break
    else:
        print("由于您选择不查看文件名统计结果，程序已直接退出。")


if __name__ == '__main__':
    main()
