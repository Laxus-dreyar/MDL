import numpy as np
import os


path = './outputs'
try:  
    os.mkdir(path)  
except OSError as error:  
    x=0

shoot = np.zeros((60,60))
dogde = np.zeros((60,60))
recharge = np.zeros((60,60))
utility = np.zeros(60)
absstate = np.zeros(60)

gamma = 0.99
delta = 0.001
penalty = -10
team_num = 88
arr = [0.5,1,2]
y_for_pur = team_num%3
penalty = penalty/arr[y_for_pur]
fd = open('./outputs/task_1_trace.txt','w+')
#shoot action
for i in range(0,60):   #i = x*20 + y*5 + z
    x = int(i/20)       #x represents stamina/50
    y = int((i%20)/5)   #y represents arrows
    z = int(i%5)        #z represents health/25
    
    if z == 0:
        for j in range(0,60):
            shoot[i][j] = 0
            absstate[i] = 1

    elif x == 0 or y == 0:
        shoot[i][i] = 0

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
            dogde[i][j] = 0

    else:

        if y == 3:
            if x == 0:
                dogde[i][i] = 0

            elif x == 1:
                dogde[i][i-20] = 1
            
            elif x == 2:
                dogde[i][i-20] = 0.8
                dogde[i][i-40] = 0.2
        
        else:
            if x == 0:
                dogde[i][i] = 0

            elif x == 1:
                dogde[i][i-15] = 0.8
                dogde[i][i-20] = 0.2
            
            elif x == 2:
                dogde[i][i-15] = 0.64
                dogde[i][i-20] = 0.16
                dogde[i][i-35] = 0.16
                dogde[i][i-40] = 0.04

#recharge action
for i in range(0,60):   #i = x*20 + y*5 + z
    x = int(i/20)       #x represents stamina/50
    y = int((i%20)/5)   #y represents arrows
    z = int(i%5)        #z represents health/25
    
    if z == 0:
        for j in range(0,60):
            recharge[i][j] = 0

    elif x == 2:
        recharge[i][i] = 1

    else:
        recharge[i][i+20] = 0.8
        recharge[i][i] = 0.2

k=0
while True:

    new_ut = np.zeros(60)
    policy = []
    print("iteration=",end="",file=fd)
    print(k,file=fd)
    # break
    for i in range(0,60):   #i = x*20 + y*5 + z
        x = int(i/20)       #x represents stamina/50
        y = int((i%20)/5)   #y represents arrows
        z = int(i%5)        #z represents health/25

        
        new_ut[i] = utility[i]
        if z == 0:
            policy.append("-1")
            continue

        ma = 0
        fg = 1
        ac = "SHOOT"
        for j in range(60):
            z1 = int(j%5)
            if(z1 == 0):
                ma += (utility[j]*gamma) * shoot[i][j]
            else:
                ma += (utility[j]*gamma + penalty) * shoot[i][j]
        
        temp = ma
        if ma == 0:
            fg = 0
        ma = 0

        for j in range(60):
            z1 = int(j%5)
            if(z1 == 0):
                ma += (utility[j]*gamma) * dogde[i][j]
            else:    
                ma += (utility[j]*gamma + penalty) * dogde[i][j]
        
        if temp == 0:
            ac = "DODGE"
            temp = ma
            if temp == 0:
                fg = 0
            else:
                fg = 1
        
        else:
            if ma > temp:
                ac = "DODGE"    
            temp = max(temp,ma)
            ma = 0

        for j in range(60):
            z1 = int(j%5)
            if(z1 == 0):
                ma += (utility[j]*gamma) * recharge[i][j]
            else:    
                ma += (utility[j]*gamma + penalty) * recharge[i][j]
        
        if temp == 0:
            ac = "RECHARGE"
            temp = ma
        else:
            if ma > temp:
                ac = "RECHARGE"
            temp = max(temp,ma)
            
        # print("(",x,",",y,",",z,")=",ac)
        new_ut[i] = float(temp)
        policy.append(ac)

    for z in range(5):
        for y in range(4):
            for x in range(3):
                if z == 0:
                    print("(",z,",",y,",",x,"):-1=[0.000]",sep="",file=fd)
                else:
                    i = x*20 + y*5 + z
                    print("(",z,",",y,",",x,"):",policy[i],"=[",'%.3f'%new_ut[i],"]",sep="",file=fd)
                    
    delerror = 0
    for i in range(60):
        delerror = max(abs(new_ut[i]-utility[i]),delerror)
    # print(delerror)
    for i in range(60):
        utility[i] = new_ut[i]
    if delerror < delta:
        break
    k += 1
    print("",file=fd)
    print("",file=fd)
