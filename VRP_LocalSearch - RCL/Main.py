from VRP_Model import Model
from solver_test import * #change solver file

m = Model()
m.BuildModel()
s = Solver(m)
sol = s.solve()
# jnci



