import os
import sys
import random
import numpy as np
import time
import jieba


def replace_number(file, out_file):
    with open(file, 'r', encoding='utf-8') as infile:
        with open(out_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                line1 = line.replace("\n", "")
                words = line1.split(" ")
                new_words = []
                for word in words:
                    if word != "":
                        new_words.append(word)
                new_line = ""
                i = 0
                count = len(new_words)
                for word in new_words:
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
                        new_line = new_line + " " + new_word
                outfile.write("BAC009S0723W0478 " + new_line + '\n')


def jieba_segment(file, out_file):
    with open(file, 'r', encoding='utf-8') as infile:
        with open(out_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                line1 = line.replace("\n", "")
                words = line1.split(" ")
                new_words = []
                for word in words:
                    if word != "":
                        new_words.append(word)
                new_line = ""
                i = 0
                count = len(new_words)
                for word in new_words:
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
                    else:
                        new_word = word

                    if i == 1:
                        new_line = new_word
                    else:
                        new_line = new_line + new_word

                segments = jieba.cut(new_line)
                seg_line = ""
                for seg in segments:
                    seg_line = seg_line + " " + seg
                outfile.write("BAC009S0723W0478 " + seg_line + '\n')

def genarate_words(file, out_file):
    words_set = set()
    with open(file, 'r', encoding='utf-8') as infile:
        with open(out_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                line1 = line.replace("\n", "")
                words = line1.split(" ")
                new_words = []
                for word in words:
                    if word != "":
                        new_words.append(word)
                new_line = ""
                i = 0
                count = len(new_words)
                for word in new_words:
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
                    else:
                        new_word = word

                    if i == 1:
                        new_line = new_word
                    else:
                        new_line = new_line + new_word

                segments = jieba.cut(new_line)
                seg_line = ""
                for seg in segments:
                    words_set.add(seg)

            for word in words_set:
                outfile.write(word + '\n')

def shuffle(file):
    lines = []
    with open(file, 'r', encoding='utf-8') as infile:
        for line in infile:
            lines.append(line)

    random.shuffle(lines)
    shuffle_file = file+".shuffle"
    with open(shuffle_file, 'w', encoding='utf-8') as outfile:
        for line in lines:
            outfile.write(line)
    print("shuffle file done")
    return shuffle_file

if __name__=='__main__':

    if len(sys.argv) > 1:
        corpus_file = sys.argv[1]

        #replace number
        #out_file = sys.argv[1]+".no_number.txt"
        #replace_number(corpus_file, out_file)

        #jieba分词
        #out_file_jieba = sys.argv[1] + ".jieba.txt"
        #jieba_segment(corpus_file, out_file_jieba)

        #生成词典
        out_file_words = sys.argv[1] + ".words.txt"
        genarate_words(corpus_file, out_file_words)

