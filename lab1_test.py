#load in functions from the lab1_fucntions file
from lab1_functions import *

#read in shakespeare
path = 'clean shakespeare'
with open(path, 'r', encoding = 'UTF-8') as f:
    shake_word_count = f.read()

#read in austen
path = 'clean austen'
with open(path, 'r', encoding = 'UTF-8') as f:
    austen_word_count = f.read()

#get word dictionaries for shakespeare and austen
shake_word_dict = get_count_dict(shake_word_count)
austen_word_dict = get_count_dict(austen_word_count)

#write results to output file
write_ouput("""Shakespeare's richness: '{}'
Austen's richness: '{}'
                
Shakespeare has a richer vocabulary than Austen.""".format(calculate_richness(shake_word_dict),
                                                           calculate_richness(austen_word_dict)))