# print(k)
# print(utility)





#################################TASK---2#####################
shoot = np.zeros((60,60))
dogde = np.zeros((60,60))
recharge = np.zeros((60,60))
utility = np.zeros(60)
absstate = np.zeros(60)

gamma = 0.99
delta = 0.001
penalty = -10
team_num = 88
arr = [0.5,1,2]
y_for_pur = team_num%3
penalty = penalty/arr[y_for_pur]
fd = open('./outputs/task_2_part_1_trace.txt','w+')

#shoot action
for i in range(0,60):   #i = x*20 + y*5 + z
    x = int(i/20)       #x represents stamina/50
    y = int((i%20)/5)   #y represents arrows
    z = int(i%5)        #z represents health/25
    
    if z == 0:
        for j in range(0,60):
            shoot[i][j] = 0
            absstate[i] = 1

    elif x == 0 or y == 0:
        shoot[i][i] = 0

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
            dogde[i][j] = 0

    else:

        if y == 3:
            if x == 0:
                dogde[i][i] = 0

            elif x == 1:
                dogde[i][i-20] = 1
            
            elif x == 2:
                dogde[i][i-20] = 0.8
                dogde[i][i-40] = 0.2
        
        else:
            if x == 0:
                dogde[i][i] = 0

            elif x == 1:
                dogde[i][i-15] = 0.8
                dogde[i][i-20] = 0.2
            
            elif x == 2:
                dogde[i][i-15] = 0.64
                dogde[i][i-20] = 0.16
                dogde[i][i-35] = 0.16
                dogde[i][i-40] = 0.04

#recharge action
for i in range(0,60):   #i = x*20 + y*5 + z
    x = int(i/20)       #x represents stamina/50
    y = int((i%20)/5)   #y represents arrows
    z = int(i%5)        #z represents health/25
    
    if z == 0:
        for j in range(0,60):
            recharge[i][j] = 0

    elif x == 2:
        recharge[i][i] = 1

    else:
        recharge[i][i+20] = 0.8
        recharge[i][i] = 0.2

k=0
while True:

    new_ut = []
    policy = []
    print("iteration=",end="",file=fd)
    print(k,file=fd)
    # break
    for i in range(60):   #i = x*20 + y*5 + z
        x = int(i/20)       #x represents stamina/50
        y = int((i%20)/5)   #y represents arrows
        z = int(i%5)        #z represents health/25

        if z == 0:
            new_ut.append(0)
            policy.append("-1")
            continue

        ma = 0
        fg = 1
        ac = "SHOOT"
        for j in range(60):
            z1 = int(j%5)
            if(z1 == 0):
                ma += (utility[j]*gamma + 10 - 0.25) * shoot[i][j]
            else:    
                ma += (utility[j]*gamma - 0.25) * shoot[i][j]
        
        ma_lis = []

        if ma == 0:
            ma_lis.append(-1000000000000)
        else:
            ma_lis.append(ma)
        ma = 0

        for j in range(60):
            z1 = int(j%5)
            if(z1 == 0):
                ma += (utility[j]*gamma + 7.5) * dogde[i][j]
            else:    
                ma += (utility[j]*gamma - 2.5) * dogde[i][j]
        
        
        if ma == 0:
            ma_lis.append(-1000000000000)
        else:
            ma_lis.append(ma)
        ma = 0

        for j in range(60):
            z1 = int(j%5)
            if(z1 == 0):
                ma += (utility[j]*gamma + 7.5) * recharge[i][j]
            else:    
                ma += (utility[j]*gamma - 2.5) * recharge[i][j]
        
        
        if ma == 0:
            ma_lis.append(-1000000000000)
        else:
            ma_lis.append(ma)

        temp = max(ma_lis)
        new_ut.append(temp)
        for i in range(3):
            if ma_lis[i] == temp:
                if i == 0:
                    ac = "SHOOT"
                elif i == 1:
                    ac = "DODGE"
                else:
                    ac = "RECHARGE"
        # print("(",x,",",y,",",z,")=",ac)
        # new_ut[i] = float(temp)
        policy.append(ac)
    # print(new_ut)
    for z in range(5):
        for y in range(4):
            for x in range(3):
                if z == 0:
                    print("(",z,",",y,",",x,"):-1=[0.000]",sep="",file=fd)
                else:
                    i = x*20 + y*5 + z
                    print("(",z,",",y,",",x,"):",policy[i],"=[",'%.3f'%new_ut[i],"]",sep="",file=fd)
                    
    delerror = 0
    for i in range(60):
        delerror = max(abs(new_ut[i]-utility[i]),delerror)
    # print(delerror)
    for i in range(60):
        utility[i] = new_ut[i]
    if delerror < delta:
        break
    k += 1
    print("",file=fd)
    print("",file=fd)
