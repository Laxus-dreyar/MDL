import numpy as np

shoot = np.zeros((60,60))
dogde = np.zeros((60,60))
recharge = np.zeros((60,60))
utility = np.zeros(60)
absstate = np.zeros(60)

gamma = 0.99
delta = 0.001
penalty = -1

#shoot action
for i in range(0,60):   #i = x*20 + y*5 + z
    x = int(i/20)       #x represents stamina/50
    y = int((i%20)/5)   #y represents arrows
    z = int(i%5)        #z represents health/25
    
    if z == 0:
        for j in range(0,60):
            shoot[i][j] = -1
            utility[i] = 10
            absstate[i] = 1

    elif x == 0 or y == 0:
        shoot[i][i] = 1

    else:
        shoot[i][i-25] = 0.5
        shoot[i][i-26] = 0.5

#dodge action
for i in range(0,60):   #i = x*20 + y*5 + z
    x = int(i/20)       #x represents stamina/50
    y = int((i%20)/5)   #y represents arrows
    z = int(i%5)        #z represents health/25
    
    if z == 0:
        for j in range(0,60):
            dogde[i][j] = -1

    else:

        if y == 3:
            if x == 0:
                dogde[i][i] = 1

            elif x == 1:
                dogde[i][i-20] = 1
            
            elif x == 2:
                dogde[i][i-20] = 0.8
                dogde[i][i-40] = 0.2
        
        else:
            if x == 0:
                dogde[i][i] = 1

            elif x == 1:
                dogde[i][i-15] = 0.8
                dogde[i][i-20] = 0.2
            
            elif x == 2:
                dogde[i][i-15] = 0.64
                dogde[i][i-20] = 0.16
                dogde[i][i-40] = 0.16
                dogde[i][i-35] = 0.04

#recharge action
for i in range(0,60):   #i = x*20 + y*5 + z
    x = int(i/20)       #x represents stamina/50
    y = int((i%20)/5)   #y represents arrows
    z = int(i%5)        #z represents health/25
    
    if z == 0:
        for j in range(0,60):
            recharge[i][j] = -1

    elif x == 2:
        recharge[i][i] = 1

    else:
        recharge[i][i+20] = 0.8
        recharge[i][i] = 0.2

print(utility)
for i in range(0,60):   #i = x*20 + y*5 + z
    x = int(i/20)       #x represents stamina/50
    y = int((i%20)/5)   #y represents arrows
    z = int(i%5)        #z represents health/25

    if z == 0:
        continue

    ma = 0
    ac = 0
    for j in range(60):
        ma += utility[j] * shoot[i][j]
    
    temp = ma
    ma = 0

    for j in range(60):
        ma += utility[j] * dogde[i][j]
    
    if ma > temp:
        ac = 1
    
    temp = ma
    ma = 0

    for j in range(60):
        ma += utility[j] * recharge[i][j]
    
    if ma > temp:
        ac = 1
    
    print("(",x,",",y,",",z,")=",ac)