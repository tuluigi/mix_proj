#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'tu'
# 采用递归遍历的方式遍历图片
import os


dir_name = os.path.dirname(os.path.realpath(__file__))


string_prefix = '  #define '
floder_path = '/Users/luigi/Documents/ZT/NNEFutures/NNEFutures/'
replaced_word_file_path = "/Users/luigi/Documents/ZT/NNEFutures/Mix_FuncationNames.h"
dict_replace = {}

def read_content(filePath):
    pass
    file = open(filePath)
    for line in file:
        pass
        if line.startswith(string_prefix):
            pass

            line_after = line.replace(string_prefix,'')
            #print("line_after--->"+line_after)
            list_line = line_after.split()
            #print("list_line=>"+list_line)

            if len(list_line)==2:
                pass
                dict_replace[list_line[0]]=list_line[1]
                #print("dict---key=>"+list_line[0]+";value=>"+dict_replace[list_line[0]])
    file.close()

    replace_string(dict_replace)

def replace_string(dict):
    # type: (object) -> object
    pass
    for (k,v) in dict.items():
        pass
        string_name_old = k
        string_name_new = v

        str_shell="sed -i \'{s/\'"+string_name_old+"\'/\'"+string_name_new+"\'/g}\' `grep "+string_name_old+" -rl "+floder_path+"`"
        print("str_shell=>"+str_shell)
        os.system(str_shell)
        #print("replace_string_old=>"+string_name_old+";new=>"+string_name_new)

def main():
    read_content(replaced_word_file_path)

if __name__ == '__main__':
    main()
