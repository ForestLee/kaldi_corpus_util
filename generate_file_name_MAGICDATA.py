#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
把MAGICDATA某个目录下TRANS.txt文件格式改成aidatatang_200_zh_transcript.txt对应格式
generate_file_name_MAGICDATA.py Z:\\李林峰\\tmp\\TRANS.txt
'''

from tqdm import tqdm
import sys

import wave
import os
import numpy as np
import jieba

def get_name_content_dict(transcript_file):
    name_content_dict = {}
    with open(transcript_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            new_line = line.replace("\n", "")
            new_line = new_line.replace("\t", " ")
            if new_line != "":
                segments = new_line.split(" ")
                name = segments[0].replace(".wav", "")
                content = segments[2]

                jieba_segments = jieba.cut(content)
                words_line = ""
                for seg in jieba_segments:
                    words_line += " " + seg.replace(" ", "")

                name_content_dict[name] = words_line
    return name_content_dict


if __name__ == '__main__':
    if len(sys.argv) > 1:
        transcript = sys.argv[1]

        new_name_content_dict = get_name_content_dict(transcript)
        new_transcript_file = transcript + ".new.txt"
        with open(new_transcript_file, 'w', encoding='utf-8') as outfile:
            for name in new_name_content_dict:
                outfile.write(name + new_name_content_dict[name] + "\n")