#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
根据语料生成词典
generate_lexicon.py D:\work\asr\dataset\from_wangzhongping\20200827.csv
生成lexicon.txt

D:\work\asr\dataset\from_wangzhongping\20200827.csv:
CN-NORM-ZJ-20191227-F-37-00003384.wav,查从北京飞南京的飞机几点走
CN-NORM-ZJ-20191227-F-37-00003383.wav,北京飞南京多久能到
CN-NORM-ZJ-20191227-F-37-00003382.wav,查下午北京去南京的飞机

'''
import sys
import random
import jieba


def replace_number(sentence):
    line1 = sentence.replace("\n", "")
    new_line = ""
    i = 0
    for word in line1:
        i += 1
        if word == '0':
            new_word = '零'
        elif word == '1':
            new_word = '一'
        elif word == '2':
            new_word = '二'
        elif word == '3':
            new_word = '三'
        elif word == '4':
            new_word = '四'
        elif word == '5':
            new_word = '五'
        elif word == '6':
            new_word = '六'
        elif word == '7':
            new_word = '七'
        elif word == '8':
            new_word = '八'
        elif word == '9':
            new_word = '九'
        elif word == '.':
            new_word = '点'
        else:
            new_word = word

        if i == 1:
            new_line = new_word
        else:
            new_line = new_line + new_word
    return new_line


def shuffle(file):
    lines = []
    with open(file, 'r', encoding='utf-8') as infile:
        for line in infile:
            lines.append(line)

    random.shuffle(lines)
    shuffle_file = file+".shuffle.txt"
    with open(shuffle_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            outfile.write(line)
    print("shuffle file done")
    return shuffle_file

def shuffle_2(file):
    lines = []
    words_set = set()
    with open(file, 'r', encoding='utf-8') as infile:
        for line in infile:
            #new_line=line[2:]
            new_line = line.replace("\n", "")
            new_line = new_line.split(",")
            no_number_line = replace_number(new_line[1])
            segments = jieba.cut(no_number_line)
            words_line = ""
            for seg in segments:
                words_line += " " + seg.replace(" ", "")
                new_word = seg.replace(" ", "")
                if new_word != "\n" and new_word != "":
                    words_set.add(new_word)

            lines.append(new_line[0].replace(".wav", "") + words_line + "\n")

    random.shuffle(lines)
    shuffle_file = file+".shuffle.txt"
    with open(shuffle_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            outfile.write(line)
    print("shuffle file done")
    return words_set

if __name__=='__main__':

    if len(sys.argv) > 1:
        corpus_file = sys.argv[1]
        words_set = shuffle_2(corpus_file)
        lexicon_file = corpus_file + ".lexicon.txt"
        with open(lexicon_file, 'w', encoding='utf-8') as lexiconfile:
            for word in words_set:
                lexiconfile.write(word + "\n")


