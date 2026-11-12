# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:22:48 2024

@author: Thuisgebruik
"""
import pandas as pd 
import random

# the letters "j" and "g" were removed because they can represent two levels of sonority
Vowels = ["a", "o", "u", "i", "e"] #just the short vowels
Affrictions = ["ts", "zz", "tsj"]
Glides = ["w"]
Liquids = ["l", "r"]
Nasals = ["m", "n", "ng"]
Fricatives = ["f", "s", "ch", "c", "sj", "x", "v", "z", "h", "g"]
Plosives = ["p", "t", "k", "q", "b", "d"]
Sonority_Rank = [Vowels, Affrictions, Glides, Liquids, Nasals, Fricatives, Plosives] #from high to low #7-1
# we can use this list to decide whether the target is congruent or not. 
#Illegal bigrams:
Same_Level = []
Congruent_Bigrams = []
Incongruent_Bigrams = []
Sonoritysum = 0
Illegals_str = ["bq", "bx", "cv", "cx", "dq", "dx", "fq", "fx", "gx", "hq", "hx", "iy", "jq", "jx", "jy", "kq", "lx", "pq", "px", "qa",
            "qc", "qb", "qd", "qe", "qf", "qg", "qh", "qi", "qj", "qk", "ql", "qm", "qn", "qo", "qp", "qq", "qr", "qs", "qt", "qv", "qx", "qy", "qz", "sx", "tx", "vb", "vd", "vf", "vg", "vh", "vk", "vm", "vp", "vq", "vt", "vw", "vx", "vz", "wq", "wx", "xj", "xn",
            "xx", "yy", "zh", "zq", "zx"]

#for element in Illegals:
    #if element[1]
    #use a class object here to easily compute sonority?

class Bigram:
    
    vowels = ["a", "o", "u", "i", "e", "aa", "oo", "ie", "ee", "uu", "eu", "ij", "y", "ei", "au", "ou"]
    affrictions = ["ts", "zz", "tsj"]
    glides = ["w"]
    liquids = ["l", "r"]
    nasals = ["m", "n", "ng"]
    fricatives = ["f", "s", "ch", "c", "sj", "x", "v", "z", "h", "g"]
    plosives = ["p", "t", "k", "q", "b", "d"]
    
    def __init__(self, bg):
        self.onset = bg[0]
        self.nucleus = bg[1]
    def full(self):
        return "{}{}".format(self.onset, self.nucleus)
    def onvalue(self):
        if self.onset in Bigram.vowels:
            return 7
        elif self.onset in Bigram.affrictions:
            return 6
        elif self.onset in Bigram.glides:
            return 5
        elif self.onset in Bigram.liquids:
            return 4
        elif self.onset in Bigram.nasals:
            return 3
        elif self.onset in Bigram.fricatives:
            return 2
        elif self.onset in Bigram.plosives:
            return 1
        else:
            return -999
    def nuvalue(self):
        if self.nucleus in Bigram.vowels:
            return 7
        elif self.nucleus in Bigram.affrictions:
            return 6
        elif self.nucleus in Bigram.glides:
            return 5
        elif self.nucleus in Bigram.liquids:
            return 4
        elif self.nucleus in Bigram.nasals:
            return 3
        elif self.nucleus in Bigram.fricatives:
            return 2
        elif self.nucleus in Bigram.plosives:
            return 1
        else:
            return -999
    def congruence(self): #we will be using 1 for congruent, 0 for same sonority and -1 for incongruent
        if self.onvalue() < self.nuvalue():
            return 1
        elif self.onvalue() > self.nuvalue():
            return -1
        else:
            return 0
        
    
        
        
example = Bigram("bq")
print(example.onset)
print(example.full()) #print the full bigram
print(example.onvalue())
print(example.nuvalue())
print(example.congruence())

Illegals_bg = []
for element in Illegals_str:
    element = Bigram(element)
    Illegals_bg.append(element)
print(Illegals_bg)
print(Illegals_bg[1].onset)

Congruents = []
Incongruents = []
Same_Sonority = []
for element in Illegals_bg:
    if element.congruence() == 1:
        Congruents.append(element)
    elif element.congruence() == -1:
        Incongruents.append(element)
    else:
        Same_Sonority.append(element)
print(len(Congruents))
print(len(Incongruents))
print(len(Same_Sonority))
    
for i in Congruents:
    print(i.full())
print("BREAK")
for j in Incongruents:
    print(j.full())
print("BREAK")
for k in Same_Sonority:
    print(k.full())

## Congruency is reversed when the onset-nucleus is used as a nucleus-coda, however this does not count for same-sonority, the validity of which depends on what follows/precedes

""" Stimulus generation """""
#Congruent stimuli
Stim_List = []
Re_Stim_List = []
onset_stim = ""
coda_stim = ""
for i in Congruents:
    onset_stim = ""
    onset_stim = str(i.full())
    for j in Incongruents:
        stim = ""
        random_vowel = str(random.choice(Vowels))
        stim = onset_stim + random_vowel
        stim += str(j.full())
        Stim_List.append(stim)
        coda_stim = str(j.full()) + random_vowel + str(i.full())
        Re_Stim_List.append(coda_stim)
print(Stim_List)


with pd.ExcelWriter(r'C:\Users\Thuisgebruik\Downloads\stim_list_full.xlsx') as writer:
     pd.DataFrame(Stim_List).to_excel(writer, sheet_name='Congruent', header="Stimuli", index=False)
     pd.DataFrame(Re_Stim_List).to_excel(writer, sheet_name='Incongruent', header= 'Stimuli', index=False)
     
print(len(Illegals_str))
     