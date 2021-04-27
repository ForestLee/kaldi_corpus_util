#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
例如把所有文件语料按照8:1:1（train:dev:test）的比例划分
split_file.py /home/forest/asr/dataset/from_wangzhongping/merge/changename_0427 /home/forest/asr/dataset/from_wangzhongping/merge/changename_0427/wav_list.txt 8 1 1
生成:
wav_list.txt.train.txt
wav_list.txt.dev.txt
wav_list.txt.test.txt

/home/forest/asr/dataset/from_wangzhongping/merge/changename_0427/wav_list.txt:
/home/forest/asr/dataset/from_wangzhongping/merge/changename/G9000/T0055G9000S0001.wav
/home/forest/asr/dataset/from_wangzhongping/merge/changename/G9000/T0055G9000S0002.wav
/home/forest/asr/dataset/from_wangzhongping/merge/changename/G9000/T0055G9000S0003.wav
/home/forest/asr/dataset/from_wangzhongping/merge/changename/G9000/T0055G9000S0004.wav
'''
import sys
import random
import os



def split(file, train_per, dev_per, test_per):
    lines = []
    with open(file, 'r', encoding='utf-8') as infile:
        for line in infile:
            new_line = line   #new_line = line[2:]
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

#先收集目录个数，按目录来分
def split_folder(root_path, wav_file, train_per, dev_per, test_per):
    lines = []
    folder_list = []
    with open(wav_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            new_line = line.replace("\n", "")
            segments = new_line.split("/")
            if not segments[-2] in folder_list:
                folder_list.append(segments[-2])

            lines.append(new_line)

    random.shuffle(lines)
    line_number = len(lines)
    random.shuffle(folder_list)
    folder_set_number = len(folder_list)
    train_number = int(folder_set_number * train_per / 10)
    dev_number = int(folder_set_number * dev_per / 10)
    test_number = folder_set_number - train_number - dev_number
    print("train:" + str(train_number) + ",dev:" + str(dev_number) + ",test:"+str(test_number)+"\n")

    train_file = wav_file+".train.txt"
    with open(train_file, 'w', encoding='utf-8') as outfile:
        for line in range(train_number):
            speaker_dir = root_path + "/" + folder_list[line]
            wav_files_in_one_folder = [os.path.join(dir_path, f)
                         for dir_path, _, files in os.walk(speaker_dir)
                         for f in files
                         if os.path.splitext(f)[1] == ".wav"]

            for file in wav_files_in_one_folder:
                outfile.write(file+"\n")

    dev_file = wav_file+".dev.txt"
    with open(dev_file, 'w', encoding='utf-8') as outfile:
        for line in range(train_number, train_number+dev_number):
            speaker_dir = root_path + "/" + folder_list[line]
            wav_files_in_one_folder = [os.path.join(dir_path, f)
                                       for dir_path, _, files in os.walk(speaker_dir)
                                       for f in files
                                       if os.path.splitext(f)[1] == ".wav"]

            for file in wav_files_in_one_folder:
                outfile.write(file+"\n")

    test_file = wav_file+".test.txt"
    with open(test_file, 'w', encoding='utf-8') as outfile:
        for line in range(train_number + dev_number, train_number + dev_number + test_number):
            speaker_dir = root_path + "/" + folder_list[line]
            wav_files_in_one_folder = [os.path.join(dir_path, f)
                                       for dir_path, _, files in os.walk(speaker_dir)
                                       for f in files
                                       if os.path.splitext(f)[1] == ".wav"]

            for file in wav_files_in_one_folder:
                outfile.write(file+"\n")

    print("split file done")

if __name__=='__main__':

    if len(sys.argv) > 1:
        root_path = sys.argv[1]
        wav_file = sys.argv[2]
        train_per = int(sys.argv[3])
        dev_per = int(sys.argv[4])
        test_per = int(sys.argv[5])

        split_folder(root_path, wav_file, train_per, dev_per, test_per)

