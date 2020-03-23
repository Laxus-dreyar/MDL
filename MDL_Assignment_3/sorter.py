import json
import requests
import numpy as np
import random
import math

API_ENDPOINT = 'http://10.4.21.147'
PORT = 3000
MAX_DEG = 11

#### functions that you can call
def get_errors(id, vector):
    """
    returns python array of length 2 
    (train error and validation error)
    """
    for i in vector: assert -10<=abs(i)<=10
    assert len(vector) == MAX_DEG

    return json.loads(send_request(id, vector, 'geterrors'))

def submit(id, vector):
    """
    used to make official submission of your weight vector
    returns string "successfully submitted" if properly submitted.
    """
    for i in vector: assert -10<=abs(i)<=10
    assert len(vector) == MAX_DEG
    return send_request(id, vector, 'submit')

#### utility functions
def urljoin(root, port, path=''):
    root = root + ':' + str(port)
    if path: root = '/'.join([root.rstrip('/'), path.rstrip('/')])
    return root

def send_request(id, vector, path):
    api = urljoin(API_ENDPOINT, PORT, path)
    vector = json.dumps(vector)
    response = requests.post(api, data={'id':id, 'vector':vector}).text
    if "reported" in response:
        print(response)
        exit()

    return response


def compute_cost(vec):
    cost = get_errors('SHgqKko0w8xXZFisPCJ4BqM7ccC9PHbsOU1eBXFIKo1Zlzcp6j', vec)
    return cost

def submiting(vec):
    submit_status = submit('SHgqKko0w8xXZFisPCJ4BqM7ccC9PHbsOU1eBXFIKo1Zlzcp6j', vec)
    return submit_status

class Individual:

    def __init__(self,arr,trainerror,valerror):
        self.genes = arr
        self.trainerror = trainerror
        self.valerror = valerror
        self.fitness = abs(self.trainerror - self.valerror)

    def mate(self,par2):
        vec = []
        for i in range(11):
            prob = random.random()
            if prob < 0.55:
                vec.append(self.genes[i])
            elif prob >=0.55 and prob <0.9:
                vec.append(par2.genes[i])
            else:
                ran = random.random()
                ran = ran*2 - 1
                vec.append(ran)
        if vec == self.genes or vec == par2.genes:
            return self.mate(par2)
        cost = compute_cost(vec)
        return Individual(vec,cost[0],cost[1])

if __name__ == "__main__":
    
    fd = open("array.txt",'r')
    data = fd.readlines()
    fd.close
    population = []
    population_size = 100
    
    for i in data:
        arr = i.split(" ")
        vec = []
        for j in range(11):
            vec.append(float(arr[j]))
        
        trainerror = float(arr[12])
        valerror = float(arr[13])
        ind = Individual(vec,trainerror,valerror)
        population.append(ind)

    fd = open("values.txt",'w+')
    population = sorted(population,key=lambda x: x.fitness)
    for j in population:
            for k in j.genes:
                fd.write("%s "%k)
            fd.write("%s "%j.fitness)
            fd.write("%s "%j.trainerror)
            fd.write("%s "%j.valerror)
            fd.write("\n")
    fd.close()