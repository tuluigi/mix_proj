#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'tu'
# 采用递归遍历的方式遍历图片
import os

# 需要扫描的图片的目录
assert_folder  = '/Users/luigi/Documents/ZT/NNEFutures/NNEFutures/Assets.xcassets'
project_floder = '/Users/luigi/Documents/ZT/NNEFutures'
# 扩展文件数组
extension_list = [".png", ".jpg", ".pdf"]
# 黑名单
black_name_list = ["ALIPAY_channel_choose", "ALIPAY_channel_default", "UNIONPAY_channel_choose",
                   "UNIONPAY_channel_default", "icon_ doubt"]

replace_imagename_dic = {}

string_replace_old = 'ant_'
string_replace_new = 'nne_'


def recurve_opt(root_path):
    # file 文件名
    for file in os.listdir(root_path):
        # target_file完整目录路径
        target_file = os.path.join(root_path, file)
        # print("target_file=>"+target_file)
        # 文件路径最后的部分
        base_dir = os.path.basename(target_file)

        if os.path.isdir(target_file) and (".imageset" in base_dir):
            pass
            # 得到要替换的内容string
            file_name = base_dir.replace(".imageset", "");
            if (string_replace_old in file_name):
                pass
                file_name_new = file_name.replace(string_replace_old, string_replace_new);
                target_file_new = target_file.replace(file_name, file_name_new);
                print("file==>"+file+";file_name=>" + file_name + "; file_name_new=>" + file_name_new+"\n target_file=>"+target_file)
                # 保存到数组中
                replace_imagename_dic[target_file] = target_file_new;

                os.rename(target_file,target_file_new)
                str_shell="sed -i \'{s/\'"+file_name+"\'/\'"+file_name_new+"\'/g}\' `grep "+file_name+" -rl "+project_floder+"`"
                os.system(str_shell)

                rename_imageset(target_file_new)
        else:
            if os.path.isdir(target_file):
                pass
                recurve_opt(target_file)

def rename_imageset(root_path):
    pass
    base_dir = os.path.basename(root_path)
    base_dir = base_dir.replace(".imageset", "");
    for file in os.listdir(root_path):
        # target_file完整目录路径
        target_file = os.path.join(root_path, file)
        # print("target_file=>"+target_file)
        # 文件路径最后的部分

        
        (path, extension) = os.path.splitext(target_file);
        print("path=>"+path+";extension=>"+extension)
        if (extension in extension_list) and (os.path.isfile(target_file)):
            pass
            
            file_name = file.replace(extension,'')
            file_name_new = base_dir
            if ("@2x" in file_name):
                pass
                file_name_new=base_dir+"@2x";
            elif ("@3x" in file_name):
                pass
                file_name_new=base_dir+"@3x"
            #file_name_new=file_name_new+extension
            #重命名文件名
            target_file_new=os.path.join(root_path, file_name_new+extension)
            print("---------target_file_new=>"+target_file_new)
            os.rename(target_file,target_file_new)
            
            #替换imageSet
            imgeset_content_json_path=root_path+"/Contents.json"
            str_shell="sed -i \'{s/\'"+file_name+"\'/\'"+file_name_new+"\'/g}\' `grep "+file_name+" -rl "+imgeset_content_json_path+"`"
            os.system(str_shell)



def main():
    recurve_opt(assert_folder)


if __name__ == '__main__':
    main()
