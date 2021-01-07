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
    for j in range(1, len(all_nodes)):
        if(i != j):
            time = dist_matrix [i][j] / 35
            if(all_nodes[j].type == 1):
                time +=(5/60)
            elif(all_nodes[j].type == 2):
                time +=(15/60)
            else:
                time +=(25/60)
        else:
            #χρονος μεγαλυτερος του 0
            time = 0
        time_matrix[i][j] = time

time_matrixA = time_matrix.copy()


total_nodes = []
for i in range(1,201):
    total_nodes.append(i)


trucks = {}
for i in range (1,26):
    trucks[i] = [[0],3000]

#trucks[1] = [[0,8,9,6],2500]
#print(trucks.get(1)[0][3])
#trucks.get(1)[0].append(17)


#για καθε γραμμη i βρισκω το ελαχιστο j (στηλη)
def FindMin(a):
    min = 100000
    min_pos = 0
    for j in range (1, len(all_nodes)):
        if(time_matrix[a][j] < min and time_matrix[a][j] > 0):
            min = time_matrix[a][j]
            min_pos = j
            minimums = [min, min_pos]
    return minimums

#pos = mins[1]
#if(trucks.get(1)[1] >= all_nodes[pos].demand):
  #  trucks.get(1)[0].append(pos)
    #trucks.get(1)[1] -= all_nodes[pos].demand
    #for i in range(0, len(all_nodes)):
      #  time_matrixA[i][pos] = 0


mins = []
for i in range (1,26):
    last_number = trucks.get(i)[0][(len(trucks.get(i)[0])-1)]
    mins.append(FindMin(last_number))
    pos = mins.get(i-1)[1]
    if(trucks.get(i)[1] < all_nodes[pos].demand):
        

min_of_mins = 100000
for i in range (0,25):
    if(mins[i][0] < min_of_mins):
        min_of_mins = mins[i][0]
        pos_min = mins[i][1]
        truck = i+1

for i in range (1,26):
    if(trucks.get(truck))
if()

print(min_of_mins)

    