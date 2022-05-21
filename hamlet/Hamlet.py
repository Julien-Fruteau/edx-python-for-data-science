# "For these exercises, functions count_words_fast, read_book,
# and word_stats are already defined as in the Case 2 Videos (Videos 3.2.x):"

import pandas as pds
import os
import matplotlib.pyplot as plt
from collections import Counter

def count_words_fast(text):
    '''
    Count the number of times each word occurs in the text (str).
    Return a dictionnay where keys are unique words and values are
    word counts. Skip punctuation.
    '''
    # 1st lower case all the words
    text = text.lower()
    # 2nd, skip words:
    skips = [".",",",";",":","''",'"',"!","?"]
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))

    return word_counts

def read_book(title_path):
    '''
    Read a book and return it as a string.
    '''
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

def word_stats(word_counts):
    '''
    Return number of unique words and word frequencies
    '''
    num_unique = len(word_counts)
    counts = word_counts.values()
    return(num_unique, counts)

# Exercise 1:
# * Write a function word_count_distribution(text) that takes a book string
#   and returns a dictionary with items corresponding to the count of times
#   a collection of words appears in the translation, and values corresponding
#   to the number of number of words that appear with that frequency.
# * First use count_words_fast(text) to create a dictionary called word_counts
#   with unique words in the dictionary as keys and their frequency in the
#   book as values.
# * Next, create and return a new dictionary count_distribution with unique
#   values from word_counts as keys and their frequency as values. For example,
#   'you are what you eat' contains three words that occur once and one word
#   that occurs twice, so word_count_distribution('you are what you eat')
#   should return a dictionary {1:3, 2:1}.
# * 'Romeo and Juliet' is [stored in Hamlet/Books/English directory. Load it
#   as text using read_book]. Call word_count_distribution(text), and save the
#   result as distribution.

# text = read_book("./Books/English/Romeo and Juliet.txt")

def word_count_distribution(text):
    '''
    Returns a dictionnary which takes as keys the frequency of each independent
    word from the text argument, and key values the frequency of the key in the
    text. It makes use of count_words_fast(text) function.
    '''
    word_counts = count_words_fast(text)
    # # solution 1:
    # count_distribution = {}
    # for word in word_counts:
    #     if word_counts[word] in count_distribution:
    #         count_distribution[word_counts[word]] += 1
    #     else:
    #         count_distribution[word_counts[word]] = 1
    # # end

    # # solution 2:
    # count_distribution = Counter()
    # for freq in word_counts.values():
    #     count_distribution[freq] += 1

    # # solution 3:
    count_distribution = Counter(word_counts.values())

    return count_distribution

# distribution = word_count_distribution(text)

# Exercise 2:
# * Create a function more_frequent(distribution) that takes a word
#   frequency dictionary (like that made in Exercise 1) and outputs a
#   dictionary with the same keys as those in distribution (the number of
#   times a group of words appears in the text), and values corresponding to
#   the fraction of words that occur with more frequency than that key.
# * Call more_frequent(distribution)

def more_frequent(distribution):
    frequent = {}
    sorted_dist = distribution.most_common()
    for i in range(len(sorted_dist)):
        more_frequent = 0
        for j in range(i + 1, len(sorted_dist)):
            more_frequent += sorted_dist[j][1]
        frequent[sorted_dist[i][0]] = more_frequent
    return frequent

# more_frequent(distribution)

# Exercise 3:
# * Edit the code used to read though each of the books in our library,
#   and store the word frequency distribution for each translation of
#   William Shakespeare's "Hamlet" as a Pandas dataframe hamlets with
#   columns named "language" and "distribution". word_count_distribution
#   is preloaded from Exercise 1. How many translations are there? Which
#   languages are they translated into?

def clean_subdir(of_dir):
    '''
    Returns a list of the subdirectories of the_dir without the
    hidden file which starts with "." in mac osX.
    '''
    return [f for f in os.listdir(of_dir) if not f.startswith(".")]

hamlets = pds.DataFrame(columns=("language", "distribution"))
# book_dir = "Books"
book_dir = "./Books"
title_num = 1

for language in clean_subdir(book_dir):
    for author in clean_subdir(book_dir + "/" + language):
        for title in clean_subdir(book_dir + "/" + language + "/" + author):
# for language in book_titles:
    # for author in book_titles[language]:
    #     for title in book_titles[language][author]:
            # if title == "Hamlet":
            if title == "Hamlet.txt":
                inputfile = book_dir + "/" + language + "/" + author + "/" + \
                            title
                # inputfile = data_filepath+"Books/"+language+"/"+author+"/"+\
                #             title+".txt"
                text = read_book(inputfile)
                distribution = word_count_distribution(text)
                hamlets.loc[title_num] = language, distribution
                title_num += 1
hamlets
# There are three translations: English, German, and Portuguese.

# Exercise 4:
# * Plot the word frequency distributions of each translations on a single
#   log-log plot. Note that we have already done most of the work for you.
#   Do the distributions of each translation differ?

colors = ["crimson", "forestgreen", "blueviolet"]
handles, hamlet_languages = [], []
for index in range(hamlets.shape[0]):
    language, distribution = hamlets.language[index+1], \
                             hamlets.distribution[index+1]
    dist = more_frequent(distribution)
    plot, = plt.loglog(sorted(list(dist.keys())),\
                       sorted(list(dist.values()),reverse = True), \
                       color = colors[index], linewidth = 2)
    handles.append(plot)
    hamlet_languages.append(language)
plt.title("Word Frequencies in Hamlet Translations")
xlim    = [0, 2e3]
xlabel  = "Frequency of Word $W$"
ylabel  = "Fraction of Words\nWith Greater Frequency than $W$"
plt.xlim(xlim); plt.xlabel(xlabel); plt.ylabel(ylabel)
plt.legend(handles, hamlet_languages, loc = "upper right", numpoints = 1)
plt.show()
