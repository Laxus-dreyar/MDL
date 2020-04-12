import json 
  
# Opening JSON file 
f = open('outputs/output.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list
  
# Closing file 
f.close() 

f1 = open('../../output.json',)

data1 = json.load(f1)

f1.close()

a1 = data["objective"]
a2 = data1["objective"]

print(a1,a2)
print(a1 == a2)