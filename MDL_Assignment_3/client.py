import json
import requests
import numpy as np
import random
import math

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

def submiting(vec):
    submit_status = submit('SHgqKko0w8xXZFisPCJ4BqM7ccC9PHbsOU1eBXFIKo1Zlzcp6j', vec)
    return submit_status

def make_rand(vec):
    arr = []
    for i in range(11):
        y = random.uniform(0.1**15,0.1**17)
        x = random.uniform(vec[i]*0.95,vec[i]*1.05)+y
        arr.append(x)
    cost = compute_cost(arr)
    ind = Individual(arr,cost[0],cost[1])
    return ind

class Individual:

    def __init__(self,arr,trainerror,valerror):
        self.genes = arr
        self.trainerror = trainerror
        self.valerror = valerror
        self.fitness = (self.trainerror) * (pow(self.valerror-self.trainerror,5))

    def mate(self,par2):
        vec = []
        for i in range(11):
            prob = random.random()
            if prob < 0.55:
                vec.append(self.genes[i])
            elif prob >=0.55 and prob <0.9:
                vec.append(par2.genes[i])
            else:
                x = self.genes[i]
                y = par2.genes[i]
                arr = []
                arr.append(x)
                arr.append(y)
                r = random.choice(arr)
                ran = random.uniform(r*0.9,r*1.1)
                ran = max(ran,-10)
                ran = min(ran, 10)
                vec.append(ran)
        if vec == self.genes or vec == par2.genes:
            return self.mate(par2)
        cost = compute_cost(vec)
        return Individual(vec,cost[0],cost[1])

if __name__ == "__main__":
    """
    Replace "test" with your secret ID and just run this file 
    to verify that the server is working for your ID.
    """

    # fd = open("trace.txt",'w+')
    # population = []
    # population_size = 100

    # fd1 = open("last_iteration.txt",'r')
    # data = fd1.readlines()
    # fd1.close()
    

    # """ uncomment for reading from file last_iteration.txt """
    # # for i in range(len(data)):

    # #     if i!=0 and data[i] == data[i-1]:
    # #         continue

    # #     arr = data[i].split(" ")
    # #     vec = []

    # #     for j in range(11):
    # #         x = float(arr[j])
    # #         vec.append(x)

    # #     trainerror = float(arr[12])
    # #     valerror = float(arr[13])
    # #     ind = Individual(vec,trainerror,valerror)
    # #     population.append(ind)

    # """ This is the code for initial population"""
    # vec = [0.0, 0.1240317450077846, -6.211941063144333, 0.04933903144709126, 0.03810848157715883, 8.132366097133624e-05, -6.018769160916912e-05, -1.251585565299179e-07, 3.484096383229681e-08, 4.1614924993407104e-11, -6.732420176902565e-12]
    # cost = compute_cost(vec)
    # ind = Individual(vec,cost[0],cost[1])
    # population.append(ind)
    # for i in range(99):
    #     ind = make_rand(vec)
    #     population.append(ind)


    # for i in range(10):
    #     population = sorted(population,key=lambda x: x.fitness)
    #     new_gen = []
        
    #     new_gen.extend(population[:10])
        
    #     for j in population:
    #         for k in j.genes:
    #             fd.write("%s "%k)
    #         fd.write("%s "%j.fitness)
    #         fd.write("%s "%j.trainerror)
    #         fd.write("%s "%j.valerror)
    #         fd.write("\n")
        
    #     while True:
            
    #         s = population_size - len(new_gen)
            
    #         for j in range(s):
    #             parent1 = random.choice(population[:40]) 
    #             parent2 = random.choice(population[:40]) 
    #             if parent1.fitness < parent2.fitness:
    #                 temp = parent1
    #                 parent1 = parent2
    #                 parent2 = temp
    #             child = parent1.mate(parent2) 
    #             new_gen.append(child)
            
    #         new_gen_temp = []
            
    #         for j in range(population_size):
    #             if j!=0 and new_gen[j].valerror == new_gen[j-1].valerror:
    #                 continue
    #             new_gen_temp.append(new_gen[j])
            
    #         new_gen = new_gen_temp
            
    #         if(len(new_gen) == population_size):
    #             break

    #     print(i+1,"iterations done")
    #     population = new_gen
        
    #     population = sorted(population,key=lambda x: x.fitness)
    #     # for i in range(20):
    #     #     sub_stat = submiting(population[i].genes)
    #     #     print(sub_stat,population[i].trainerror,population[i].valerror)
        
    #     # population = sorted(population,key=lambda x: x.valerror)
    #     # for i in range(20):
    #     #     sub_stat = submiting(population[i].genes)
    #     #     print(sub_stat,population[i].trainerror,population[i].valerror)
    
    # population = sorted(population,key=lambda x: x.fitness)
    # for j in population:
    #     for k in j.genes:
    #         fd.write("%s "%k)
    #     fd.write("%s "%j.fitness)
    #     fd.write("%s "%j.trainerror)
    #     fd.write("%s "%j.valerror)
    #     fd.write("\n")
    
    # fd.close()

    # population = sorted(population,key=lambda x: x.valerror)

    # for i in range(20):
    #     # print(population[i].genes)
    #     sub_stat = submiting(population[i].genes)
    #     print(sub_stat,population[i].trainerror,population[i].valerror)

    population = []
    population_size = 10
    fd = open("values.txt",'r')
    data = fd.readlines()
    fd.close()

    print("initial population")
    
    for i in range(10):
        print(population[i].genes)

    for i in range(10):
        
        print("population : " + str(i+1))
        population = sorted(population,key=lambda x: x.fitness)
        new_gen = []

        for j in range(9):
            arr = [0,1,2,3]
            x = int(random.choice(arr))
            y = int(random.choice(arr))
            parent1 = population[x]
            parent2 = population[y]
            if parent1.fitness < parent2.fitness:
                temp = parent1
                parent1 = parent2
                parent2 = temp
            child = parent1.mate(parent2) 
            new_gen.append(child)
            print(child.genes,x,y)
        population = new_gen