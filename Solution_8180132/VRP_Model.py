import random
import math


class Model:

# instance variables
    def __init__(self):
        self.allNodes = []
        self.customers = []
        self.matrix = []
        self.capacity = -1

    def BuildModel(self):
        random.seed(1)
        depot = Node(0, 0, 0, 50, 50)
        self.allNodes.append(depot)
        self.capacity = 2500 #try different capacitys for better solutions  (2500 for rm)
        totalCustomers = 200
        for i in range (0, totalCustomers):
            id = i + 1
            tp = random.randint(1,3)
            dem = random.randint(1, 5)*100
            xx = random.randint(0, 100)
            yy = random.randint(0, 100)
            cust = Node(i + 1, tp, dem, xx, yy)
            self.allNodes.append(cust)
            self.customers.append(cust)

        rows = len(self.allNodes)
        self.matrix = [[0.0 for x in range(rows)] for y in range(rows)]

        for i in range(0, rows):
            for j in range(0, rows):
                a = self.allNodes[i]
                b = self.allNodes[j]
                time = round((math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))))/35
                self.matrix[i][j] = time



class Node:
    def __init__(self, id, tp, dem, xx, yy):
        self.ID = id
        self.type = tp
        self.demand = dem
        self.x = xx
        self.y = yy
        self.isRouted = False

class Route:
    def __init__(self, nodes, cap):
        self.sequenceOfNodes = nodes
        #self.sequenceOfNodes.append(dp)
        #self.sequenceOfNodes.append(dp)
        self.cost = 0
        self.capacity = cap
        self.load = 0