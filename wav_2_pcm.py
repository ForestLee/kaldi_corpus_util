#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
把目录下*.wav转变成*.pcm
wav_2_pcm.py D:\\work\\asr\\dataset\\self_test_corpus\\test

'''

from tqdm import tqdm
import sys

import wave
import os
import numpy as np


def is_wav(f):
    res = True
    try:
        wave.open(f)
    except wave.Error as e:
        res = False
    return res


def wav2pcm(wav_file, pcm_file, data_type=np.int16):
    if is_wav(wav_file):
        f = open(wav_file, "rb")
        f.seek(0)
        f.read(44)
        data = np.fromfile(f, dtype=data_type)
        data.tofile(pcm_file)
        f.close()


def convert_dir(root, ext=".wav"):
    """ 把一个文件夹内的wav，转成pcm,去掉文件头上44个字节
        Args:
            root 文件夹根目录
            ext wav文件的扩展名
    """

    src_files = [os.path.join(dir_path, f)
                 for dir_path, _, files in os.walk(root)
                 for f in files
                 if os.path.splitext(f)[1] == ext]

    for src_file in tqdm(src_files, ascii=True):
        try:
            pcm_file = os.path.splitext(src_file)[0] + ".pcm"
            wav2pcm(src_file, pcm_file)
        except Exception as e:
            print('Convert fail: ' + src_file)
            print(e)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        corpus_path = sys.argv[1]
        convert_dir(corpus_path, '.wav')