#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'tu'
#采用递归遍历的方式遍历图片
import os
#from PIL import Image
suffer = 'xy_'
#需要扫描的图片的目录
assert_folder = '/Users/luigi/Documents/SYW/Test/zt-ios/ZTFutures'

#需要替换的文件对应的目录
project_floder = '/Users/luigi/Documents/SYW/Test/zt-ios/ZTFutures'
#不带有后缀的图片名
file_name_list = []
#带有后缀的文件图片
full_file_list=[]
#file_name_list = ['arrow_down','default_header','icon_star_select']
def recurve_opt(root_path):
    for file in os.listdir(root_path):
        target_file = os.path.join(root_path, file)
        if os.path.isfile(target_file):
            (path, extension) = os.path.splitext(target_file)
            
            file_name = file.replace(extension,'')
            count = target_file.count(file_name)
           
            if (extension == '.jpg' or extension == '.png' or extension == '.pdf') and (count==2):

                #替换后的文件名，eg:zt_xxx.jpg
            	rename_target_file = target_file.replace(file,suffer+file)
                rename_target_file = rename_target_file.replace("@2x","");
                rename_target_file = rename_target_file.replace("@3x","");
                os.rename(target_file,rename_target_file)

                #完整的文件名给加入到full_file_list； eg icon_home.png; 用来以后替换Assert的content.json中的
                if file not in full_file_list:
                    full_file_list.append(file)
                
                #记录修改过的file_name eg:icon_home 用来以后替换代码中的
                if file_name not in file_name_list :
                    file_name_list.append(file_name)
                    print "将要修改的文件为->"+file_name
        else:
            recurve_opt(target_file)


def rename_dir_opt(root_path):
    #print  "查询到namelist->"+','.join(file_name_list)
    for file in os.listdir(root_path):
        target_file = os.path.join(root_path, file)

        #文件路径最后的部分
        base_dir = os.path.basename(target_file)
        if os.path.isdir(target_file) and (".imageset" in base_dir):

            file_name = base_dir.replace(".imageset","")
            #print("扎到符合条件name=>" + file_name)
            if file_name in file_name_list:
                # print  "需要重名文件夹->"+target_file
                #替换后的文件名，eg:zt_xxx.jpg
            	rename_target_file = target_file.replace(base_dir,suffer+base_dir)
                # print("rename dir =>",rename_target_file)
                os.rename(target_file,rename_target_file)

               #print 'rename_target_file=>' + rename_target_file
        else:
            if os.path.isdir(target_file):
                rename_dir_opt(target_file)
            else:
                continue;

def replace_file_name():
    print  "查询到namelist->"+','.join(file_name_list)
    #os.system('cd '+ project_floder)
    for file_name in file_name_list:
        
        origin_file_name = '\\"'+file_name+'\\"'
        after_file_name = '\\"'+suffer+file_name+'\\"'
        
        str_shell="sed -i \'{s/\'"+origin_file_name+"\'/\'"+after_file_name+"\'/g}\' `grep "+origin_file_name+" -rl "+project_floder+"`"
        
        
        #print "shell cmd==>"+str_shell
        print('替换代码中图片'+file_name+'--->'+suffer+file_name)
        os.system(str_shell)

    for item_file_name in full_file_list:
        rigin_item_file_name = '\\"'+item_file_name+'\\"'
        after_item_file_name = '\\"'+suffer+item_file_name+'\\"'
        
        str_full_shell="sed -i \'{s/\'"+rigin_item_file_name+"\'/\'"+after_item_file_name+"\'/g}\' `grep "+rigin_item_file_name+" -rl "+project_floder+"`"
        
        
        print "shell cmd==>"+str_full_shell
        print('替换图片名'+rigin_item_file_name+'--->'+after_item_file_name)
        os.system(str_full_shell)

def main():
    recurve_opt(assert_folder)
    rename_dir_opt(project_floder)
    replace_file_name()
if __name__ == '__main__':
    main()
