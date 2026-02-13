# mypackage/arithmetics.py
# arithmetics.py
import re

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b

def remove_filler(the_dict=dict):
    filler_list=['the','and','of','to','is','in','our','all','for','a','have','this','it','your','with','not','you','what','but','us','has','as','that','every','on','be','or','by','while','â€”','-','their','from','back','are','they','who','was','can','those','who','its','than','been','at','because','when','too','no','cannot','so','will','let']
    for word in filler_list:
        if word in the_dict:
            the_dict.pop(word)
    return the_dict

def find_most_common_words(text,rank):
    word_list = {}
    re.sub(".-™*"," ",text)
    text = text.lower()
    words_in_line = text.split()
    for word in words_in_line:
        if word in word_list:
            word_list[word]+=1
        else:
            word_list[word]=1

    word_list = remove_filler(word_list)
    
    asc = {key: value for key, value in sorted(word_list.items(), key=lambda item: item[1], reverse=True)[:rank]}
    return asc
