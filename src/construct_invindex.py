import os.path
import re
import sqlite3

DATA_PATH = "./dataset/maildir"
INDEX_PATH = "./output/invindex_db"

# HELPER FUNCTIONS

punctre = re.compile('[%s]' % re.escape(string.punctuation))

def walk_os(root):
    for dirname, subdirnames, filenames in os.walk(root):
        for filename in filenames:
            yield os.path.join(dirname, filename)

def gen_open(filenames):
    for filename in filenames:
        with open(filename) as f:
            yield f.read().replace('\n', ' ')

def strip_punct(files):
    for file in files:
        nopunct = punctre.sub('',file)
        yield nopunct

def stem_words(files):
    pass
    return files

def exclude_stop_words(files):
    pass
    return files


# MAIN FUNCTIONS

def constructInvIndex():
    # file pre_process: tokenization, stemming, exclude stop words
    filenames = walk_os(DATA_PATH)
    opened_files = gen_open(filenames)
    stripped_files = strip_punct(opened_files)
    stemmed_files = stem_words(stripped_files)
    no_stop_word_files = exclude_stop_words(stemmed_files)
    prepared_files = no_stop_word_files

    inv_index = {}
    for email in prepared_files:
        words = email.split()
        for word in words:
            



if __name__ == "__index__"
    constructInvIndex()
