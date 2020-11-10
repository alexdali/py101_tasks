"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

if __name__ == '__main__':
    pass

    import argparse
    import os
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    parser = argparse.ArgumentParser(description='Words frequency script')

    parser.add_argument('target_file', action="store", help="path to target text file")

    args = parser.parse_args()

    target_f = args.target_file

    if os.path.isfile(target_f):

        file_name = os.path.basename(target_f)

        stop_words = set(stopwords.words('english'))

        file = open(target_f,'r')
        f_content = file.read()
        file.close()

        # tokenizer for words only, excludes punctuation marks
        reg_tokenizer = nltk.RegexpTokenizer(r'\w+')

        word_token = reg_tokenizer.tokenize(f_content)
        # filter list, excludes stop words
        filtered_list = [w.lower() for w in word_token if not w.lower() in stop_words]
        # frequency distribution
        fdist = nltk.FreqDist(w for w in filtered_list)
        # the 100 most frequent words
        freq_top100 = fdist.most_common(100)

        print('the file {} contains only {} words, \nof which the top 100 in frequency:'.format(file_name, len(filtered_list)))

        for index, word_freq in enumerate(freq_top100,1):
            print('{}. {}: {} times'.format(index, word_freq[0],word_freq[1]))

        # set of unique words
        set_list = set(filtered_list)

        print('\ntotal unique words in the file: ' + str(len(set_list)))

    else:
        print('file not exist')