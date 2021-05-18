#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
把文件中非utf-8的内容删除，并且打印出来
delete_non_utf8.py text

'''

import sys



def isUTF8(text):
    try:
        text = str(text, 'UTF-8', 'strict')
        return True
    except UnicodeDecodeError:
        return False

def findNoneUTF8(text):
        if -1 != text.find(u"\u3000"):
            return True
        if -1 != text.find(u"\u0009"):
            return True
        if -1 != text.find(u"\u0020"):
            return True
        if -1 != text.find(u"\u000d"):
            return True

        return False


def delete_utf8(input_file, output_file):
    inFile = open(input_file, 'r', encoding="utf-8")
    outFile = open(output_file,'w', encoding="utf-8")


    while True:
        line_str = inFile.readline()
        if line_str:
            new_line_str = line_str.replace(" ", "")
            new_line_str = new_line_str.replace("\n", "")
            new_line_str = new_line_str.replace("\t", "")
            if findNoneUTF8(new_line_str):
                print("none utf-8 line:" + line_str + "\n")
                #print("none utf-8 line:" + line_str.replace(u"\u3000", "") + "\n")
                outFile.write(line_str.replace(u"\u3000", ""))
            else:
                outFile.write(line_str)
        else:
            break

    inFile.close()
    outFile.close()



if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = input_file + ".no_utf8"
        delete_utf8(input_file, output_file)