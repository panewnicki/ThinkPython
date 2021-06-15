# -*- coding: utf-8 -*-

def create_my_dict(text):
    file = open(text)
    my_dict = {}
    
    for line in file:
        word = line.strip()
        word2 = list(word)
        word2.sort()
        dict_key = ""
        for letter in word2:
            dict_key += letter
        
        if dict_key not in my_dict:
            my_dict[dict_key] = [word]
        else:
            my_dict[dict_key] += [word]

    return my_dict

#12.4.1.
def set_of_anagrams(text):
    d = create_my_dict(text) 
    
    for key, value in d.items():
        if len(value) > 1:
            print (value)

#12.4.2.
def anagrams_dict_sorted(text):
    d = create_my_dict(text) 
    my_list = []
    
    for key, value in d.items():
        if len(value) > 1:
            t = (len(value), value)
            my_list.append(t)
    my_list.sort(reverse=True)
    for length, value in my_list:
        print(length, value)

#12.4.3.
def bingo_list(text):
    d = create_my_dict(text)     
    scrabble_list = []
    
    for key, value in d.items():
        if len(key) == 8 and len(value) > 1:
            t = (len(value), key, value)
            scrabble_list.append(t)
            
    scrabble_list.sort(reverse=True)

    print(scrabble_list[0][1], scrabble_list[0][2])