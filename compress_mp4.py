#!/bin/python3

import os
import ffmpeg

source_dir = "/root/temp"
target_dir = "/root/mv"


def build_dir(dir_path) -> None:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


# 子函数，显示所有文件的路径
def show_mp4_files(source_file_dir, all_files_name=[], all_files_path=[]):
    # 显示当前目录所有文件和子文件夹，放入file_list数组里
    file_list = os.listdir(source_file_dir)
    # 循环判断每个file_list里的元素是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量
        cur_path = os.path.join(source_file_dir, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            # 递归
            show_mp4_files(cur_path, all_files_name)
        else:
            # 将file_name添加进all_files里
            if file[-3:] == 'mp4':
                all_files_name.append(file)
                all_files_path.append(cur_path)
    return all_files_name, all_files_path


def compress_mp4_to_smaller_size(mp4_file_name, mp4_file_path):  # 输入为文件名, 文件路径
    # 转换的源mp4文件路径
    #stream = ffmpeg.input(mp4_file_path)
    target_mp4_dir = os.path.join(target_dir, mp4_file_name)
    build_dir(target_mp4_dir)
    target_file_path = os.path.join(target_mp4_dir, mp4_file_name)
    os.system('ffmpeg -i {0} -s 640x480 -b:v 500k -r 20 {1}'.format(mp4_file_path, target_file_path))
    #'640 X 480''码率500kbps''帧率15fps'


# 以下是主程序
if __name__ == '__main__':
    # 创建目标文件夹，如存在则不操作
    build_dir(target_dir)
    # 传入空的list接收文件名
    mp4_files_name, mp4_files_path = show_mp4_files(source_dir, [])
    # 循环打印show_files函数返回的文件名列表
    for i in range(len(mp4_files_name)):
        print("processing::", mp4_files_name[i])
        compress_mp4_to_smaller_size(mp4_files_name[i], mp4_files_path[i])
