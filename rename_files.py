#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
把目录下*.pcm文件名改成其对应的text的名字，
rename_files.py D:\\work\\asr\\dataset\\self_test_corpus\\test D:\\work\\asr\\dataset\\self_test_corpus\\transcript\\aidatatang_200_zh_transcript.txt
'''

from tqdm import tqdm
import sys

import wave
import os
import numpy as np

def get_name_content_dict(transcript_file):
    name_content_dict = {}
    with open(transcript_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            new_line = line.replace("\n", "")
            if new_line != "":
                offset = new_line.find(" ")
                if offset != -1:
                    name = new_line[0:offset]
                    content = new_line[offset+1:]
                    name_content_dict[name] = content.replace(" ", "")
    return name_content_dict

def rename_dir(root, transcript, ext=".pcm"):
    name_content_dict = get_name_content_dict(transcript)

    src_files = [os.path.join(dir_path, f)
                 for dir_path, _, files in os.walk(root)
                 for f in files
                 if os.path.splitext(f)[1] == ext]

    for src_file in tqdm(src_files, ascii=True):
        try:
            src_file_name = os.path.splitext(src_file)[0]
            src_file_name_splits = src_file_name.split("\\")
            dest_file_name = name_content_dict[src_file_name_splits[-1]]
            abs_path = ""
            for seg in range(len(src_file_name_splits) - 1):
                abs_path += src_file_name_splits[seg] + "\\"
            os.rename(src_file_name + ".pcm", abs_path + dest_file_name + ".pcm")
        except Exception as e:
            print('rename fail: ' + src_file)
            print(e)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        corpus_path = sys.argv[1]
        transcript = sys.argv[2]
        rename_dir(corpus_path, transcript, '.pcm')