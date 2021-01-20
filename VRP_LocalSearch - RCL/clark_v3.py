import random
import math
from VRP_Model import *


savings = [[0.0 for j in range(0, len(allNodes))] for k in range(0, len(allNodes))]
for i in range(1, len(allNodes)):
    for j in range(1, len(allNodes)):
        if(i<j):
            savings[i][j] = matrix[i][0] + matrix[0][j] - matrix[i][j]

dictionary = {}
for i in range(1, len(allNodes)):
    for j in range(1, len(allNodes)):
        dictionary[(i,j)] = [savings[i][j]]

sort_dict = sorted(dictionary.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
  
#sorted savings
nodes=[]
for i in range(0,len(sort_dict)):
    nodes.append(list(sort_dict)[i][0])


roads = []
roads.append(000)
for i in range (1,201):
    roads.append([0,i,0])

for k in range(0,len(sort_dict)):
    
    for i in range(1,201):
        if nodes[k][0] in roads[i]:
            pos1 = i
        if nodes[k][1] in roads[i]:
            pos2 = i

    if(pos1!=pos2):
        if((roads[pos1][1] == nodes[k][0] or roads[pos1][len(roads[pos1])-2] == nodes[k][0]) and (roads[pos2][1] == nodes[k][1] or roads[pos2][len(roads[pos2])-2] == nodes[k][1])):
            n0 = nodes[k][0]
            n1 = nodes[k][1]
            if(len(roads[pos1])<len(roads[pos2])):
                pos1,pos2 = pos2,pos1
                n0,n1=n1,n0
            sum1 = 0
            sum2 = 0
            for i in range(1,len(roads[pos1])-1):
                sum1 += allNodes[roads[pos1][i]].demand
            for i in range(1,len(roads[pos2])-1):
                sum2 += allNodes[roads[pos2][i]].demand
            if((sum1 + sum2) <= 2300):
                roads[pos1].insert(len(roads[pos1])-1,n1) #προσθετω στην πρωτη διαδρομη την δευτερη διαδρομη
                roads[pos2]=[0,0,0]  # σβηνω τη διαδρομη που εχω προσθεσει

count = 0
mymax=-1
for i in range(1,201):
    if(roads[i]!=[0,0,0]):
        count+=1
        # print(roads[i])
        time_sum=0
        for j in range(0,len(roads[i])-2):
            if(allNodes[roads[i][j+1]].type == 1):
                time_out =(5/60)
            elif(allNodes[roads[i][j+1]].type == 2):
                time_out =(15/60)
            elif(allNodes[roads[i][j+1]].type == 3):
                time_out =(25/60)
            time_sum+=matrix[roads[i][j]][roads[i][j+1]]
            time_sum+=time_out
        #print(time_sum)
        if(mymax<time_sum):
            mymax=time_sum

#print(count)
# print(mymax)
