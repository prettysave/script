#!/usr/bin/env python
# coding:utf-8

import os
import shutil

PATH_BASE = ""


def build_path(source_path, path_list):
    file_list = os.listdir(source_path)
    # print(file_list)
    for file in file_list:
        if file[0] != '.':
            sub_path = os.path.join(source_path, file)
            if os.path.isdir(sub_path):
                build_path(sub_path, path_list)
            else:
                path_list[file] = sub_path
                # path_list.append(sub_path)


def mv_file(source_path):
    path_dict = {}
    build_path(source_path, path_dict)

    for file in path_dict:
        print(file)
        print(path_dict[file])

        shutil.move(path_dict[file], os.path.join(source_path, file))


if __name__ == '__main__':
    mv_file(PATH_BASE)
