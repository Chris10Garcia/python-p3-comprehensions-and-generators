#!/usr/bin/env python3

def return_evens(num_list):
    num_list = [element for element in num_list if element % 2 == 0]
    return num_list

def make_exclamation(sentence_list):
    sentence_list = [word + "!" for word in sentence_list]
    return sentence_list