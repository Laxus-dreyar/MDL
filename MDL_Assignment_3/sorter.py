import json
import requests
import numpy as np
import random

class Individual:
    
    def __init__(self,arr,valerror,testerror):
        self.genes = arr
        self.valerror = valerror
        self.testerror = testerror

fd = open("iteration3.txt",'r+')
data = fd.readlines()
fd.close()
j = 0
population = []
vec = []
valerror = 0
testerror = 0
for i in data:
    if j == 0:
        vec = i.split()
        st = ''
        for k in vec[10]:
            if k!='\n':
                st = st + k
        vec[10] = st
    if j == 1:
        st = ''
        for k in i:
            if k!='\n':
                st = st + k
        valerror = float(st)
    if j == 2:
        st = ''
        for k in i:
            if k!='\n':
                st = st + k
        testerror = float(st)
        ind = Individual(vec,valerror,testerror)
        population.append(ind)
    j = j + 1
    j = j%8

population = sorted(population,key=lambda x: x.valerror)
fd = open('weights.txt','w')
for j in population:
    print(j.genes)
    for k in j.genes:
        fd.write("%s "%k)
    fd.write("\n%s"%j.valerror)
    fd.write("\n%s"%j.testerror)
    fd.write("\n\n\n\n\n\n")
fd.close()