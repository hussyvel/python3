# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:56:47 2019

@author: Hussyvel
"""

#def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            ++score
    return score


  