#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
根据最新的文件，重新生成aidatatang_200_zh_transcript.txt, 新文件名aidatatang_200_zh_transcript.txt.new.txt
generate_file_name.py D:\\work\\asr\\dataset\\self_test_corpus\\test D:\\work\\asr\\dataset\\self_test_corpus\\transcript\\aidatatang_200_zh_transcript.txt
'''

from tqdm import tqdm
import sys

import wave
import os
import numpy as np
import platform

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
                    name_content_dict[name] = content
    return name_content_dict

def gen_new_name_content_dict(root, transcript, ext=".wav"):
    name_content_dict = get_name_content_dict(transcript)
    new_name_content_dict = {}

    src_files = [os.path.join(dir_path, f)
                 for dir_path, _, files in os.walk(root)
                 for f in files
                 if os.path.splitext(f)[1] == ext]

    for src_file in tqdm(src_files, ascii=True):
        try:
            src_file_name = os.path.splitext(src_file)[0]
            if platform.system() == 'Linux':
                src_file_name_splits = src_file_name.split("\/")
            elif platform.system() == 'Windows':
                src_file_name_splits = src_file_name.split("\\")
            else:
                print("unknow OS")

            only_file_name = src_file_name_splits[-1]
            sentense = name_content_dict[src_file_name_splits[-1]]
            new_name_content_dict[only_file_name] = sentense
        except Exception as e:
            print('gen_new_name_content_dict fail: ' + src_file)
            print(e)

    return new_name_content_dict


if __name__ == '__main__':
    if len(sys.argv) > 2:
        corpus_path = sys.argv[1]
        transcript = sys.argv[2]
        new_name_content_dict = gen_new_name_content_dict(corpus_path, transcript, '.wav')
        new_transcript_file = transcript + ".new.txt"
        with open(new_transcript_file, 'w', encoding='utf-8') as outfile:
            for name in new_name_content_dict:
                outfile.write(name + " " + new_name_content_dict[name] + "\n")