# print(k)
# print(utility)

shoot = np.zeros((60,60))
dogde = np.zeros((60,60))
recharge = np.zeros((60,60))
utility = np.zeros(60)
absstate = np.zeros(60)

gamma = 0.1
delta = 0.001
penalty = -2.5
team_num = 88
arr = [0.5,1,2]
y_for_pur = team_num%3
penalty = penalty/arr[y_for_pur]
penalty = -2.5
fd = open('./outputs/task_2_part_2_trace.txt','w+')

#shoot action
for i in range(0,60):   #i = x*20 + y*5 + z
    x = int(i/20)       #x represents stamina/50
    y = int((i%20)/5)   #y represents arrows
    z = int(i%5)        #z represents health/25
    
    if z == 0:
        for j in range(0,60):
            shoot[i][j] = 0
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
            dogde[i][j] = 0

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
                dogde[i][i-35] = 0.16
                dogde[i][i-40] = 0.04

#recharge action
for i in range(0,60):   #i = x*20 + y*5 + z
    x = int(i/20)       #x represents stamina/50
    y = int((i%20)/5)   #y represents arrows
    z = int(i%5)        #z represents health/25
    
    if z == 0:
        for j in range(0,60):
            recharge[i][j] = 0

    elif x == 2:
        recharge[i][i] = 1

    else:
        recharge[i][i+20] = 0.8
        recharge[i][i] = 0.2

k=0
while True:

    new_ut = np.zeros(60)
    policy = []
    print("iteration=",end="",file=fd)
    print(k,file=fd)
    # break
    for i in range(0,60):   #i = x*20 + y*5 + z
        x = int(i/20)       #x represents stamina/50
        y = int((i%20)/5)   #y represents arrows
        z = int(i%5)        #z represents health/25

        
        new_ut[i] = utility[i]
        if z == 0:
            policy.append("-1")
            continue

        ma = 0
        ac = "SHOOT"
        for j in range(60):
            z1 = int(j%5)
            if(z1 == 0):
                ma += (utility[j]*gamma + 7.5) * shoot[i][j]
            else:    
                ma += (utility[j]*gamma + penalty) * shoot[i][j]
        
        temp = ma
        ma = 0

        for j in range(60):
            z1 = int(j%5)
            if(z1 == 0):
                ma += (utility[j]*gamma + 7.5) * dogde[i][j]
            else:    
                ma += (utility[j]*gamma + penalty) * dogde[i][j]
        
        if ma > temp:
            ac = "DODGE"
        
        temp = max(temp,ma)
        ma = 0

        for j in range(60):
            z1 = int(j%5)
            if(z1 == 0):
                ma += (utility[j]*gamma + 7.5 ) * recharge[i][j]
            else:    
                ma += (utility[j]*gamma + penalty) * recharge[i][j]
        
        if ma > temp:
            ac = "RECHARGE"
        temp = max(temp,ma)
        # print("(",x,",",y,",",z,")=",ac)
        new_ut[i] = float(temp)
        policy.append(ac)

    for z in range(5):
        for y in range(4):
            for x in range(3):
                if z == 0:
                    print("(",z,",",y,",",x,"):-1=[0.000]",sep="",file=fd)
                else:
                    i = x*20 + y*5 + z
                    print("(",z,",",y,",",x,"):",policy[i],"=[",'%.3f'%new_ut[i],"]",sep="",file=fd)
                    
    delerror = 0
    for i in range(60):
        delerror = max(abs(new_ut[i]-utility[i]),delerror)
    # print(delerror)
    for i in range(60):
        utility[i] = new_ut[i]
    if delerror < delta:
        break
    k += 1
    print("",file=fd)
    print("",file=fd)
