from VRP_Model import *
#from SolutionDrawer import *

class Solution:
    def __init__(self):
        self.cost = 0.0
        self.routes = []
        self.maximum = 0.0

class RelocationMove(object):
    def __init__(self):
        self.originRoutePosition = None
        self.targetRoutePosition = None
        self.originNodePosition = None
        self.targetNodePosition = None
        self.costChangeOriginRt = None
        self.costChangeTargetRt = None
        self.moveCost = None

    def Initialize(self):
        self.originRoutePosition = None
        self.targetRoutePosition = None
        self.originNodePosition = None
        self.targetNodePosition = None
        self.costChangeOriginRt = None
        self.costChangeTargetRt = None
        self.moveCost = 10 ** 9

class Solver:
    def __init__(self, m):
        self.allNodes = m.allNodes
        self.customers = m.customers
        self.depot = m.allNodes[0]
        self.distanceMatrix = m.matrix
        self.capacity = m.capacity
        self.sol = None
        self.bestSolution = None
        self.overallBestSol = None
        self.rcl_size = 3


    def Clark(self):
        savings = [[0.0 for j in range(0, len(self.allNodes))] for k in range(0, len(self.allNodes))]
        for i in range(1, len(self.allNodes)):
            for j in range(1, len(self.allNodes)):
                if(i<j):
                    savings[i][j] = self.distanceMatrix[i][0] + self.distanceMatrix[0][j] - self.distanceMatrix[i][j]

        dictionary = {}
        for i in range(1, len(self.allNodes)):
            for j in range(1, len(self.allNodes)):
                dictionary[(i,j)] = [savings[i][j]]

        sort_dict = sorted(dictionary.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
        
        #sorted savings
        nodes=[]
        for i in range(0,len(sort_dict)):
            nodes.append(list(sort_dict)[i][0])


        roads = []
        roads.append([0,0,0])
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
                        sum1 += self.allNodes[roads[pos1][i]].demand
                    for i in range(1,len(roads[pos2])-1):
                        sum2 += self.allNodes[roads[pos2][i]].demand
                    if((sum1 + sum2) <= 2300):
                        roads[pos1].insert(len(roads[pos1])-1,n1) #προσθετω στην πρωτη διαδρομη την δευτερη διαδρομη
                        roads[pos2]=[0,0,0]  # σβηνω τη διαδρομη που εχω προσθεσει

        return roads

    def Time(self, road):
        time_sum=0
        for j in range(0,len(road)-2):
            """
            if(self.allNodes[roads[i][j+1]].type == 1):
                time_out =(5/60)
            elif(self.allNodes[roads[i][j+1]].type == 2):
                time_out =(15/60)
            elif(self.allNodes[roads[i][j+1]].type == 3):
                time_out =(25/60)
            """
            time_sum+=self.distanceMatrix[road[j]][road[j+1]]
            #time_sum+=time_out
        #print(time_sum)
        return time_sum

    def Load(self, r: Route):
        load = 0
        for i in range(0,len(r.sequenceOfNodes)-1):
            load += r.sequenceOfNodes[i].demand
        return load


    def solve(self):
        self.sol = Solution()
        clark = self.Clark()
        max1 = -1
        for i in range(0, len(clark)):
            road = []
            if clark[i] != [0,0,0]:
                for j in range(0, len(clark[i])):
                    for k in range(0, len(self.allNodes)):
                        if clark[i][j] == self.allNodes[k].ID:
                            road.append(self.allNodes[k])
                r = Route(road, self.capacity)
                r.cost = self.Time(clark[i])
                if r.cost > max1:
                    max1 = r.cost
                r.load = self.Load(r)
                self.sol.routes.append(r) #possible error
        self.sol.maximum = max1       
        for i in range(3): 
            cc = self.sol.maximum
            #print(i, 'Constr:', self.sol.maximum)
            self.LocalSearch(0)
            if self.overallBestSol == None or self.overallBestSol.maximum > self.sol.maximum:
                self.overallBestSol = self.cloneSolution(self.sol)
            #print(i, 'Const: ', cc, ' LS:', self.sol.maximum, 'BestOverall: ', self.overallBestSol.cost)
            #SolDrawer.draw(i, self.sol, self.allNodes)

        self.sol = self.overallBestSol
        self.ReportSolution(self.sol)
        #SolDrawer.draw(10000, self.sol, self.allNodes)
        return self.sol
   

    def LocalSearch(self, operator):
        self.bestSolution = self.cloneSolution(self.sol)
        terminationCondition = False
        localSearchIterator = 0

        rm = RelocationMove()

        while terminationCondition is False:

            self.InitializeOperators(rm)
            # SolDrawer.draw(localSearchIterator, self.sol, self.allNodes)

            # Relocations
            if operator == 0:
                self.FindBestRelocationMove(rm)
                if rm.originRoutePosition is not None:
                    if rm.moveCost < 0:
                        self.ApplyRelocationMove(rm)
                    else:
                        terminationCondition = True

            self.TestSolution()

            if (self.sol.cost < self.bestSolution.cost):
                self.bestSolution = self.cloneSolution(self.sol)

            localSearchIterator = localSearchIterator + 1

        self.sol = self.bestSolution


    def cloneRoute(self, rt:Route):
        cloned = Route(self.depot, self.capacity)
        cloned.cost = rt.cost
        cloned.load = rt.load
        cloned.sequenceOfNodes = rt.sequenceOfNodes.copy()
        return cloned

    def cloneSolution(self, sol: Solution):
        cloned = Solution()
        for i in range (0, len(sol.routes)):
            rt = sol.routes[i]
            clonedRoute = self.cloneRoute(rt)
            cloned.routes.append(clonedRoute)
        cloned.cost = self.sol.cost
        return cloned

    def FindBestRelocationMove(self, rm):
        for originRouteIndex in range(0, len(self.sol.routes)):
            rt1:Route = self.sol.routes[originRouteIndex]
            for targetRouteIndex in range (0, len(self.sol.routes)):
                rt2:Route = self.sol.routes[targetRouteIndex]
                for originNodeIndex in range (1, len(rt1.sequenceOfNodes) - 1):
                    for targetNodeIndex in range (0, len(rt2.sequenceOfNodes) - 1):

                        if originRouteIndex == targetRouteIndex and (targetNodeIndex == originNodeIndex or targetNodeIndex == originNodeIndex - 1):
                            continue

                        A = rt1.sequenceOfNodes[originNodeIndex - 1]
                        B = rt1.sequenceOfNodes[originNodeIndex]
                        C = rt1.sequenceOfNodes[originNodeIndex + 1]

                        F = rt2.sequenceOfNodes[targetNodeIndex]
                        G = rt2.sequenceOfNodes[targetNodeIndex + 1]

                        if rt1 != rt2:
                            if rt2.load + B.demand > rt2.capacity:
                                continue
                        if(C.ID != 0 and G.ID != 0):
                            costAdded = self.distanceMatrix[A.ID][C.ID] + self.distanceMatrix[F.ID][B.ID] + self.distanceMatrix[B.ID][G.ID]
                            costRemoved = self.distanceMatrix[A.ID][B.ID] + self.distanceMatrix[B.ID][C.ID] + self.distanceMatrix[F.ID][G.ID]

                            originRtCostChange = self.distanceMatrix[A.ID][C.ID] - self.distanceMatrix[A.ID][B.ID] - self.distanceMatrix[B.ID][C.ID]
                            targetRtCostChange = self.distanceMatrix[F.ID][B.ID] + self.distanceMatrix[B.ID][G.ID] - self.distanceMatrix[F.ID][G.ID]
                        elif(C.ID == 0 and G.ID != 0):
                            costAdded = self.distanceMatrix[F.ID][B.ID] + self.distanceMatrix[B.ID][G.ID]
                            costRemoved = self.distanceMatrix[A.ID][B.ID] + self.distanceMatrix[F.ID][G.ID]

                            originRtCostChange = (-1)*(self.distanceMatrix[A.ID][B.ID])
                            targetRtCostChange = self.distanceMatrix[F.ID][B.ID] + self.distanceMatrix[B.ID][G.ID] - self.distanceMatrix[F.ID][G.ID]
                        elif(G.ID ==0 and C.ID != 0):
                            costAdded = self.distanceMatrix[A.ID][C.ID] + self.distanceMatrix[F.ID][B.ID]
                            costRemoved = self.distanceMatrix[A.ID][B.ID] + self.distanceMatrix[B.ID][C.ID]

                            originRtCostChange = self.distanceMatrix[A.ID][C.ID] - self.distanceMatrix[A.ID][B.ID] - self.distanceMatrix[B.ID][C.ID]
                            targetRtCostChange = self.distanceMatrix[F.ID][B.ID]
                        elif(G.ID ==0 and C.ID == 0):
                            costAdded = self.distanceMatrix[F.ID][B.ID]
                            costRemoved = self.distanceMatrix[A.ID][B.ID]

                            originRtCostChange = (-1)*(self.distanceMatrix[A.ID][B.ID])
                            targetRtCostChange = self.distanceMatrix[F.ID][B.ID]

                        moveCost = costAdded - costRemoved

                        if (moveCost < rm.moveCost):
                            self.StoreBestRelocationMove(originRouteIndex, targetRouteIndex, originNodeIndex, targetNodeIndex, moveCost, originRtCostChange, targetRtCostChange, rm)

    def ApplyRelocationMove(self, rm: RelocationMove):
    
        oldCost = self.CalculateTotalCost(self.sol)

        originRt = self.sol.routes[rm.originRoutePosition]
        targetRt = self.sol.routes[rm.targetRoutePosition]

        B = originRt.sequenceOfNodes[rm.originNodePosition]

        if originRt == targetRt:
            del originRt.sequenceOfNodes[rm.originNodePosition]
            if (rm.originNodePosition < rm.targetNodePosition):
                targetRt.sequenceOfNodes.insert(rm.targetNodePosition, B)
            else:
                targetRt.sequenceOfNodes.insert(rm.targetNodePosition + 1, B)

            originRt.cost += rm.moveCost
        else:
            del originRt.sequenceOfNodes[rm.originNodePosition]
            targetRt.sequenceOfNodes.insert(rm.targetNodePosition + 1, B)
            originRt.cost += rm.costChangeOriginRt
            targetRt.cost += rm.costChangeTargetRt
            originRt.load -= B.demand
            targetRt.load += B.demand

        self.sol.cost += rm.moveCost

        newCost = self.CalculateTotalCost(self.sol)
        #debuggingOnly
        if abs((newCost - oldCost) - rm.moveCost) > 0.0001:
            print('Cost Issue')

    def ReportSolution(self, sol):
        for i in range(0, len(sol.routes)):
            r = sol.routes[i]
            for j in range (1, len(r.sequenceOfNodes)-1):
                if(r.sequenceOfNodes[j].type == 1):
                    time_out =(5/60)
                elif(r.sequenceOfNodes[j].type == 2):
                    time_out =(15/60)
                elif(r.sequenceOfNodes[j].type == 3):
                    time_out =(25/60)
                r.cost+=time_out
        maxofall = 0.0
        for i in range(0, len(sol.routes)):
            rt = sol.routes[i]
            if(len(rt.sequenceOfNodes)>2):
                for j in range (0, len(rt.sequenceOfNodes)-1):
                    print(rt.sequenceOfNodes[j].ID, end=' ')
                print(rt.cost)
                if(rt.cost>maxofall):
                    maxofall=rt.cost
        print(maxofall)

    def StoreBestRelocationMove(self, originRouteIndex, targetRouteIndex, originNodeIndex, targetNodeIndex, moveCost, originRtCostChange, targetRtCostChange, rm:RelocationMove):
        rm.originRoutePosition = originRouteIndex
        rm.originNodePosition = originNodeIndex
        rm.targetRoutePosition = targetRouteIndex
        rm.targetNodePosition = targetNodeIndex
        rm.costChangeOriginRt = originRtCostChange
        rm.costChangeTargetRt = targetRtCostChange
        rm.moveCost = moveCost

    def CalculateTotalCost(self, sol):
        c = 0
        for i in range (0, len(sol.routes)):
            rt = sol.routes[i]
            for j in range (0, len(rt.sequenceOfNodes) - 2):
                a = rt.sequenceOfNodes[j]
                b = rt.sequenceOfNodes[j + 1]
                c += self.distanceMatrix[a.ID][b.ID]
        return c

    def InitializeOperators(self, rm):
        rm.Initialize()

    def TestSolution(self):
        totalSolCost = 0
        for r in range (0, len(self.sol.routes)):
            rt: Route = self.sol.routes[r]
            rtCost = 0
            rtLoad = 0
            for n in range (0 , len(rt.sequenceOfNodes) - 2):
                A = rt.sequenceOfNodes[n]
                B = rt.sequenceOfNodes[n + 1]
                rtCost += self.distanceMatrix[A.ID][B.ID]
            for n in range (0 , len(rt.sequenceOfNodes) - 1):
                A = rt.sequenceOfNodes[n]
                rtLoad += A.demand
            if abs(rtCost - rt.cost) > 0.0001:
                print ('Route Cost problem')
                print ('object cost', rt.cost)
                print ('rtcost',rtCost)
                for w in range (0 , len(rt.sequenceOfNodes)):
                    print (rt.sequenceOfNodes[w].ID, end= ',')
            if rtLoad != rt.load:
                print ('Route Load problem')

            totalSolCost += rt.cost
    