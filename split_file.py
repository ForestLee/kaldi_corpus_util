#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
按比例把文件按比例分割
split_file.py D:\work\asr\dataset\from_wangzhongping\wav_list.txt 8 1 1
生成:
wav_list.txt.train.txt
wav_list.txt.dev.txt
wav_list.txt.test.txt

D:\work\asr\dataset\from_wangzhongping\wav_list.txt:
./CN-NORM-SC-20190119-F-27-00044073.wav
./CN-NORM-SC-20191218-M-45-10007334.wav
./CN-NORM-YU-20191218-F-19-10040410.wav
'''
import sys
import random




def split(file, train_per, dev_per, test_per):
    lines = []
    with open(file, 'r', encoding='utf-8') as infile:
        for line in infile:
            new_line = line[2:]
            lines.append(new_line)

    random.shuffle(lines)
    line_number = len(lines)
    train_number = int(line_number * train_per / 10)
    dev_number = int(line_number * dev_per / 10)
    test_number = line_number - train_number - dev_number
    print("train:" + str(train_number) + ",dev:" + str(dev_number) + ",test:"+str(test_number)+"\n")

    train_file = file+".train.txt"
    with open(train_file, 'w', encoding='utf-8') as outfile:
        for line in range(train_number):
            outfile.write(lines[line])

    dev_file = file+".dev.txt"
    with open(dev_file, 'w', encoding='utf-8') as outfile:
        for line in range(train_number, train_number+dev_number):
            outfile.write(lines[line])

    test_file = file+".test.txt"
    with open(test_file, 'w', encoding='utf-8') as outfile:
        for line in range(train_number + dev_number, train_number + dev_number + test_number):
            outfile.write(lines[line])
    print("split file done")


if __name__=='__main__':

    if len(sys.argv) > 1:
        corpus_file = sys.argv[1]
        train_per = int(sys.argv[2])
        dev_per = int(sys.argv[3])
        test_per = int(sys.argv[4])
        split(corpus_file, train_per, dev_per, test_per)