# print(k)
# print(utility)

shoot = np.zeros((60,60))
dogde = np.zeros((60,60))
recharge = np.zeros((60,60))
utility = np.zeros(60)
absstate = np.zeros(60)

gamma = 0.1
delta = 0.0000000001
team_num = 88
penalty = -2.5
arr = [0.5,1,2]
y_for_pur = team_num%3
penalty = penalty/arr[y_for_pur]
penalty = -2.5
fd = open('./outputs/task_2_part_3_trace.txt','w+')

#shoot action
for i in range(0,60):   #i = x*20 + y*5 + z
    x = int(i/20)       #x represents stamina/50
    y = int((i%20)/5)   #y represents arrows
    z = int(i%5)        #z represents health/25
    
    if z == 0:
        for j in range(0,60):
            shoot[i][j] = 0
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
            dogde[i][j] = 0

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
                dogde[i][i-35] = 0.16
                dogde[i][i-40] = 0.04

#recharge action
for i in range(0,60):   #i = x*20 + y*5 + z
    x = int(i/20)       #x represents stamina/50
    y = int((i%20)/5)   #y represents arrows
    z = int(i%5)        #z represents health/25
    
    if z == 0:
        for j in range(0,60):
            recharge[i][j] = 0

    elif x == 2:
        recharge[i][i] = 1

    else:
        recharge[i][i+20] = 0.8
        recharge[i][i] = 0.2

k=0
while True:

    new_ut = np.zeros(60)
    policy = []
    print("iteration=",end="",file=fd)
    print(k,file=fd)
    # break
    for i in range(0,60):   #i = x*20 + y*5 + z
        x = int(i/20)       #x represents stamina/50
        y = int((i%20)/5)   #y represents arrows
        z = int(i%5)        #z represents health/25

        
        new_ut[i] = utility[i]
        if z == 0:
            policy.append("-1")
            continue

        ma = 0
        ac = "SHOOT"
        for j in range(60):
            z1 = int(j%5)
            if(z1 == 0):
                ma += (utility[j]*gamma + 7.5) * shoot[i][j]
            else:    
                ma += (utility[j]*gamma + penalty) * shoot[i][j]
        
        temp = ma
        ma = 0

        for j in range(60):
            z1 = int(j%5)
            if(z1 == 0):
                ma += (utility[j]*gamma + 7.5) * dogde[i][j]
            else:    
                ma += (utility[j]*gamma + penalty) * dogde[i][j]
        
        if ma > temp:
            ac = "DODGE"
        
        temp = max(temp,ma)
        ma = 0

        for j in range(60):
            z1 = int(j%5)
            if(z1 == 0):
                ma += (utility[j]*gamma + 7.5) * recharge[i][j]
            else:    
                ma += (utility[j]*gamma + penalty) * recharge[i][j]
        
        if ma > temp:
            ac = "RECHARGE"
        temp = max(temp,ma)
        # print("(",x,",",y,",",z,")=",ac)
        new_ut[i] = float(temp)
        policy.append(ac)

    for z in range(5):
        for y in range(4):
            for x in range(3):
                if z == 0:
                    print("(",z,",",y,",",x,"):-1=[0.000]",sep="",file=fd)
                else:
                    i = x*20 + y*5 + z
                    print("(",z,",",y,",",x,"):",policy[i],"=[",'%.3f'%new_ut[i],"]",sep="",file=fd)
                    
    delerror = 0
    for i in range(60):
        delerror = max(abs(new_ut[i]-utility[i]),delerror)
    # print(delerror)
    for i in range(60):
        utility[i] = new_ut[i]
    if delerror < delta:
        break
    k += 1
    print("",file=fd)
    print("",file=fd)
# print(k)
# print(utility)