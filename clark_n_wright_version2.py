import random
import math


class Node:
    def __init__(self, id, tp, dem, xx, yy):
        self.id = id
        self.type = tp
        self.demand = dem
        self.x = xx
        self.y = yy

all_nodes = []
service_locations = []
depot = Node(0, 0, 0, 50, 50)
all_nodes.append(depot)
random.seed(1)

for i in range(0, 200):
    id = i + 1
    tp = random.randint(1,3)
    dem = random.randint(1,5) * 100
    xx = random.randint(0, 100)
    yy = random.randint(0, 100)
    serv_node = Node(id, tp, dem, xx, yy)
    all_nodes.append(serv_node)
    service_locations.append(serv_node)
#print(all_nodes[1].demand)

dist_matrix = [[0.0 for j in range(0, len(all_nodes))] for k in range(0, len(all_nodes))]
for i in range(0, len(all_nodes)):
    for j in range(0, len(all_nodes)):
        source = all_nodes[i]
        target = all_nodes[j]
        dx_2 = (source.x - target.x)**2
        dy_2 = (source.y - target.y) ** 2
        dist = round(math.sqrt(dx_2 + dy_2))
        dist_matrix[i][j] = dist





time_matrix = [[0.0 for j in range(0, len(all_nodes))] for k in range(0, len(all_nodes))]
for i in range(0, len(all_nodes)):
    for j in range(0, len(all_nodes)):
        if(i != j):
            time = dist_matrix [i][j] / 35            
        else:
            #χρονος μεγαλυτερος του 0
            time = 0
        time_matrix[i][j] = time



savings = [[0.0 for j in range(0, len(all_nodes))] for k in range(0, len(all_nodes))]
for i in range(1, len(all_nodes)):
    for j in range(1, len(all_nodes)):
        if(i<j):
            savings[i][j] = time_matrix[i][0] + time_matrix[0][j] - time_matrix[i][j]

dictionary = {}
for i in range(1, len(all_nodes)):
    for j in range(1, len(all_nodes)):
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
                sum1 += all_nodes[roads[pos1][i]].demand
            for i in range(1,len(roads[pos2])-1):
                sum2 += all_nodes[roads[pos2][i]].demand
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
            if(all_nodes[roads[i][j+1]].type == 1):
                time_out =(5/60)
            elif(all_nodes[roads[i][j+1]].type == 2):
                time_out =(15/60)
            elif(all_nodes[roads[i][j+1]].type == 3):
                time_out =(25/60)
            time_sum+=time_matrix[roads[i][j]][roads[i][j+1]]
            time_sum+=time_out
        #print(time_sum)
        if(mymax<time_sum):
            mymax=time_sum

#print(count)
# print(mymax)

'''
mylist = [[0,1,50,65,101,130,150,165,183],
[0,2,46,74,77,96,120,146,179],
[0,3,34,72,104,123,145,162,194],
[0,4,40,80,103,138,163,175,198],
[0,5,49,59,70,98,106,140,166,195],
[0,6,36,62,91,107,131,178],
[0,7,33,73,99,105,126,153,169],
[0,8,47,78,115,143,167,193],
[0,9,39,61,90,100,108,119,133,159,177,187],
[0,10,51,75,85,102,127,154,173],
[0,11,48,82,111,142,156,184],
[0,12,30,41,69,93,125,151,164],
[0,13,38,79,94,141,158,196,199],
[0,14,29,60,88,117,135,155,180,200],
[0,15,43,57,95,124,148,181,189],
[0,16,52,87,122,160,192],
[0,17,27,44,76,112,137,171,188],
[0,18,31,56,64,86,116,149,174,185],
[0,19,28,55,71,110,129,168],
[0,20,32,58,84,114,147,170,191],
[0,21,37,53,67,97,144,161,197],
[0,22,35,81,118,136,157,190],
[0,23,42,68,89,128,139,176,186],
[0,24,54,92,113,134,152,182],
[0,25,26,45,63,66,83,109,121,132,172]]   

max1=-1
for i in range(0,24):
    newtime_sum=0
    for j in range(0,len(mylist[i])-1):
        if(all_nodes[mylist[i][j+1]].type == 1):
            newtime_out =(5/60)
        elif(all_nodes[mylist[i][j+1]].type == 2):
            newtime_out =(15/60)
        elif(all_nodes[mylist[i][j+1]].type == 3):
            newtime_out =(25/60)
        newtime_sum+=time_matrix[mylist[i][j]][mylist[i][j+1]]
        newtime_sum+=newtime_out
    #print(newtime_sum)
    if(max1<newtime_sum):
        max1=newtime_sum
print(max1)
'''