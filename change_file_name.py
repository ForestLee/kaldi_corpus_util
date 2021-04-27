#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
修改文件名, 适配aidatatang的格式。
每一个speaker的话放在一个目录里,目录名就是说话人ID
例如  G7072/T0055G7072S0181.wav
G7072 - 说话人ID     G0001~G9999
S0181 - 该说话人索引  S0001~S9999
并且产生文件列表wav_list.txt, aidatatang_200_zh_transcript.txt

wav_list.txt:
G0002/T0055G0002S0001.wav
G0002/T0055G0002S0002.wav
G0002/T0055G0002S0004.wav

aidatatang_200_zh_transcript.txt:
T0055G0002S0001 以后 你 是 男孩子
T0055G0002S0002 兰州 哪有 买路 虎 汽车 的
T0055G0002S0004 看看 我 的 日程表
...


change_file_name.py src_path dest_path 20200827.csv /tmp/wav_list.txt /tmp/aidatatang_200_zh_transcript.txt

'''
import sys
import os
import platform
import jieba

START_WITH = "T0055"
START_FROM = 9000   #现有最大 + 1
EVERY_SPEAKER = 400  #默认每一个人400句话

def change(src_folder, dest_folder, in_file_name_corpus_dict, out_file_list, out_file_name_sentence, start, every):
    output_file_name_corpus_dict = {}
    src_files = [os.path.join(dir_path, f)
                 for dir_path, _, files in os.walk(src_folder)
                 for f in files
                 if os.path.splitext(f)[1] == ".wav"]

    start_index = 0
    every_index = 1
    for src_file in src_files:
        try:
            src_file_segments = src_file.split("/")
            src_file_wo_path = src_file_segments[-1]
            if not src_file_wo_path in in_file_name_corpus_dict:
                continue

            if every_index == 1:
                speaker_int_str = "G" + "{:0>4d}".format(start+start_index)
                speaker_dir = os.path.join(dest_folder, str(speaker_int_str))
                os.system("mkdir " + speaker_dir)
                start_index += 1

            src_wav_file = os.path.join(src_folder, src_file)
            every_str = "{:0>4d}".format(every_index)
            dest_file = START_WITH + str(speaker_int_str) + "S" + every_str + ".wav"
            if platform.system() == 'Linux':
                os.system("cp " + src_wav_file + " " + speaker_dir + "/" + dest_file)
            elif platform.system() == 'Windows':
                os.system("copy " + src_wav_file + " " + speaker_dir + "\\" + dest_file)
            else:
                print("unknow OS")

            sentence = in_file_name_corpus_dict.get(src_file_wo_path)
            output_file_name_corpus_dict[dest_file] = sentence

            every_index += 1
            if every_index > every:
                every_index = 1

        except Exception as e:
            print('change fail: ' + src_file)
            print(e)

    with open(out_file_list, 'w', encoding='utf-8') as write_file:
        for key in output_file_name_corpus_dict:
            write_file.write(key + "\n")

    with open(out_file_name_sentence, 'w', encoding='utf-8') as write_file:
        for key in output_file_name_corpus_dict:
            segments = jieba.cut(output_file_name_corpus_dict[key])
            words_line = ""
            for seg in segments:
                words_line += " " + seg.replace(" ", "")
            write_file.write(key + words_line + "\n")

def read_file_corpus(in_file_name_sentence):
    file_name_corpus = {}
    with open(in_file_name_sentence, 'r', encoding='utf-8') as infile:
        for line in infile:
            new_line = line.replace("\n", "")
            if new_line != "":
                new_line = new_line.split(",")
                file_name_corpus[new_line[0]] = new_line[1]
    return file_name_corpus

if __name__=='__main__':

    if len(sys.argv) > 2:
        start = START_FROM
        every = EVERY_SPEAKER
        src_folder = sys.argv[1]
        dest_folder = sys.argv[2]
        in_file = sys.argv[3]  #20200827.csv
        out_file_list = sys.argv[4]            #/tmp/wav_list.txt
        out_file_name_sentence = sys.argv[5]   #/tmp/aidatatang_200_zh_transcript.txt

        in_file_name_corpus_dict = read_file_corpus(in_file)
        change(src_folder, dest_folder, in_file_name_corpus_dict, out_file_list, out_file_name_sentence, start, every)