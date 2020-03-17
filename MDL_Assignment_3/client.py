import json
import requests
import numpy as np
import random

######### DO NOT CHANGE ANYTHING IN THIS FILE ##################
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

class Individual:

    def __init__(self,arr,valerror,testerror):
        self.genes = arr
        self.valerror = valerror
        self.testerror = testerror
        self.fitness = self.valerror*abs(self.testerror-self.valerror)

    def mate(self,par2):
        vec = []
        for i in range(11):
            prob = random.random()
            if prob < 0.45:
                vec.append(self.genes[i])
            elif prob >=0.45 and prob <0.9:
                vec.append(par2.genes[i])
            else:
                ran = random.random()
                ran = ran*2 - 1
                vec.append(ran)
        cost = compute_cost(vec)
        return Individual(vec,cost[0],cost[1])

if __name__ == "__main__":
    """
    Replace "test" with your secret ID and just run this file 
    to verify that the server is working for your ID.
    """

    # fd = open("population.txt",'w+')
    # population = []
    # population_size = 100
    # fd1 = open("weights.txt",'r')
    # data = fd1.readlines()
    # fd1.close()
    # j = 0
    # vec = []
    # valerror = 0
    # testerror = 0
    # for i in data:
    #     if j == 0:
    #         vec = i.split()
    #         st = ''
    #         for k in vec[10]:
    #             if k!='\n':
    #                 st = st + k
    #         vec[10] = st
    #     if j == 1:
    #         st = ''
    #         for k in i:
    #             if k!='\n':
    #                 st = st + k
    #         valerror = float(st)
    #     if j == 2:
    #         st = ''
    #         for k in i:
    #             if k!='\n':
    #                 st = st + k
    #         testerror = float(st)
    #         ind = Individual(vec,valerror,testerror)
    #         population.append(ind)
    #     j = j + 1
    #     j = j%8

    # vec = [0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
    # cost = compute_cost(vec)
    # ind = Individual(vec,cost[0],cost[1])
    # population.append(ind)
    # for i in range(population_size-1):
    #     vec = []
    #     for j in range(11):
    #         ran = random.random()
    #         ran = ran*2 - 1
    #         vec.append(ran)
    #     cost = compute_cost(vec)
    #     ind = Individual(vec,cost[0],cost[1])
    #     population.append(ind)

    # for i in range(3):
    #     population = sorted(population,key=lambda x: x.fitness)
    #     new_gen = []
    #     s = int(population_size/10)
    #     new_gen.extend(population[:s])
    #     s = population_size-s
    #     for j in range(s):
    #         parent1 = random.choice(population[:50]) 
    #         parent2 = random.choice(population[:50]) 
    #         child = parent1.mate(parent2) 
    #         new_gen.append(child) 
    #     for j in population:
    #         for k in j.genes:
    #             fd.write("%s "%k)
    #         fd.write("%s "%j.fitness)
    #         fd.write("%s "%j.valerror)
    #         fd.write("%s "%j.testerror)
    #         fd.write("\n")
    #     population = new_gen
    
    # population = sorted(population,key=lambda x: x.fitness)
    # for j in population:
    #         for k in j.genes:
    #             fd.write("%s "%k)
    #         fd.write("%s "%j.fitness)
    #         fd.write("%s "%j.valerror)
    #         fd.write("%s "%j.testerror)
    #         fd.write("\n")
    
    # fd.close()

    vec = [-0.00016927573251173823, 0.0010953590656607808, 0.003731869524518327, 0.08922889556431182, 0.03587507175384199, -0.0015634754169704097, -7.439827367266828e-05, 3.7168210026033343e-06, 1.555252501348866e-08, -2.2215895929103804e-09, 2.306783174308054e-11]
    err = get_errors('SHgqKko0w8xXZFisPCJ4BqM7ccC9PHbsOU1eBXFIKo1Zlzcp6j', vec)
    assert len(err) == 2
    print(err[0])
    print(err[1])
    # submit_status = submit('SHgqKko0w8xXZFisPCJ4BqM7ccC9PHbsOU1eBXFIKo1Zlzcp6j', list(-np.arange(0,1.1,0.1)))
    # assert "submitted" in submit_status