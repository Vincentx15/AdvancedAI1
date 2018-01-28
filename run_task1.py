from numpy import *
from astar import find_path

# Edge cost matrix
M = loadtxt('M.dat')

N,N = M.shape
# Node positions 
XX = loadtxt('Nodes.dat')

# Find the shortest path using A*
path = find_path(XX,M,0,12)

# Print the path
print("Path: %s" % str(path))
