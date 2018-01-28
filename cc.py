from numpy import *
import copy
from sklearn.linear_model import LogisticRegression

class CC() :
    '''
        Classifier Chain
    '''

    h = None
    L = -1

    def __init__(self, h=LogisticRegression()):
        ''' 
        Setup.

        Parameters
        ----------
        h : a sklearn model
            The instantiated base classifier

        '''
        self.base_classifier = h

    def fit(self, X, Y):
        ''' 
        Train the chain.

        Parameters
        ----------
        X : input matrix (N * D array)
        Y : label matrix (N * L array)

        '''
        N, self.L = Y.shape
        L = self.L
        N, D = X.shape

        # Copy the base model for each label ...
        self.h = [ copy.deepcopy(self.base_classifier) for j in range(L)]
        XY = zeros((N, D + L-1))
        XY[:,0:D] = X
        XY[:,D:] = Y[:,0:L-1]
        # ... and train each model.
        for j in range(self.L):
            self.h[j].fit(XY[:,0:D+j], Y[:,j])

        return self

    def explore_paths(self, x, epsilon=0.5):
        '''
            epsilon-Greedy exploration of the probability tree.

            Carry out an exploration of the probability tree given instance x,
            using the epsilon-greedy strategy.

            Parameters
            ----------

            x : A D-dimensional array
                contains values for the D input features.

            Returns
            -------

            branches : a list of branches involved in your search, where 
                       a branch is a tuple (parent,child,branch_score,path_score) where
                        parent : an integer array to identify the path to this node
                        child : an integer array to identify the path to this node
                        branch_score : the score by taking this branch
                        path_score : the score obtained so far along the path relevant to this branch
            y        : the best path (of those explored) to a goal node
            p        : the score/payoff associated with this path
        '''

        ###############################################
        # TODO: Rewrite this function
        #       Currently this function is implemented as greedy-search
        #       (equivalent to epsilon >= 0.5), and you should re-write
        #       it so that it works for any epsilon.
        ###############################################

        branches = []          # to store the branches we go down
        y = zeros(self.L)      # an array to store labels (the best path)
        p = 1.                 # p(y|x)
        xy = x.reshape(1,-1)   # make x into a 1 * D array

        for j in range(self.L):
            if j>0:
                # stack the previous y as an additional feature
                xy = column_stack([xy, y[j-1]])
            # P_j := p(y[j]|x,y[1],...,y[j-1])
            P_j = self.h[j].predict_proba(xy)[0] # (N.B. [0], because it is the first and only row)
            k = argmax(P_j)
            y[j] = k
            p = p * P_j[k]
            branch = (y[0:j].astype(int),y[0:j+1].astype(int),P_j[k],p)
            branches.append(branch)

        return branches,y,p


    def predict(self, X, epsilon=0.5):
        ''' 
        Predict.

        Parameters
        ----------
        X : input matrix (N * D array)

        Returns
        -------

        A binary matrix (N * L array) of predictions.

        '''

        N,D = X.shape
        Yp = zeros((N,self.L))

        for n in range(N):
            x = X[n]
            paths,yp,w_max = self.explore_paths(x, epsilon)
            Yp[n] = yp

        return Yp



