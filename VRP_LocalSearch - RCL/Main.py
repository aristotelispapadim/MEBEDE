from VRP_Model import Model
from Solver_version2 import *

m = Model()
m.BuildModel()
s = Solver(m)
sol = s.solve()
print(sol)
# jnci



