import os
import requests
import operator
from bs4 import BeautifulSoup
from collections import Counter


'''Function defining the web-crawler/core 
spider, which will fetch information from 
a given website, and push the contents to 
the second  function clean_wordlist()'''

def start(url):

    wordlist = []
    source_code = requests.get(url).text
    #print ("Soiurce code", source_code)


    #BeautifulSoup object which will
    #ping the requested url for data
    soup = BeautifulSoup(source_code, 'html.parser')
    #print ("Soup", soup)

    # Text in given web-page is stored under
    # the <div> tags with class <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text
        #print (content)

        # use split() to break the sentence into
        # words and convert them into lowercase
        words = content.lower().split()
        #print (words)
        for word in words:
            #print ("####",word)
            wordlist.append(word)
            #print (wordlist)
        clean_wordlist(wordlist)


def clean_wordlist(wordlist):
    clean_list = []
    for each_word in wordlist:
        #print (each_word)
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '

        for i in range(0, len(symbols)):
            #print (i)
            word =each_word.replace(symbols[i], '')
            #print (len(word))
        if len(each_word)>0:
            clean_list.append(each_word)
                #print (clean_list)

    create_dictionary(clean_list)

            # Creates a dictionary conatining each word's
            # count and top_20 ocuuring words
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        #print (word_count)
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    #for key, value in sorted(word_count.items(),
                             #key=operator.itemgetter(1)):
            #print ("% s : % s " % (key, value))

    c = Counter(word_count)
#print (c)
    top = c.most_common(10)
    print (top)





        # Driver code
if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/programming-language-choose/")

