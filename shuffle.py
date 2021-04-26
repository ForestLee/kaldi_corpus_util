import os
import sys
import random
import numpy as np
import time
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
    with open(file, 'r', encoding='utf-8') as infile:
        for line in infile:
            #new_line=line[2:]
            new_line = line.replace("\n", "")
            new_line = new_line.split(",")
            no_number_line = replace_number(new_line[1])
            segments = jieba.cut(no_number_line)
            words_set = ""
            for seg in segments:
                words_set += " " + seg.replace(" ", "")

            lines.append(new_line[0].replace(".wav", "") + words_set + "\n")

    random.shuffle(lines)
    shuffle_file = file+".shuffle.txt"
    with open(shuffle_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            outfile.write(line)
    print("shuffle file done")
    return shuffle_file

if __name__=='__main__':

    if len(sys.argv) > 1:
        corpus_file = sys.argv[1]
        shuffle_2(corpus_file)

