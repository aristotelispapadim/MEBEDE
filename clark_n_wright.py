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
print(all_nodes[1].demand)

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
            if(all_nodes[j].type == 1):
                time +=(5/60)
            elif(all_nodes[j].type == 2):
                time +=(15/60)
            elif(all_nodes[j].type == 3):
                time +=(25/60)

                
        else:
            #χρονος μεγαλυτερος του 0
            time = 0
        time_matrix[i][j] = time
#print(time_matrix[4][2])

total_nodes = []
for i in range(1,201):
    total_nodes.append(i)

savings = [[0.0 for j in range(0, len(all_nodes))] for k in range(0, len(all_nodes))]
for i in range(1, len(all_nodes)):
    for j in range(1, len(all_nodes)):
        if(i!=j):
            savings[i][j] = time_matrix[i][0] + time_matrix[0][j] - time_matrix[i][j]


dictionary = {}
for i in range(1, len(all_nodes)):
    for j in range(1, len(all_nodes)):
        dictionary[(i,j)] = [savings[i][j]]
#print(dictionary)

sort_dict = sorted(dictionary.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
  
#sorted savings
nodes=[]
for i in range(0,len(sort_dict)):
    nodes.append(list(sort_dict)[i][0])

print(nodes[0][0])
print(nodes[0][1])


#if():
 #   if((roads[nodes[0][0]][0][1] == nodes[0][0] or roads[nodes[0][0]][0][len(roads[nodes[0][0]][0])-2] == nodes[0][0]) and (roads[nodes[0][1]][0][1] == nodes[0][1] or roads[nodes[0][1]][0][len(roads[nodes[0][1]][0])-2] == nodes[0][1])):

roads = []
roads.append(000)
for i in range (1,201):
    roads.append([0,i,0])

for i in range(1,201):
    if nodes[0][0] in roads[i]:
        pos1 = i
print(pos1)

for i in range(1,201):
    if nodes[0][1] in roads[i]:
        pos2 = i
print(pos2)

if(pos1!=pos2):
    if((roads[pos1][1] == nodes[0][0] or roads[pos1][len(roads[pos1])-2] == nodes[0][0]) and (roads[pos2][1] == nodes[0][1] or roads[pos2][len(roads[pos2])-2] == nodes[0][1])):
        if(all_nodes[pos1].demand + all_nodes[pos2].demand <= 3000):









