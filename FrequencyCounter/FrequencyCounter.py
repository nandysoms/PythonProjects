import requests
from bs4 import BeautifulSoup
import operator


def get_words(url):
    all_words = []
    source_words = requests.get(url).text
    words = BeautifulSoup(source_words, "html.parser")
    content0 = words.get_text()
    content_list = content0.lower().split()
    for each_word in content_list:
         all_words.append(each_word)
    clean_up_all_words(all_words)


def clean_up_all_words(all_words):
    all_clean_words = []
    for word in all_words:
        symbols = r'~!@#$%^&*()_+{}[]|\:;"\'<>,./?='
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i],"")
        if len(word) > 0:
            all_clean_words.append(word)
    create_dictionary(all_clean_words)


def create_dictionary(all_clean_words):
    dict = {}
    for word in all_clean_words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    for key, value in sorted(dict.items(), key=operator.itemgetter(1)):
        print(key, value)


get_words('http://watchseries.fi/')
