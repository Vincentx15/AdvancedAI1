# Generate a matrix M, save it to M.dat

from numpy import *
from numpy.random import *
import matplotlib.pyplot as plt
import networkx as nx

seed(2)   # <-- may be changed
N = 50   # <-- may be changed

G = nx.DiGraph()

# Node positions
G.add_nodes_from(range(N))
XX = rand(N,2) * 100.
pos = {}
for n in range(N):
    pos[n] = XX[n]
    G.node[n]['pos'] = pos[n]

# Edge costs
M = zeros((N,N))
for j in range(N):
    for k in range(N):
        d = sqrt(dot(pos[j] - pos[k],pos[j] - pos[k]))
        if j != k and rand() > 0.95:
            M[j,k] = d + rand() * 20
            M[k,j] = d + rand() * 20

rows, cols = where(M > 0)
edges = zip(rows.tolist(), cols.tolist())
G.add_edges_from(edges)

# Plot & Save
fig = plt.figure()
nx.draw(G, pos, with_labels=True)
savetxt('M.dat',M,fmt='%3.2f')
savetxt('Nodes.dat',XX,fmt='%3.2f')
plt.xticks(arange(0, 100, 1.0))
plt.yticks(arange(0, 100, 1.0))
fig.savefig("M.png")
plt.show()
