#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'tu'
# 采用递归遍历的方式遍历图片
import os


dir_name = os.path.dirname(os.path.realpath(__file__))


origin_string = 'SYW'
replace_string = 'NNE'
floder_path = '/Users/luigi/Documents/ZT/NNEFutures/NNEFutures'
replaced_word_file_path = dir_name+"/rename_words.cfg"

def read_replaced_words_list(file_name):
    pass
    print ("replace_word_file=>"+file_name)
    with open(file_name,'r') as f:
        name_list = f.read().splitlines()
        print(name_list)
        for item in name_list:
            pass
            string_name_old = item
            string_name_new = item.replace(origin_string,replace_string)

            str_shell="sed -i \'{s/\'"+string_name_old+"\'/\'"+string_name_new+"\'/g}\' `grep "+string_name_old+" -rl "+floder_path+"`"
            os.system(str_shell)
            print("replace_string_old=>"+string_name_old+";new=>"+string_name_new)
        

def main():
    read_replaced_words_list(replaced_word_file_path)

if __name__ == '__main__':
    main()
