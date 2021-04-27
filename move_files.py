#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
按照文件列表copy文件
python ~/asr/dataset/kaldi_corpus_util/move_files.py /home/forest/asr/dataset/from_wangzhongping/merge/changename_0427/wav_list.txt.train.txt /home/forest/asr/dataset/from_wangzhongping/merge/changename_0427/train
python ~/asr/dataset/kaldi_corpus_util/move_files.py /home/forest/asr/dataset/from_wangzhongping/merge/changename_0427/wav_list.txt.dev.txt /home/forest/asr/dataset/from_wangzhongping/merge/changename_0427/dev
python ~/asr/dataset/kaldi_corpus_util/move_files.py /home/forest/asr/dataset/from_wangzhongping/merge/changename_0427/wav_list.txt.test.txt /home/forest/asr/dataset/from_wangzhongping/merge/changename_0427/test
'''

import os
import sys
import tqdm
import platform



def move(file_list, src_folder, dest_folder):
    file_names = []
    with open(file_list, 'r', encoding='utf-8') as infile:
        for line in infile:
            new_line = line.replace('\n','')
            file_names.append(new_line)
    print("there are " + str(len(file_names)) + " files in list file")

    src_files = [os.path.join(dir_path, f)
                 for dir_path, _, files in os.walk(src_folder)
                 for f in files
                 if os.path.splitext(f)[1] == ".wav"]

    src_files_2 = [f
                 for dir_path, _, files in os.walk(src_folder)
                 for f in files
                 if os.path.splitext(f)[1] == ".wav"]

    i = 0
    for src_file in file_names:
        if src_file in src_files_2:

            try:
                #src_wav_file = os.path.splitext(src_file)[0] + ".wav"
                i += 1
                src_wav_file = os.path.join(src_folder, src_file)
                if platform.system() == 'Linux':
                    os.system("cp " + src_wav_file + " " + dest_folder + "/")
                elif platform.system() == 'Windows':
                    os.system("copy " + src_wav_file + " " + dest_folder + "\\" + src_file)
                else:
                    print("unknow OS")
            except Exception as e:
                print('copy fail: ' + src_file)
                print(e)
        else:
            print('not found: ' + src_file)

    print("copied " + str(i) + " files done")

def move_folder(file_list, dest_folder):
    file_names = []
    src_speaker_folders = []
    with open(file_list, 'r', encoding='utf-8') as infile:
        for line in infile:
            new_line = line.replace('\n','')
            file_names.append(new_line)
            segments = new_line.split("/")
            src_speaker = ""
            for i in range(len(segments) - 1):
                if segments[i] != "":
                    src_speaker += "/" + segments[i]

            if not src_speaker in src_speaker_folders:
                src_speaker_folders.append(src_speaker)

    i = 0
    for src_speaker_folder in src_speaker_folders:
            try:
                i += 1
                if platform.system() == 'Linux':
                    os.system("cp -r " + src_speaker_folder + " " + dest_folder + "/")
                    print("cp -r " + src_speaker_folder + " " + dest_folder)
                elif platform.system() == 'Windows':
                    segments = src_speaker_folder.split("\\")
                    os.system("copy " + src_speaker_folder + " " + dest_folder + "\\" + segments[-1])
                else:
                    print("unknow OS")
            except Exception as e:
                print('copy fail: ' + src_speaker_folder)
                print(e)

    print("copied " + str(i) + " files done")

if __name__=='__main__':

    if len(sys.argv) > 2:
        # file_list = sys.argv[1]
        # src_folder = sys.argv[2]
        # dest_folder = sys.argv[3]
        # move(file_list, src_folder, dest_folder)

        file_list = sys.argv[1]
        dest_folder = sys.argv[2]
        move_folder(file_list, dest_folder)