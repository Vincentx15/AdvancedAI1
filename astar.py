from numpy import *
import heapq as queue # only a suggestion

def find_path(Coords, M, start, goal):
    '''
        Find the shortest path from start to goal.
        
        Parameters
        ----------
        Coords : an N * 2 array
            of 2D coordinates for each of the N nodes
        M : an N * N array 
            defining edge costs, the cost from node j to k is M[j,k] 
        start : int
            the start node (number between 0 and N-1)
        goal : int
            the goal node (number between 0 and N-1)

        Returns
        -------
            the shortest path as a list, e.g., [3, 8, 2, 0] where start = 3, goal = 0
    '''
    # TODO
    return [-1]




