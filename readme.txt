
#####################################
#        pcm to wav                 #
#####################################
把目录下*.pcm转变成*.wav
pcm_2_wav.py D:\work\asr\dataset
前：
D:\work\asr\dataset\CN-NORM-SC-20190119-F-27-00044073.pcm
D:\work\asr\dataset\CN-NORM-SC-20191218-M-45-10007334.pcm
D:\work\asr\dataset\CN-NORM-YU-20191218-F-19-10040410.pcm
后：
D:\work\asr\dataset\CN-NORM-SC-20190119-F-27-00044073.wav
D:\work\asr\dataset\CN-NORM-SC-20191218-M-45-10007334.wav
D:\work\asr\dataset\CN-NORM-YU-20191218-F-19-10040410.wav

#####################################
#        根据语料生成词典              #
#####################################
generate_lexicon.py D:\work\asr\dataset\from_wangzhongping\20200827.csv
生成lexicon.txt

D:\work\asr\dataset\from_wangzhongping\20200827.csv的内容:
CN-NORM-ZJ-20191227-F-37-00003384.wav,查从北京飞南京的飞机几点走
CN-NORM-ZJ-20191227-F-37-00003383.wav,北京飞南京多久能到
CN-NORM-ZJ-20191227-F-37-00003382.wav,查下午北京去南京的飞机

#####################################
#        按比例把文件按比例分割         #
#####################################
例如把所有文件语料按照8:1:1（train:dev:test）的比例划分
split_file.py D:\work\asr\dataset\from_wangzhongping\wav_list.txt 8 1 1
生成:
wav_list.txt.train.txt
wav_list.txt.dev.txt
wav_list.txt.test.txt

D:\work\asr\dataset\from_wangzhongping\wav_list.txt:
./CN-NORM-SC-20190119-F-27-00044073.wav
./CN-NORM-SC-20191218-M-45-10007334.wav
./CN-NORM-YU-20191218-F-19-10040410.wav

#####################################
#        拷贝文件                    #
#####################################
按照文件列表copy文件到指定目录
move_files.py D:\tmp\1\file_list.txt.train.txt D:\tmp\1 D:\tmp\train\
把D:\tmp\1中文件名出现在file_list.txt.train.txt中的文件copy到D:\tmp\train\

move_files.py D:\tmp\1\file_list.txt.dev.txt D:\tmp\1 D:\tmp\dev\
move_files.py D:\tmp\1\file_list.txt.test.txt D:\tmp\1 D:\tmp\test\