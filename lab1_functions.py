#import sys for printing out utf-8 strings
import sys

#some utility functions for viewing non-ascii output, I had trouble viewing the output so I made these
#also much nicer than viewing output in the terminal
def view_utf8_string(string):
    '''This function prints out a utf8 string'''

    sys.stdout.buffer.write(string.encode('utf-8'))

def write_ouput(object):
    '''This fucntion writes a python object to the output file for viewing'''

    with open('output', 'w', encoding='utf-8') as f:
        f.write(str(object))

#functions used to complete lab 1
def get_count_dict(count_string):
    '''This function takes in a string of words and their counts from a Hadoop map reduce and returns
    a dictionary of the words and their counts. Each word is a key, each count a value.'''

    #split the string into a list
    split_string = count_string.split('\n')

    #create a list of lists where first element in each sub list is word, second is count
    split_list = [l.split('\t') for l in split_string]
    
    #create a dictionary where each key is the word and each value the count
    split_dict = {a[0]:int(a[1]) for a in split_list}

    return split_dict

def get_top_n_words(count_dict, n):
    '''This function takes a dictionary generated by the get_count_dict fucntion and an integer value
    n. It returns the top n key-value pairs based on word count.'''

    return sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:n]

def calculate_richness(count_dict):
    '''This function takes in a dictionary of words and their counts and returns
    the ratio of unique words to the total number of words.'''

    #calculate the total number of words
    num_words = sum(count_dict.values())

    #get unique words by finding the length of the dictionary. Each Key-Value
    #pair represents a unique word and its count
    unique_words = len(count_dict)

    return round(unique_words/num_words, 4)

#Store the filepath to the map reduce output
path = 'clean shakespeare'

#open the file path and read in the word counts
with open(path, 'r', encoding = 'UTF-8') as f:
    word_count = f.read()

#get a dictionary of words and word counts
counts = get_count_dict(word_count)
#get the top 10 counts and store the output in the output file
write_ouput(get_top_n_words(counts, 10))
