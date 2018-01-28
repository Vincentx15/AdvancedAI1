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
    
    n = shape(M)[0]
    precedent = [start for i in range(n)]
    distance_start = [2**14 for i in range(n)]
    distance_start[start]=0;
    q = []
    queue.heappush(q,(start,0))
    
    #tant que la queue n'est pas vide, il reste des sommets connectés à start qui n'ont pas été explorés
    while (q):
        sommet, distance_sommet = queue.heappop(q)
        
        #si le sommet est le but, on retrace le chemin
        if(sommet==goal):
            output = [goal]
            previous = goal
            while (previous!=start):
                previous = precedent[previous]
                output = [previous] + output
            return output
        
        for voisin in range(n):
            #on selectionne les voisins du sommet et on regarde si il vaut mieux passer par le sommet
            if (M[sommet,voisin]):
                dist_par_sommet = distance_start[sommet]+M[sommet, voisin]
                #si oui, on note la nouvelle distance et le précédent, et on met le voisin dans la queue
                #Attention, le voisin peut rentrer plusieurs fois dans la queue mais l'inégalité est stricte 
                #donc ses voisins ne peuvent rentrer qu'une fois dans la queue par ce sommet
                if(dist_par_sommet < distance_start[voisin]): 
                    distance_start[voisin] = dist_par_sommet
                    precedent[voisin] = sommet
                    queue.heappush(q,(voisin, dist_par_sommet))
                    
    #Si on a pas atteint le noeud goal et que la liste est vide, les noeuds ne sont pas reliés         
    return [-1]




